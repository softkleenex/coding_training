---
title: "DACON MAI GLM 회고: 큰 유전체 모델보다 맞는 objective가 중요했다"
description: "2nd MAI Competition에서 Nucleotide Transformer, ESM-2, HyenaDNA, PCA, contrastive learning을 비교하며 variant-sensitive genomic embeddings를 만든 기록입니다."
tags:
  - Competition
  - DACON
  - Genomics
  - BioAI
  - Embedding
  - Retrospective
status: "Published"
---

# DACON MAI GLM 회고: 큰 유전체 모델보다 맞는 objective가 중요했다

이 프로젝트는 DACON `2nd MAI Competition: Improving Variant Sensitivity in Genomic Language Models` 기록이다. 목표는 DNA sequence를 고정 차원 embedding으로 바꾸되, reference sequence와 variant sequence의 차이가 잘 드러나도록 만드는 것이었다.

기록에는 두 점수가 함께 남아 있다. README의 final table 기준 private 기록은 `0.54554`, 순위는 `815`팀 중 `91`위(top 11.1%)였다. 별도로 best experiment/submission으로는 contrastive learning 기반 `0.54805`가 정리되어 있다. 이 글에서는 둘을 섞지 않고, 최종 leaderboard 기록과 실험상 최고 방법을 나눠서 본다.

## 한눈에 보기

| 항목       | 내용                                                                                                                                             |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Platform   | `DACON`                                                                                                                                          |
| Local repo | `dacon-mai-glm-2025`                                                                                                                             |
| GitHub     | [dacon-mai-glm-2025](https://github.com/softkleenex/dacon-mai-glm-2025)                                                                          |
| Blog URL   | [https://softkleenex.github.io/coding_training/dacon/dacon-mai-glm-2025](https://softkleenex.github.io/coding_training/dacon/dacon-mai-glm-2025) |
| Category   | [DACON 대회 아카이브](./)                                                                                                                        |

## 어떤 문제였나

입력은 1,024bp DNA sequence `13,711`개였다. 대회가 요구한 것은 sequence별 embedding이고, embedding 차원은 `768` 이하로 제한됐다. 평가는 reference-variant pair 사이의 cosine distance, pathogenic/benign variant 구분력, variant count와 distance의 correlation을 함께 보는 방식이었다.

즉 일반적인 classification 대회가 아니었다. label을 맞히는 문제라기보다, embedding space 자체가 variant-sensitive해야 했다. 이 차이를 늦게 인정할수록 실험은 돌아갔다.

## 실험 흐름

초기에는 여러 genomic/protein language model에서 embedding을 뽑고 pooling과 dimensionality reduction을 바꾸는 식으로 접근했다.

| 방법                        | 점수      | 메모                                   |
| --------------------------- | --------- | -------------------------------------- |
| ESM-2 L33 + PCA 768D        | `0.5432`  | protein model baseline                 |
| NT 500m-human-ref + PCA     | `0.5445`  | standard extraction best baseline      |
| NT 500m-human-ref raw 1280D | `0.4955`  | PCA 없는 raw embedding은 크게 실패     |
| NT 2.5B multi-species       | `0.5420`  | 큰 모델이 더 좋지는 않았다             |
| HyenaDNA character-level    | `0.4977`  | 긴 context 장점이 점수로 이어지지 않음 |
| Contrastive + ClinVar       | `0.54805` | best experiment/submission             |

가장 의외였던 건 PCA였다. 차원 축소는 단순히 파일 크기를 줄이기 위한 후처리가 아니라, variant detection을 방해하는 noise dimension을 제거하는 핵심 단계였다. raw 1280D는 `0.4955`였지만 PCA 768D는 `0.5445`까지 올랐다. 심지어 PCA 256D와 768D가 같은 점수를 냈기 때문에, 필요한 신호는 생각보다 낮은 차원에 압축되어 있었다.

## 실패한 가정

처음에는 더 큰 모델, 더 복잡한 pooling, 더 많은 layer 조합이 이길 것이라고 기대했다. 실제 결과는 반대에 가까웠다.

1. `NT 2.5B`는 `NT 500m-human-ref`보다 낮았다. 모델 크기보다 human genome domain alignment가 더 중요했다.
2. center pooling은 variant가 sequence 중앙에 있을 것이라는 가정을 깔고 있었지만, 실제로는 mean pooling이 더 안정적이었다.
3. layer concatenation과 weighted layers는 baseline을 확실히 넘지 못했다.
4. splice/promoter classification fine-tuning은 loss가 random baseline 근처에서 멈췄다.

가장 큰 깨달음은 classification fine-tuning과 similarity-based variant detection이 다른 문제라는 점이었다. promoter를 잘 분류하는 representation이 reference-variant distance를 잘 벌려준다는 보장은 없다.

## 왜 contrastive가 맞았나

후반부에는 ClinVar에서 pathogenic/benign variant pair를 모으고, reference와 variant embedding 사이의 거리를 직접 학습하는 contrastive 방향으로 바꿨다. backbone은 `Nucleotide Transformer 500m-human-ref`를 사용하고, backbone을 얼린 뒤 projection head를 학습하는 식이었다.

핵심은 objective였다.

- pathogenic variant pair는 더 강하게 분리한다.
- benign pair도 reference와 variant 차이를 반영하되, 가중치를 다르게 둔다.
- classification label을 맞히는 대신 embedding distance 자체를 조정한다.

이 접근은 "대회 metric이 무엇을 원하는가"에 더 직접적으로 맞았다. 그래서 architectural tweak보다 작은 projection head와 contrastive loss가 더 설득력 있는 방향이 됐다.

## 포트폴리오에 남길 교훈

이 대회는 BioAI라는 단어보다, representation learning 문제를 어떻게 읽을 것인가가 더 중요했다.

1. metric이 embedding space를 평가하면 objective도 embedding space를 직접 겨냥해야 한다.
2. PCA는 단순 압축이 아니라 noise reduction일 수 있다.
3. 모델 크기보다 pretraining corpus와 task alignment가 중요하다.
4. fine-tuning은 "무엇을 학습시키는가"가 틀리면 compute만 태운다.
5. bio domain에서는 실패한 모델도 왜 실패했는지 문서화해야 다음 실험이 짧아진다.

이 프로젝트가 마음에 남는 이유는 점수보다 방향 전환 때문이다. 처음에는 모델을 바꾸고 layer를 섞으며 답을 찾으려 했다. 하지만 결국 문제는 "더 많은 표현"이 아니라 "평가지표가 보는 거리"였다. 그걸 인정하고 contrastive learning으로 옮겨간 순간, 실험의 언어가 조금 더 정확해졌다.

## 기록 포인트

- 핵심 발견은 repo의 `docs/FINDINGS.md`에 정리되어 있습니다.
- 전체 실험 흐름은 `README.md`, `docs/FINAL_REPORT.txt`, `archive/experiments.md`에서 이어서 볼 수 있습니다.
- 이 페이지는 유전체 모델 크기 경쟁보다 PCA noise reduction, objective mismatch, contrastive learning 교훈을 중심으로 정리합니다.

## 연결

- 카테고리: [[index|DACON 대회 아카이브]]
- GitHub repo: [dacon-mai-glm-2025](https://github.com/softkleenex/dacon-mai-glm-2025)
- 감사 노트: [Softkleenex Archive 대회 기록 감사](../posts/competition-archive-audit-2026-06-26)
- 이 페이지: [https://softkleenex.github.io/coding_training/dacon/dacon-mai-glm-2025](https://softkleenex.github.io/coding_training/dacon/dacon-mai-glm-2025)
