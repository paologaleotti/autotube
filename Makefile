export PYTHONPATH := $(shell pwd)/src

.PHONY: clips video all

clips:
	rm -rf clips
	python3 src/clip_maker/main.py

video:
	python3 src/clip_combiner/main.py

all: clips video