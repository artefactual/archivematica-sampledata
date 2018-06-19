# Artefactual sample data

Once you've cloned this repo you can install the OPF format corpus by
entering the following command:

    git submodule update --init


## Build

This repository contains a Python executable named `createtransfers.py` which
can be used to create test transfers (see [#13][0] for more details). Try
running it with the following command:

    $ ./createtransfers/createtransfers.py --help

The number of arguments of this command is increasing. We provide a couple of
shortcuts meant to be used by other tools while maintaining a simple interface:

```shell
# Build simpler test transfers - it should build fast.
$ make simple

# Build all test transfers - it may take a while and use a lot of space.
$ make all
```


[0]: https://github.com/artefactual/archivematica-sampledata/pull/13
