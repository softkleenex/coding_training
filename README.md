# Softkleenex's Coding Training Blog

이 저장소는 백준(Baekjoon), AtCoder 등 알고리즘 문제 풀이 기록을 저장하고 배포하는 **옵시디언(Obsidian) 기반 정적 블로그(Quartz)** 입니다.

### 🌐 블로그 주소
👉 **[https://softkleenex.github.io/coding_training/](https://softkleenex.github.io/coding_training/)**

---

## 🛠 블로그 워크플로우

1. **백준/AtCoder 문제 풀이:**
   * 기존에 사용하시던 [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub) 익스텐션을 통해 문제를 풀면 자동으로 이 저장소에 코드가 커밋됩니다.
2. **자동 마크다운 변환:**
   * 새로운 소스 코드가 푸시되면 깃허브 액션(`Auto Format Coding Problems`)이 동작하여 코드를 마크다운(`.md`) 파일과 블로그 템플릿 형태로 변환합니다.
3. **옵시디언(Obsidian)에서 풀이 작성:**
   * 로컬에 연동된 폴더를 옵시디언으로 열어, 각 문제의 `💡 해결 방법` 섹션에 본인만의 풀이와 회고를 작성합니다.
4. **블로그 자동 배포:**
   * 작성한 내용을 `git push`하면, 깃허브 액션(`Deploy Quartz site to GitHub Pages`)이 즉시 블로그를 빌드하여 위 URL로 배포합니다.

---

## 📂 폴더 구조
* `content/백준/` : 백준 문제 풀이 아카이브 (난이도별 폴더)
* `content/atcoder/` : AtCoder 문제 풀이 아카이브
* `content/posts/` : 알고리즘 외 자유로운 개발 블로그 포스트 작성 공간
* `scripts/` : 템플릿 변환 및 자동화 Python 스크립트
