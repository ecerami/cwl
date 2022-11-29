# cwl

This directory contains a toy CWL Pipeline.

The pipeline runs two steps:

* Extract a single JSON element from a JSON file.
* Convert the JSON element text to upper case.

## Installation

To get set-up, follow these instructions:

	python3 -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt

## Validation

You can validate all the CWL pipelines by running:

	make validate

## Python Docker Image

The python folder contains two very simple Python command line tools.

I have created a Docker image for these tools and pushed them to:

https://hub.docker.com/repository/docker/ecerami/extract

## Pipelines

The pipeline is built from the bottom up:

* extract_tool.json:  runs the extract step via Docker.
* upper_tool.json:  runs the upper case step via Docker.

You can run these like so:

	make extract_tool
	make upper_tool

You can then run the workflow like so:

	make workflow

Lastly, you can run the subdir CWL required for scatter like so:

	make subdirs

Finally, you can run the whole thing on multiple files:

	make scatter

## Packing

You can pack the CWL into one file by running:

	make pack

