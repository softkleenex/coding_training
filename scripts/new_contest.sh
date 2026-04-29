#!/bin/bash
# scripts/new_contest.sh
# atcoder-cli(acc)와 마크다운 다운로드 파이썬 스크립트를 한 번에 실행하는 래퍼 스크립트입니다.

if [ -z "$1" ]; then
    echo "사용법: ./scripts/new_contest.sh <콘테스트ID>"
    echo "예시: ./scripts/new_contest.sh abc455"
    exit 1
fi

CONTEST_ID=$(echo "$1" | tr '[:upper:]' '[:lower:]')

echo "============================================="
echo " 1. [acc] 폴더 및 테스트 케이스(예제) 다운로드 중..."
echo "============================================="
# content/atcoder 폴더로 이동해서 생성
mkdir -p content/atcoder
cd content/atcoder || exit 1
acc new "$CONTEST_ID" -c all

echo ""
echo "============================================="
echo " 2. [fetch_atcoder] 문제 지문(Markdown) 다운로드 중..."
echo "============================================="
# 부모 폴더(루트)로 돌아와서 스크립트 실행
cd ../..
python3 scripts/fetch_atcoder.py "$CONTEST_ID" --acc-mode

echo ""
echo "✨ 완료되었습니다! content/atcoder/$CONTEST_ID/ 폴더 안을 확인해주세요."
