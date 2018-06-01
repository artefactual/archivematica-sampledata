.DEFAULT_GOAL := simple

simple:
	./createtransfers/createtransfers.py create-variously-encoded-files
	./createtransfers/createtransfers.py create-deep-transfers
	./createtransfers/createtransfers.py create-variously-encoded-dir-names
	./createtransfers/createtransfers.py create-deep-zip-packages
	./createtransfers/createtransfers.py \
		create-zip-packages-with-var-encoded-fnames
	./createtransfers/createtransfers.py \
		create-zip-packages-with-var-encoded-dirs

all: simple
	./createtransfers/createtransfers.py create-large-test-transfers
	./createtransfers/createtransfers.py create-large-zip-packages
