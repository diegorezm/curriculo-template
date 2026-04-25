OUTPUT_DIR := output
SOURCES    := $(filter-out README.md, $(wildcard *.md))
GDRIVE_DIRECTORY := curriculos/
PDFS       := $(SOURCES:%.md=$(OUTPUT_DIR)/%.pdf)

.PHONY: all clean sync

all: $(OUTPUT_DIR) $(PDFS)

$(OUTPUT_DIR):
	mkdir -p $(OUTPUT_DIR)

$(OUTPUT_DIR)/%.pdf: %.md style.css config.json
	python build.py $< $@

clean:
	rm -rf $(OUTPUT_DIR)

sync: all
	rclone sync output/ gdrive:$(GDRIVE_DIRECTORY) -v
