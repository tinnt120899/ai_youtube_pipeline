#!/bin/bash
# ----------------------------
# 🚀 Auto Git Add - Commit - Push
# ----------------------------

# Dừng nếu có lỗi
set -e

# Màu sắc hiển thị
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Hỏi nội dung commit
echo "📦 Nhập nội dung commit:"
read COMMIT_MSG

# Thêm toàn bộ thay đổi
git add .

# Commit
git commit -m "$COMMIT_MSG"

# Đảm bảo đang ở branch main
git branch -M main

# Push lên GitHub
git push -u origin main

# Hiển thị kết quả
echo -e "${GREEN}✅ Đã đẩy code lên GitHub thành công!${NC}"
