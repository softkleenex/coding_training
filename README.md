# Automated Notion Blog from GitHub

Welcome to the new structure! The repository has been transitioned from an old Baekjoon auto-sync repository to an **Automated Notion Blog Hub**.

### 🌟 How It Works
1. Write a markdown file in the `posts/` folder.
2. Ensure you include the proper YAML frontmatter (title, tags, status).
3. Commit and push to the `main` branch.
4. The `.github/workflows/notion-sync.yml` workflow automatically grabs your post and publishes it to your specified Notion Database!

### 🔧 One-Time Setup Instructions

Since you are transitioning to this automated flow, you need to configure your Notion credentials.

#### 1. Set up a Notion Database
1. Open your [softkleenex_blog](https://www.notion.so/softkleenex_blog-34d86836bc57808d95e9cea425f1e744) page in Notion.
2. Create a new **Database - Inline** or **Full page**.
3. Add the following Properties to the database exactly as spelled:
   - `Name` (Type: Title)
   - `Status` (Type: Select) -> Add options: `Draft`, `Published`
   - `Tags` (Type: Multi-select)
4. Get your **Database ID**: Open the database as a full page. The URL looks like `https://notion.so/your-workspace/{DATABASE_ID}?v=...`. Copy that 32-character `{DATABASE_ID}`.

#### 2. Get your Notion API Token
1. Go to [Notion Integrations](https://www.notion.so/my-integrations).
2. Create a new Integration (e.g., "GitHub Sync Bot").
3. Copy the **Internal Integration Secret (NOTION_TOKEN)**.
4. **CRITICAL**: Go back to your Notion Database page, click the `...` menu in the top right, click **Connect to**, and select the integration you just created to give it access.

#### 3. Add GitHub Secrets
1. Go to your GitHub repository -> **Settings** -> **Secrets and variables** -> **Actions**.
2. Click **New repository secret**.
3. Add `NOTION_TOKEN` and paste your Internal Integration Secret.
4. Add `NOTION_DATABASE_ID` and paste your Database ID.

That's it! Now every push to the `posts/` folder will be synced to your blog.

### 🗂 Archive
Old competitive programming files (Baekjoon, AtCoder) have been moved to the `archive/` folder.
