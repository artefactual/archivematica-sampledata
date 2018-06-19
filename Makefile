.DEFAULT_GOAL := simple

simple:
	./createtransfers/createtransfers.py create-variously-encoded-files
	./createtransfers/createtransfers.py create-deep-transfers

all: simple
	./createtransfers/createtransfers.py create-large-test-transfers

