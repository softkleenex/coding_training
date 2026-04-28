import os
import glob
import re

def count_problems():
    stats = {
        "백준": {
            "Bronze": 0,
            "Silver": 0,
            "Gold": 0,
            "Platinum": 0,
            "Unrated": 0,
            "Total": 0
        },
        "AtCoder": {
            "Total": 0
        }
    }

    # Count Baekjoon
    bj_dirs = [d for d in os.listdir("content/백준") if os.path.isdir(os.path.join("content/백준", d))]
    for difficulty in bj_dirs:
        if difficulty not in stats["백준"]:
            stats["백준"][difficulty] = 0
            
        problems = glob.glob(f"content/백준/{difficulty}/**/*.md", recursive=True)
        # Filter out index.md or other non-problem files if any
        problems = [p for p in problems if not p.endswith("index.md")]
        
        count = len(problems)
        stats["백준"][difficulty] += count
        stats["백준"]["Total"] += count

    # Count AtCoder
    if os.path.exists("content/atcoder"):
        ac_problems = glob.glob("content/atcoder/**/*.md", recursive=True)
        ac_problems = [p for p in ac_problems if not p.endswith("index.md")]
        stats["AtCoder"]["Total"] += len(ac_problems)

    return stats

def update_readme(stats):
    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Build the stats markdown
    stats_md = f"""<!-- problems:start -->
### 🏆 Algorithm Solving Status

**Total Solved: {stats['백준']['Total'] + stats['AtCoder']['Total']} Problems**

| Platform | Difficulty | Solved Count |
| :--- | :--- | :---: |
| **Baekjoon** | 🥉 Bronze | {stats['백준'].get('Bronze', 0)} |
| | 🥈 Silver | {stats['백준'].get('Silver', 0)} |
| | 🥇 Gold | {stats['백준'].get('Gold', 0)} |
| | 💎 Platinum | {stats['백준'].get('Platinum', 0)} |
| | ❔ Unrated | {stats['백준'].get('Unrated', 0)} |
| | **Total** | **{stats['백준']['Total']}** |
| **AtCoder** | - | **{stats['AtCoder']['Total']}** |
<!-- problems:end -->"""

    # Check if marker exists, if not, insert before the folder structure section
    if "<!-- problems:start -->" in readme_content:
        new_content = re.sub(
            r"<!-- problems:start -->.*?<!-- problems:end -->",
            stats_md,
            readme_content,
            flags=re.DOTALL
        )
    else:
        # Insert before "## 📂 디렉토리 구조"
        parts = readme_content.split("## 📂 디렉토리 구조")
        if len(parts) == 2:
            new_content = parts[0] + "## 📊 성과 대시보드\n\n" + stats_md + "\n\n## 📂 디렉토리 구조" + parts[1]
        else:
            new_content = readme_content + "\n\n" + stats_md

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

def main():
    stats = count_problems()
    update_readme(stats)
    print("Successfully updated README.md with problem statistics.")

if __name__ == "__main__":
    main()
