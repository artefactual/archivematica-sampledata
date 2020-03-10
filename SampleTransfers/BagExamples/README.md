# Bag transfer type examples

This sample data enables the testing of Bags within Archivematica. Bags are
separated into the different types of Bag that transfers can be created from in
Archivematica.

A handful of use-cases are described below.

## Bags with processing configurations

E.g. `SimpleBagWithProcessingMCP/`, `SimpleBagWithProcessingMCP.zip`,
`SimpleBagWithProcessingMCP.tar.gz`.

Each bag has a processing configuration. The processing configuration has
every decision point set to None. This is designed so that no matter what
points a user has automated for testing, they will always be overwritten with
this transfer asking them to resolve all decisions in order to complete an AIP.

## Bags with Dublin Core metadata

E.g. `BaggedDemoTransferCSV/`, `BaggedDemoTransferCSV.tar.gz`,
`BaggedDemoTransferCSV.zip`.

Each bag has a CSV metadata file that contains Dublin Core metadata formatted
to match a bag specification. Metadata and files contain a limited number of
diacritics to also ensure compatibility across locales.

## Simple bags

E.g. `UnzippedBag/`, `TarredBag.tar.gz`, `ZippedBag.zip`.

Original bags from the Archivematica sample data. A feature of these is their
`bag-info.txt` which is translated to AIP METS sourceMD field. The bags
described in the other examples above also have some `bag-info.txt` which can be
consulted during testing.
