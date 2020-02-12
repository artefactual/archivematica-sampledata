# Zipped directory sample transfers

A small collection of zipped directory sample transfers. Zipped directory
transfers were introduced in Archivematica 1.11 as part of a piece of work
submitted by Wellcome Trust.

## DemoTransferCSV.zip

Part of Archivematica's standard corpus of tests. DemoTransferCSV contains
features such as checksum manifests for checking the integrity of the transfer
and Dublin Core metadata for adding descriptive metadata to the AIP METS.

## Images.tar.gz

Part of Archivematica's standard corpus of tests. Images contains a selection
of image formats for testing various format-policy-register outputs.

## ZippedDirectoryTransferWithProcessing.zip

Zipped Directory Transfer with Processing is a sample transfer containing one
image alongside a LICENSE, README, and custom processing configuration file.
The processing configuration has every decision point set to `None`. This is
designed so that no matter what points a user has automated for testing, they
will always be overwritten with this transfer asking them to resolve all
decisions in order to complete an AIP.
