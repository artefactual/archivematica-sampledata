# Artefactual sample data

Once you've cloned this repo you can install the OPF format corpus by
entering the following command:

    git submodule update --init

## Contents

The Archivematica sample data contains four top-level folders. Each of these
folders contains individual transfers that can be used to test all manner of
things.

### acceptance-tests

**Purpose**: packages that Artefactual uses for automated testing, based on step
files in artefactual-labs/archivematica-acceptance-tests.

* BagTransfer is used to test AIP encryption
* fixityCheckShouldFail is used to test the capture output setting feature

### test-transfers



### tools

**Purpose**: a place to put things that aren’t actually transferrable test data,
but instead used to create or manipulate testing data, i.e.
[createtransfers.py](#build-createtransfers.py)

### training-resources

**Purpose**: "realistic" public domain material that Artefactual and others can
use for demonstrations, training, and workshops.

* _arthur-conan-doyle-letters-tpl_ - digitized letters from Arthur Conan Doyle to his publisher (Toronto Public Library public domain material). This transfer contains descriptive and rights metadata about the digital objects and can be used to demonstrate metadata workflows.
* _digitized-book-covers-tpl_ - book covers for The Hound of the Baskervilles and The Memoirs of Sherlock Holmes (Toronto Public Library public domain material). This transfer is very simple and can be used to demonstrate basic transfer workflows.
* _illustrations-of-reichenbach-falls-tpl_ - artists' illustrations of the Reichenbach Falls in Switzerland (Toronto Public Library public domain material). This transfer contains valid checksum files and can be used to demonstrate fixity checking.
* _illustrations-of-reichenbach-falls-tpl-bad-checksums_ - artists' illustrations of the Reichenbach Falls in Switzerland (Toronto Public Library public domain material). This transfer contains invalid checksum files and can be used to demonstrate fixity checking failures.
* _sherlock-holmes-baffled-loc-video_ - a video clip from the _Sherlock Holmes Baffled_ (Library of Congress public domain material). This transfer can be used to demonstrate audiovisual workflows.
* _story-illustrations-tpl-disk-image_ - illustrations from Sherlock Holmes stories, stored as a disk image (Toronto Public Library public domain material). This transfer can be used to demonstrate disk image workflows.
* _the-strand-magazine-tpl_ - digitized covers of The Strand Magazine, which published Sherlock Holmes stories as serials (Toronto Public Library public domain material). This transfer contains access and preservation derivates and can be used to demonstrate manual normalization workflows.

**Citations**:

Materials in the training-resources folder come from the public domain:

* Toronto Public Library's ["Adventures with Sherlock Holmes" album](https://flic.kr/s/aHsjDtzmY1) (Flickr), which contains select digitized images and photographs from Toronto Public Library's [Arthur Conan Doyle collection](https://www.torontopubliclibrary.ca/books-video-music/specialized-collections/literature-genre-doyle.jsp)
* [Sherlock Holmes Baffled](https://commons.wikimedia.org/w/index.php?title=File%3ASherlock_Holmes_Baffled.ogv) (Wikimedia Commons), originally from the Library of Congress

## Build createtransfers.py

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
