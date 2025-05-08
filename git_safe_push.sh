#!/bin/bash

echo "✅ Starting safe Git push for VGT-Core..."

# تحقق من تهيئة git
if [ ! -d .git ]; then
  echo "❌ Error: Not a git repository."
  exit 1
fi

echo "🔄 Pulling latest changes from remote main (with rebase)..."
git pull origin main --rebase

echo "📦 Adding and committing changes..."
git add .
git commit -m "Synced local VGT-Core package with remote"

echo "🚀 Pushing to origin/main..."
git push -u origin main

echo "✅ Push completed successfully!"
