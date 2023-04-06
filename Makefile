export PYTHONPATH := $(shell pwd)/src

.PHONY: clips

clips:
	rm -rf clips
	python3 src/clip_maker/main.py
