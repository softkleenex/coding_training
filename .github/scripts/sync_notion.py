import os
import glob
import yaml
from notion_client import Client

def main():
    notion_token = os.getenv("NOTION_TOKEN")
    database_id = os.getenv("NOTION_DATABASE_ID")
    
    if not notion_token or not database_id:
        print("Missing NOTION_TOKEN or NOTION_DATABASE_ID environment variables.")
        return

    notion = Client(auth=notion_token)
    
    # Get existing pages in the database to avoid duplicates
    existing_pages = {}
    try:
        results = notion.databases.query(database_id=database_id).get("results", [])
        for page in results:
            # Assuming the database has a title property named "Name" or "Title"
            title_prop = page["properties"].get("Name") or page["properties"].get("Title")
            if title_prop and title_prop["title"]:
                title = title_prop["title"][0]["plain_text"]
                existing_pages[title] = page["id"]
    except Exception as e:
        print(f"Error querying Notion Database: {e}")
        return

    # Process markdown files in the posts directory
    post_files = glob.glob("posts/*.md")
    for file_path in post_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Simple YAML frontmatter parser
        frontmatter = {}
        body = content
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1]) or {}
                except Exception as e:
                    print(f"Error parsing YAML in {file_path}: {e}")
                body = parts[2].strip()

        title = frontmatter.get("title", os.path.basename(file_path).replace(".md", ""))
        tags = frontmatter.get("tags", [])
        status = frontmatter.get("status", "Draft")

        if title in existing_pages:
            print(f"Post '{title}' already exists in Notion. Skipping to prevent duplicates.")
            continue

        print(f"Syncing '{title}' to Notion...")

        # Build properties
        properties = {
            "Name": {
                "title": [
                    {"text": {"content": title}}
                ]
            },
            "Status": {
                "select": {"name": status}
            }
        }

        if tags:
            properties["Tags"] = {
                "multi_select": [{"name": tag} for tag in tags]
            }

        # Build blocks (simple paragraph blocks, chunked if necessary)
        blocks = []
        for paragraph in body.split("\n\n"):
            if not paragraph.strip():
                continue
            
            # Notion limits text content to 2000 characters per block
            chunk_size = 2000
            for i in range(0, len(paragraph), chunk_size):
                chunk = paragraph[i:i+chunk_size]
                blocks.append({
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {"type": "text", "text": {"content": chunk}}
                        ]
                    }
                })

        try:
            notion.pages.create(
                parent={"database_id": database_id},
                properties=properties,
                children=blocks[:100]  # Notion API allows max 100 blocks per request
            )
            print(f"Successfully synced '{title}'!")
        except Exception as e:
            print(f"Failed to sync '{title}': {e}")

if __name__ == "__main__":
    main()
