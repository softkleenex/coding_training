---
title: "DACON ETRI Human Understanding AI Paper Challenge 회고"
tags:
  - DACON
  - Machine-Learning
  - Competition
  - Retrospective
status: "Published"
---

# DACON ETRI Human Understanding AI Paper Challenge 회고

2026년 6월, DACON ETRI Human Understanding AI Paper Challenge를 마무리했다.  
스마트폰과 스마트워치에서 수집된 라이프로그로 수면, 피로, 스트레스, 수면 지표를 예측하는 문제였다.

이번 대회에서 가장 오래 남은 감각은 모델보다도 검증과 기록의 중요성이었다. 로컬 CV는 좋아지는데 public leaderboard가 거의 움직이지 않거나 오히려 나빠지는 일이 반복됐다. 그래서 마지막에는 "점수를 조금이라도 더 낮추는 것"만큼이나 "무엇을 왜 제출했고, 왜 실패했는지 복구 가능한 상태로 남기는 것"이 중요했다.

## 최종 anchor

최종적으로 public 기준 가장 좋았던 제출은 `ID342`였다.

|  id | 설명                                              | local CV |    public LB |
| --: | ------------------------------------------------- | -------: | -----------: |
| 342 | ID178/ID221 feature-similarity shrink, alpha 0.50 | 0.534000 | 0.5960832519 |

ID342는 큰 모델 하나가 모든 것을 해결한 결과라기보다, 기존 예측 두 계열의 feature-similarity 기반 신호를 보수적으로 줄여 섞은 후보였다. 이후 여러 Q3, S3, S4 중심의 독립 신호를 시도했지만 이 기준점을 넘지는 못했다.

## 마지막 제출

대회 마지막 날에는 Q3 app-name lexicon anti-signal 후보를 만들었다. 로컬 게이트에서는 꽤 좋아 보였다. split 기준으로 일관되게 이기는 후보도 있었고, local proxy도 ID342보다 낮아졌다.

하지만 public leaderboard에서는 전부 실패했다.

|  id | local CV |    public LB | ID342 대비 public 변화 |
| --: | -------: | -----------: | ---------------------: |
| 346 | 0.533659 | 0.5963391483 |          +0.0002558964 |
| 350 | 0.533699 | 0.5963352712 |          +0.0002520193 |
| 347 | 0.533813 | 0.5961947552 |          +0.0001115033 |

셋 중 가장 가까웠던 ID347도 ID342보다 나빴다. 이 결과는 꽤 선명한 CV/LB gap 사례로 남았다. 로컬에서 의미 있어 보이는 target-specific 신호라도 public split에서는 다르게 작동할 수 있었다.

## 효과가 있었던 것

- 제출 파일, notebook-history stub, submission log 한 행을 맞춰 둔 것
- 로컬 점수와 public 점수를 분리해서 기록한 것
- 후보마다 decision note를 남겨 나중에 실패 원인을 복구할 수 있게 한 것
- 큰 이동보다 anchor 주변의 작은 convex movement를 더 엄격히 보는 습관

특히 submission log는 마지막 날에 빛을 봤다. 어떤 파일이 실제 제출됐고, 어떤 파일은 일일 제출 한도로 거절됐고, 어느 public score가 어느 후보에 대응되는지를 빠르게 정리할 수 있었다.

## 실패했던 것

- 로컬 CV 개선을 곧바로 제출 가치로 해석한 것
- Q3/S3/S4의 새 신호가 "도메인상 그럴듯하다"는 이유만으로 transfer 가능성이 높다고 본 것
- public feedback을 설명하는 validation lens를 충분히 빨리 만들지 못한 것

이번 대회에서는 "좋은 로컬 점수"와 "좋은 제출 후보"가 다르다는 말을 계속 확인했다. 로컬에서 ID342를 이긴 후보가 public에서는 ID342보다 나빠지는 일이 많았다.

## 운영 교훈

1. 제출 파일과 실험 로그는 반드시 1:1로 맞춰야 한다.
2. public score는 local score와 별도 컬럼으로 관리해야 한다.
3. 대회 막판에는 새 아이디어보다 검증된 후보군의 위험도를 비교하는 시간이 더 중요하다.
4. 자동 제출 스크립트는 편하지만 credential은 반드시 환경변수로만 다뤄야 한다.
5. Git history에 민감 정보가 들어갔다면 현재 파일만 고치는 것으로는 부족하고, history rewrite와 토큰 폐기가 필요하다.

## 마무리

목표했던 0.55에는 닿지 못했다. 그래도 이 대회는 모델링 이상의 것을 남겼다.  
다음 대회에서는 더 강한 모델을 더 빨리 만드는 것보다, public feedback을 설명할 수 있는 validation lens를 먼저 세우는 데 더 많은 시간을 쓸 것이다.

마지막 점수보다 오래 남는 것은 기록이다. 이번 대회는 그 사실을 꽤 비싸게, 하지만 확실하게 가르쳐줬다.
