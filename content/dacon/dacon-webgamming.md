---
title: "Dacon Web Minigame Hackathon"
description: "DACON 월간 웹 미니게임 해커톤에서 만든 Just One Click 회고입니다. 원 버튼 패링 액션, Canvas 2D, Web Audio, 빠른 재도전 루프와 해커톤 스코프 관리 기록을 정리합니다."
tags:
  - Competition
  - DACON
  - Game
  - TypeScript
  - Canvas
status: "Published"
---

# Dacon Web Minigame Hackathon

DACON 월간 해커톤 웹 미니게임 챌린지 참가 기록이다. 주제는 “10분 안에 중독시켜라”였고, 여기서 만든 게임 컨셉은 `Just One Click`, 원 버튼 보스 킬러였다. 복잡한 조작, 성장 시스템, 맵 이동을 버리고 클릭 또는 스페이스바 하나로 패링, 반격, 재도전을 모두 처리하는 초고속 아케이드 게임을 목표로 했다.

ML 대회와는 완전히 다른 종류의 작업이었다. 점수식이나 CV가 아니라, 사용자가 첫 3초 안에 규칙을 이해하고 다시 플레이하고 싶어지는지가 중요했다. 그래서 기획의 중심을 “새로운 시스템을 많이 넣기”가 아니라 “하나의 core loop를 손맛 있게 만들기”에 두었다.

## 한눈에 보기

| 항목       | 내용                                                                                                                                         |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Platform   | `DACON`                                                                                                                                      |
| Local repo | `dacon-webgamming`                                                                                                                           |
| GitHub     | origin remote 또는 Git repo가 아직 설정되어 있지 않습니다.                                                                                   |
| Blog URL   | [https://softkleenex.github.io/coding_training/dacon/dacon-webgamming](https://softkleenex.github.io/coding_training/dacon/dacon-webgamming) |
| Category   | [DACON 대회 아카이브](./)                                                                                                                    |
| Game       | `Just One Click`                                                                                                                             |
| Stack      | Vite, Vanilla TypeScript, Canvas 2D, Web Audio API                                                                                           |
| Core Loop  | 투사체를 타이밍에 맞춰 패링하고 보스에게 반사                                                                                                |

## 기획 판단

해커톤 문서에서 가장 강하게 잡은 원칙은 스코프 최소화였다. 미니게임은 아이디어가 커지기 쉽다. 스킬트리, 여러 보스, 스테이지, 아이템, 랭킹 시스템을 넣기 시작하면 짧은 기간 안에 완성도와 안정성을 같이 잃을 수 있다. 그래서 단일 화면, 단일 보스, 단일 입력으로 줄였다.

대신 남은 시간을 피드백에 몰았다. 패링 성공 시 파티클, 화면 흔들림, hit stop, floating text, 콤보 증가, 보스 체력 감소가 동시에 터지게 했다. 실패 시에는 하트가 줄고 콤보가 초기화되며 바로 재시작할 수 있게 했다. 게임의 깊이는 방대한 컨텐츠가 아니라, 짧은 루프가 얼마나 즉각적으로 반응하는지에서 나오도록 설계했다.

## 구현

구현은 Vite와 Vanilla TypeScript, HTML5 Canvas 2D API로 했다. 별도 게임 엔진을 쓰지 않고 직접 game loop, projectile update, collision, boss phase, particle, floating text를 구성했다. 오디오는 Web Audio API로 합성해서 외부 사운드 에셋 의존도를 줄였다.

보스는 체력에 따라 phase가 바뀐다. phase 1은 기본 단발 투사체, phase 2는 빠른 확산탄과 laser charge, phase 3은 더 빠른 곡선 투사체와 강한 압박을 사용한다. 플레이어는 마우스 위치 또는 터치 위치를 따라 좌우로 움직이고, 클릭/스페이스 입력으로 짧은 parry window를 연다. 이 타이밍에 투사체나 laser가 닿으면 반사되어 보스에게 damage가 들어간다.

시각적 스타일은 네온 아케이드 쪽으로 잡았다. 화면 전체 grid, 보스 glow, laser warning, CRT 느낌의 UI, 파티클 폭발 같은 요소는 모두 “규칙 설명 없이도 지금 무슨 일이 벌어졌는지 보이게 하자”는 목적이었다.

## 회고

가장 잘한 판단은 아이디어를 끝까지 줄인 것이다. 기획 문서에는 여러 후보가 있었지만, 최종적으로 원 버튼 패링 액션을 선택하면서 구현 경로가 선명해졌다. 덕분에 조작, 충돌, 보스 패턴, 사운드, 연출이 같은 방향으로 쌓였다.

아쉬운 점은 배포와 공개 저장소 정리가 대회 산출물만큼 깔끔하지 않았다는 점이다. 현재 로컬 레포는 존재하지만 GitHub origin remote가 연결되어 있지 않고, 블로그에서는 코드 링크 대신 작업 기록만 연결하고 있다. 포트폴리오로 쓰려면 playable demo, GitHub repo, 짧은 gameplay capture까지 붙여야 완성도가 훨씬 좋아질 것이다.

이 작업은 이후 경쟁형 ML 대회에도 은근히 도움이 됐다. 해커톤에서는 “작게 만들고, 빨리 확인하고, 사용자가 느끼는 핵심 피드백에 집중한다”는 감각이 중요하다. ML에서도 feature를 무작정 늘리기보다, 점수를 움직이는 가장 짧은 loop를 찾아야 한다는 점에서 꽤 닮아 있었다.

## 연결

- 카테고리: [[index|DACON 대회 아카이브]]
- GitHub repo: 아직 공개 origin remote가 없습니다.
- 전체 아카이브 점검: [[../posts/competition-archive-audit-2026-06-26|Competition archive audit]]
- 이 페이지: [https://softkleenex.github.io/coding_training/dacon/dacon-webgamming](https://softkleenex.github.io/coding_training/dacon/dacon-webgamming)
