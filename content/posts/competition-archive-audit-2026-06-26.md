---
title: "Softkleenex Archive 대회 기록 감사: 얕은 링크 모음에서 포트폴리오 회고로"
description: "Softkleenex Archive의 DACON, Kaggle 대회 기록을 점검하고, repo README와 블로그 회고 사이의 다음 개선 작업을 정리한 감사 노트입니다."
tags:
  - AI
  - DACON
  - Kaggle
  - Portfolio
  - Retrospective
status: "Published"
---

# Softkleenex Archive 대회 기록 감사: 얕은 링크 모음에서 포트폴리오 회고로

`Softkleenex Archive`를 개발 블로그이자 AI competition 포트폴리오로 쓰려면, 대회 페이지가 단순 링크 모음에서 끝나면 안 된다. 코드는 GitHub repo에 있어도 되지만, 블로그에는 사람이 읽고 이해할 수 있는 이야기가 있어야 한다.

그래서 2026년 6월 26일 기준으로 DACON, Kaggle 대회 아카이브를 한 번 훑었다. 목적은 간단하다.

- 어떤 페이지가 이미 회고로 읽히는가
- 어떤 페이지가 아직 1차 링크 노트에 머물러 있는가
- GitHub repo와 블로그가 서로 이어져 있는가
- 다음에 어떤 주제부터 깊게 고쳐야 하는가

## 현재 구조

블로그는 루트 사이트와 Quartz 블로그가 분리되어 있다.

| 영역   | URL                                                               | 역할                         |
| ------ | ----------------------------------------------------------------- | ---------------------------- |
| 루트   | [softkleenex.github.io](https://softkleenex.github.io/)           | 브랜드/포트폴리오 입구       |
| 블로그 | [coding_training](https://softkleenex.github.io/coding_training/) | 글, 대회 기록, 알고리즘 기록 |
| DACON  | [DACON 대회 아카이브](../dacon/)                                  | DACON repo와 회고 연결       |
| Kaggle | [Kaggle 대회 아카이브](../kaggle/)                                | Kaggle repo와 회고 연결      |

대회 repo 자체는 블로그 repo 안으로 복사하지 않는다. 각 repo는 그대로 두고, 블로그는 읽기 좋은 회고와 탐색 지도로 유지한다. 이 구조는 맞다. 문제는 깊이다.

## 발견한 것

### 1. 대회 페이지 대부분은 아직 얕다

현재 대회별 Markdown 페이지는 DACON 9개, Kaggle/공모전 9개가 있다. 이 중 `DACON ETRI Human Understanding` 회고만 100줄 이상으로 실제 회고에 가깝고, 나머지 대회 페이지 대부분은 34줄짜리 허브 노트다.

허브 노트가 나쁜 것은 아니다. 하지만 포트폴리오로 읽히려면 최소한 다음 항목이 있어야 한다.

- 어떤 문제였는지
- 어떤 접근을 했는지
- 어디서 막혔는지
- 무엇을 고쳤거나 우회했는지
- 결과가 어땠는지
- 다음에 반복하지 않을 교훈이 무엇인지

지금은 이 내용이 블로그보다 각 repo README에 더 많이 남아 있다. 다음 작업은 README의 깊이를 블로그 회고로 옮기는 것이다.

### 2. README 역링크는 꽤 잘 되어 있다

로컬에서 확인한 DACON/Kaggle git repo 17개는 모두 README 안에 블로그 링크를 가지고 있었다. 이건 좋은 상태다.

다만 두 repo는 GitHub origin remote가 없었다.

| repo               | 상태               | 처리 방향                                       |
| ------------------ | ------------------ | ----------------------------------------------- |
| `dacon-webgamming` | origin remote 없음 | 블로그에서는 로컬/미공개 프로젝트로 명시        |
| `kaggle-dpc-tate`  | origin remote 없음 | 공개 repo를 만들지 않을 거면 미공개 상태로 명시 |

그리고 `HLFTC`는 git repo가 아니라 로컬 폴더로 보인다. 제출 자료와 참고 자료가 많지만, 블로그에서는 “공모전/기획 프로젝트”로 따로 다루는 편이 맞다.

### 3. 구조 오류도 있었다

대회별 “한눈에 보기” 표에서 Category 행이 깨져 있었다. 예를 들어 `[[index | DACON 대회 아카이브]]`가 Markdown table의 열 구분자로 오해되는 형태였다.

이건 감사 중 바로 수정했다. 링크 자체는 작은 문제처럼 보이지만, 포트폴리오 문서에서는 이런 깨진 표가 신뢰를 빨리 깎는다.

### 4. 일부 repo는 dirty 상태다

몇몇 대회 repo에는 아직 커밋되지 않은 변경이 있다. 이 감사에서는 대회 repo를 수정하지 않았다. 사용자가 만든 변경과 섞지 않기 위해서다.

README 상호 링크 보강이나 repo 문서 정리는 별도 주제로 잡고, 각 repo의 dirty 상태를 먼저 확인한 뒤 들어가는 것이 안전하다.

## 다음 작업 우선순위

### 1순위: DACON ETRI 회고 고도화

이미 가장 깊은 글이지만, 최근 대회라 포트폴리오 가치가 가장 높다. 다음을 보강하면 좋다.

- 대회 데이터와 타깃 구조를 더 명확히 설명
- ID342, ID346, ID350, ID347 제출 흐름을 표로 정리
- ASOS, AirKorea, 생활기상지수 API 실험이 왜 기대만큼 작동하지 않았는지 정리
- “점수는 아쉬웠지만 운영 기록은 남았다”는 결론을 더 선명하게 다듬기

### 2순위: README가 이미 깊은 대회부터 블로그화

repo README에 이미 회고 재료가 많은 프로젝트부터 옮기면 효율이 좋다.

| 우선순위 | 후보                                    | 이유                                          |
| -------- | --------------------------------------- | --------------------------------------------- |
| 1        | `kaggle-hull-tactical-prediction`       | 실패 분석과 regime shift 회고가 강함          |
| 2        | `kaggle-medgemma-clinical-rag-pipeline` | 인증/멀티모달/RAG 병목이 포트폴리오에 좋음    |
| 3        | `dacon-mosquito-trajectory-prediction`  | 문제 해결 기법과 스코어 빌드업이 선명함       |
| 4        | `dacon-k-league-pass-prediction`        | simplicity, pseudo-labeling, 실패 분석이 있음 |
| 5        | `kaggle-jigsaw-acrc-portfolio`          | 디버깅 사례로 읽히기 좋음                     |

### 3순위: 미공개/비정형 프로젝트 상태 정리

`dacon-webgamming`, `kaggle-dpc-tate`, `HLFTC`는 공개 repo 링크가 없거나 git repo 구조가 다르다. 무리하게 GitHub 링크를 채우기보다, 현재 공개 가능 여부를 명확히 적는 편이 낫다.

## 완료 기준

이 감사 주제의 완료 기준은 다음과 같다.

- 대회 아카이브의 현재 상태를 블로그 글로 남긴다.
- 깨진 Category 표를 고친다.
- 다음 deep-dive 작업 순서를 정한다.
- Quartz build, sitemap/RSS, 민감정보 스캔, live URL 검증을 통과한다.

다음 주제는 `DACON ETRI Human Understanding` 회고 고도화로 들어가는 것이 가장 자연스럽다. 최근 작업이고, 이미 기록이 많고, 이 블로그가 어떤 포트폴리오 톤을 가질지 기준점으로 삼기 좋다.
