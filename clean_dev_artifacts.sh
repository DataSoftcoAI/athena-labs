#!/bin/bash

echo "🧹 Removing all __pycache__ and .ipynb_checkpoints folders..."

# حذف المجلدات فعليًا
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +

# تحديث .gitignore
echo "🔧 Updating .gitignore..."
touch .gitignore
for pattern in "__pycache__/" ".ipynb_checkpoints/"; do
  if ! grep -qx "$pattern" .gitignore; then
    echo "$pattern" >> .gitignore
    echo "✅ Added $pattern to .gitignore"
  else
    echo "✅ $pattern already in .gitignore"
  fi
done

# إزالة التتبع من Git
echo "📦 Cleaning Git cache..."
git rm -r --cached __pycache__/ .ipynb_checkpoints/ 2>/dev/null

# إنشاء Commit للتنظيف
echo "✅ Committing .gitignore update..."
git add .gitignore
git commit -m "Remove dev artifacts and ignore __pycache__ + .ipynb_checkpoints" || echo "No changes to commit."

echo "🚀 Done! Push your changes with: git push"
