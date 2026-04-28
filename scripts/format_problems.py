import os
import glob
import re

def get_language_from_ext(ext):
    ext_map = {
        ".py": "python",
        ".c": "c",
        ".cc": "cpp",
        ".cpp": "cpp",
        ".java": "java",
        ".js": "javascript",
        ".ts": "typescript",
        ".go": "go",
        ".rs": "rust",
        ".kt": "kotlin",
        ".swift": "swift",
    }
    return ext_map.get(ext.lower(), "")

def format_readme(readme_path):
    dir_path = os.path.dirname(readme_path)
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if already formatted
    if "---" in content[:10] or "## 💡" in content:
        return False
        
    title_match = re.search(r'^#\s+\[(.*?)\]\s+(.*)', content, re.MULTILINE)
    difficulty = "Unrated"
    problem_title = "Unknown Problem"
    
    if title_match:
        difficulty = title_match.group(1).strip()
        problem_title = title_match.group(2).strip()
    
    code_files = [f for f in os.listdir(dir_path) if f != "README.md" and not f.endswith(".md") and os.path.isfile(os.path.join(dir_path, f))]
    
    code_content = ""
    language = ""
    if code_files:
        code_file = code_files[0]
        ext = os.path.splitext(code_file)[1]
        language = get_language_from_ext(ext)
        
        try:
            with open(os.path.join(dir_path, code_file), 'r', encoding='utf-8') as cf:
                code_content = cf.read()
        except Exception:
            pass

    platform = "백준" if "백준" in dir_path else "AtCoder" if "atcoder" in dir_path.lower() else "Algorithm"
    frontmatter = f"""---
title: "[{difficulty}] {problem_title}"
tags: ["{platform}", "{difficulty}"]
---

"""
    
    custom_sections = f"""

---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->

## 💻 코드

```{language}
{code_content}
```
"""
    
    new_content = frontmatter + content + custom_sections
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    return True

def create_md_for_standalone_code(code_path):
    dir_path = os.path.dirname(code_path)
    filename = os.path.basename(code_path)
    name, ext = os.path.splitext(filename)
    
    language = get_language_from_ext(ext)
    if not language:
        return False
        
    # If README.md exists, it's handled by format_readme
    if os.path.exists(os.path.join(dir_path, "README.md")):
        return False
        
    md_path = os.path.join(dir_path, f"{name}.md")
    
    # If a markdown file with the same name already exists, skip
    if os.path.exists(md_path):
        return False

    with open(code_path, 'r', encoding='utf-8') as cf:
        code_content = cf.read()

    platform = "백준" if "백준" in dir_path else "AtCoder" if "atcoder" in dir_path.lower() else "Algorithm"
    difficulty = "Unrated"

    content = f"""---
title: "[{platform}] {name}"
tags: ["{platform}", "{difficulty}"]
---

# {name}

이 문제는 {platform}에서 푼 문제입니다. 문제 설명이 제공되지 않았습니다.

---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->

## 💻 코드

```{language}
{code_content}
```
"""
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    return True

def main():
    updated_count = 0
    
    # 1. Process README.md files
    readmes = glob.glob("content/백준/**/README.md", recursive=True) + glob.glob("content/atcoder/**/README.md", recursive=True)
    for readme in readmes:
        if format_readme(readme):
            updated_count += 1
            print(f"Formatted README: {readme}")
            
    # 2. Process standalone code files (like AtCoder files without README)
    code_files = []
    for ext in [".py", ".cc", ".cpp", ".java", ".c"]:
        code_files.extend(glob.glob(f"content/백준/**/*{ext}", recursive=True))
        code_files.extend(glob.glob(f"content/atcoder/**/*{ext}", recursive=True))
        
    for code_file in code_files:
        if create_md_for_standalone_code(code_file):
            updated_count += 1
            print(f"Created MD for code: {code_file}")
            
    print(f"Total {updated_count} files formatted/created.")

if __name__ == "__main__":
    main()
