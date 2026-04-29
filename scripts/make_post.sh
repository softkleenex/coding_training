#!/bin/bash
# 로컬에서 마크다운 포스트를 수동으로 자동 생성하는 스크립트

# 스크립트가 실행되는 위치와 상관없이 항상 프로젝트 최상위 폴더로 이동하여 실행
cd "$(git rev-parse --show-toplevel)" || exit 1

echo "🚀 로컬 마크다운 포스트 생성 시작..."
python3 scripts/format_problems.py
python3 scripts/update_readme.py
echo "✨ 완료! 옵시디언에서 마크다운 파일들을 확인해 보세요."
