# Makefile for VGT-Core Development

.PHONY: clean_ds clean_dev test build publish

# تنظيف .DS_Store
clean_ds:
	bash tools/maintenance/clean_ds_store.sh

# تنظيف __pycache__ و .ipynb_checkpoints
clean_dev:
	bash tools/maintenance/clean_dev_artifacts.sh

# اختبار النموذج
test:
	python vgt_core/tests/test_vgt_core.py

# بناء الحزمة
build:
	python setup.py sdist bdist_wheel

# نشر الحزمة (يتطلب PYPI_TOKEN في environment)
publish:
	twine upload dist/*
