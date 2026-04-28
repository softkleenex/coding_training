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
        ".rs": "go",
        ".kt": "rust",
        ".swift": "kotlin",
    }
    return ext_map.get(ext.lower(), "")

def format_readme(readme_path):
    dir_path = os.path.dirname(readme_path)
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if already formatted (has frontmatter or custom section)
    if "---" in content[:10] or "## 💡" in content:
        return False
        
    # Extract title from the first line, usually looks like: # [Bronze V] A+B - 1000
    title_match = re.search(r'^#\s+\[(.*?)\]\s+(.*)', content, re.MULTILINE)
    difficulty = "Unrated"
    problem_title = "Unknown Problem"
    
    if title_match:
        difficulty = title_match.group(1).strip()
        problem_title = title_match.group(2).strip()
    
    # Try to find the source code file in the same directory
    code_files = [f for f in os.listdir(dir_path) if f != "README.md" and os.path.isfile(os.path.join(dir_path, f))]
    
    code_content = ""
    language = ""
    if code_files:
        # Assuming the first non-readme file is the source code
        code_file = code_files[0]
        ext = os.path.splitext(code_file)[1]
        language = get_language_from_ext(ext)
        
        try:
            with open(os.path.join(dir_path, code_file), 'r', encoding='utf-8') as cf:
                code_content = cf.read()
        except Exception:
            pass

    # Prepare Frontmatter
    platform = "백준" if "백준" in dir_path else "AtCoder" if "atcoder" in dir_path.lower() else "Algorithm"
    frontmatter = f"""---
title: "[{difficulty}] {problem_title}"
tags: ["{platform}", "{difficulty}"]
---

"""
    
    # Prepare the new appended sections
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

def main():
    # Process Baekjoon
    baekjoon_readmes = glob.glob("content/백준/**/README.md", recursive=True)
    atcoder_readmes = glob.glob("content/atcoder/**/README.md", recursive=True)
    
    all_readmes = baekjoon_readmes + atcoder_readmes
    
    updated_count = 0
    for readme in all_readmes:
        if format_readme(readme):
            updated_count += 1
            print(f"Formatted: {readme}")
            
    print(f"Total {updated_count} files formatted.")

if __name__ == "__main__":
    main()
