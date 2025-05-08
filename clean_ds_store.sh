#!/bin/bash

echo "🧹 Removing all .DS_Store files from project recursively..."
find . -name .DS_Store -print -delete

echo "🛑 Ensuring .DS_Store is in .gitignore..."
if ! grep -qx ".DS_Store" .gitignore; then
  echo ".DS_Store" >> .gitignore
  echo "✅ Added .DS_Store to .gitignore"
else
  echo "✅ Already ignored"
fi

echo "🧼 Removing .DS_Store from Git index..."
git rm -r --cached .DS_Store 2>/dev/null

echo "✅ Committing changes..."
git add .gitignore
git commit -m "Remove .DS_Store and add to .gitignore" || echo "No changes to commit."

echo "🚀 Push your changes with: git push"
