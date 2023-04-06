export PYTHONPATH := $(shell pwd)/src

.PHONY: clips

clips:
	rm -rf clips
	python3 src/clip_maker/main.py
video:
	python3 src/clip_combiner/main.py
