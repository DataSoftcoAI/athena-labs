#!/bin/bash

echo "🔄 Updating README.md on GitHub..."

# تحقق من وجود git
if [ ! -d .git ]; then
  echo "❌ Error: Not inside a Git repository."
  exit 1
fi

# نسخ README المحدث إلى جذر المشروع
cp /mnt/data/vgt_core_pkg/README.md ./README.md

# تحديث Git
git add README.md
git commit -m "Update README.md with Quick Start SDK section"
git push origin main

echo "✅ README.md updated and pushed successfully!"
