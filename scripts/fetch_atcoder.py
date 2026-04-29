#!/usr/bin/env python3
import os
import sys
import argparse
import requests
from bs4 import BeautifulSoup

try:
    import markdownify
except ImportError:
    print("markdownify 모듈이 필요합니다. 'pip install markdownify bs4 requests' 를 실행해주세요.")
    sys.exit(1)

def get_problem_statement(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")
    task_statement = soup.select_one("#task-statement")
    
    if not task_statement:
        return None
        
    lang_en = task_statement.select_one(".lang-en")
    lang_ja = task_statement.select_one(".lang-ja")
    
    content = ""
    if lang_ja and lang_en:
        content += "## 🇯🇵 問題文 (Japanese)\n\n" + markdownify.markdownify(str(lang_ja), heading_style="ATX")
        content += "\n\n---\n\n## 🇬🇧 Problem Statement (English)\n\n" + markdownify.markdownify(str(lang_en), heading_style="ATX")
    else:
        content += markdownify.markdownify(str(task_statement), heading_style="ATX")
        
    title_tag = soup.select_one("title")
    title = title_tag.text.split(" - ")[0].strip() if title_tag else "Unknown Problem"
    
    return title, content

def main():
    parser = argparse.ArgumentParser(description="AtCoder 문제 지문을 Markdown으로 다운로드합니다.")
    parser.add_argument("contest_id", help="콘테스트 ID (예: abc455)")
    parser.add_argument("--acc-mode", action="store_true", help="acc 폴더 구조(예: abc455/a/)에 맞춰 README.md로 저장합니다.")
    
    args = parser.parse_args()
    contest_id = args.contest_id.lower()
    tasks = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] # 넉넉하게 G번까지 시도
    
    print(f"🚀 {contest_id.upper()} 문제 지문 다운로드를 시작합니다...\n")

    for task_id in tasks:
        url = f"https://atcoder.jp/contests/{contest_id}/tasks/{contest_id}_{task_id}"
        
        result = get_problem_statement(url)
        if not result:
            # 문제가 없으면(예: 4문제짜리 대회에서 e번 시도) 조용히 넘어감
            continue
            
        title, content = result
        
        if args.acc_mode:
            # acc new abc455 로 생성된 폴더 구조 사용: content/atcoder/abc455/a/README.md
            target_dir = os.path.join("content", "atcoder", contest_id, task_id)
            os.makedirs(target_dir, exist_ok=True)
            file_path = os.path.join(target_dir, f"{task_id.upper()}.md")
        else:
            target_dir = os.path.join("content", "atcoder", contest_id)
            os.makedirs(target_dir, exist_ok=True)
            file_path = os.path.join(target_dir, f"{task_id.upper()}.md")
            
        frontmatter = f"""---
title: "[AtCoder] {title}"
tags: ["AtCoder", "{contest_id.upper()}"]
---

# {title}

[AtCoder Problem Link: {title}]({url})

"""
        
        footer = f"""
---

## 💡 해결 방법
<!-- 이 문제에 대한 접근 방식과 풀이를 작성하세요 -->

## 💻 코드

```python
import sys

def solve():
    # 여기에 코드를 작성하세요
    pass

if __name__ == '__main__':
    solve()
```
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(frontmatter + content + footer)
            
        print(f"✅ Saved: {file_path}")

    print(f"\n🎉 문제 지문 변환이 완료되었습니다!")

if __name__ == "__main__":
    main()
