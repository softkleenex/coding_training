<div align="center">

# 🚀 Softkleenex's Coding Training

[![Deploy Status](https://github.com/softkleenex/coding_training/actions/workflows/deploy.yml/badge.svg)](https://github.com/softkleenex/coding_training/actions/workflows/deploy.yml)
[![Auto Format](https://github.com/softkleenex/coding_training/actions/workflows/auto_format.yml/badge.svg)](https://github.com/softkleenex/coding_training/actions/workflows/auto_format.yml)
[![Obsidian](https://img.shields.io/badge/Obsidian-483699?style=flat&logo=obsidian&logoColor=white)](https://obsidian.md/)
[![Quartz](https://img.shields.io/badge/Quartz-v4-blue?style=flat)](https://quartz.jzhao.xyz/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)

**알고리즘 문제 풀이 아카이브 및 개인 기술 블로그 (Obsidian + Quartz)**

[🌐 블로그 바로가기](https://softkleenex.github.io/coding_training/)

</div>

---

## 📝 소개

이 저장소는 백준(Baekjoon), AtCoder 등 알고리즘 플랫폼에서 해결한 문제들의 소스 코드와 저만의 풀이(해설)를 기록하는 공간입니다. 동시에 작성된 마크다운(`.md`) 파일들은 **GitHub Pages**를 통해 정적 블로그 웹사이트로 자동 배포됩니다.

## ⚙️ 자동화 파이프라인 (Workflow)

본 블로그는 개발자의 개입을 최소화하기 위해 완전 자동화된 파이프라인으로 운영됩니다.

1. **Solve & Auto-Push:** [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub) 익스텐션을 통해 플랫폼에서 문제를 해결하면 자동으로 저장소에 소스 코드가 커밋됩니다.
2. **Auto-Formatting:** 새로운 코드가 푸시되면 GitHub Action 봇이 파이썬 스크립트(`scripts/format_problems.py`)를 실행하여, 소스 코드를 읽어오고 SEO 및 블로그 렌더링에 최적화된 마크다운 템플릿을 자동으로 생성/병합합니다.
3. **Review & Write:** 로컬 PC 또는 모바일 기기에서 **옵시디언(Obsidian)** 을 통해 동기화된 파일을 열고, `💡 해결 방법` 섹션에 본인만의 풀이 로직과 회고를 기록합니다.
4. **Deploy:** 작성된 글을 `git push`하면, Quartz 엔진이 마크다운 파일들을 연결망(Graph) 구조를 가진 아름다운 HTML 웹사이트로 빌드하여 배포합니다.

## 📂 디렉토리 구조

```text
.
├── content/
│   ├── 백준/         # 백준(BOJ) 문제 풀이 (Bronze, Silver, Gold 등 난이도별 분류)
│   ├── atcoder/      # AtCoder 문제 풀이 모음
│   ├── posts/        # 알고리즘 외 자유로운 개발/기술 포스트 작성 공간
│   └── index.md      # 블로그 메인 대문(Landing Page) 파일
├── scripts/          # 문제 포맷팅 및 파이프라인 자동화용 Python 스크립트
├── quartz/           # 블로그 렌더링 엔진 (Quartz 4) 코어 소스
└── quartz.config.ts  # 블로그 환경 설정 (이름, 테마, SEO 설정)
```

## 💻 Tech Stack

*   **Note-taking:** Obsidian
*   **Static Site Generator (SSG):** Quartz 4 (Node.js / React)
*   **Automation:** GitHub Actions, Python 3
*   **Hosting:** GitHub Pages
