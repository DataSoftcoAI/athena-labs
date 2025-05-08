#!/bin/bash

echo "🚀 Uploading Mini SDK to GitHub Release..."

# تحقق من تثبيت gh CLI
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) is not installed. Please install it first: https://cli.github.com/"
    exit 1
fi

# إعداد المتغيرات
REPO="DataSoftcoAI/athena-labs"
TAG="v0.3.0"
TITLE="VGT-Core v0.3 – Stable Release"
BODY="Includes the full library + Mini SDK for rapid experimentation."

# تحقق مما إذا كان الإصدار موجودًا
if gh release view $TAG --repo $REPO &>/dev/null; then
    echo "📦 Release $TAG already exists. Uploading asset..."
else
    echo "🆕 Creating release $TAG..."
    gh release create $TAG /mnt/data/vgt_core_mini_sdk.zip \
        --repo $REPO \
        --title "$TITLE" \
        --notes "$BODY"
    exit 0
fi

# رفع ملف Mini SDK
gh release upload $TAG /mnt/data/vgt_core_mini_sdk.zip --repo $REPO --clobber

echo "✅ Mini SDK uploaded to release $TAG successfully."
