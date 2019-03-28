# Dataverse Sample Data

Sample Dataverse transfers that can be run standalone to test functionality
added in Archivematica 1.8.

All datasets are licensed *CC0* [![CC0-1.0][dataverse-1].

To use these as Archivematica transfers select the Dataverse transfer type
inside Archivematica, and then select the top-level folder (listed in brackets
below) belonging to each one.

[dataverse-1]: https://licensebuttons.net/l/zero/1.0/80x15.png)](http://creativecommons.org/publicdomain/zero/1.0/

## Datasets

### A study of my afternoon drinks (AStudyOfMyAfternoonDrinks)

**Citation:** *Tester, Archivematica, 2018, "A study of my afternoon drinks",
https://doi.org/10.5072/FK2/6PPJ6Y, Root Dataverse, V1,
UNF:6:IgxkjKXUlveGP0Darp1fYg==*

### A study of my afternoon snacks (AStudyOfMyAfternoonSnacks)

Noel Fielding; Mary Berry; Hollywood, Paul, 2019, "A study of my afternoon
snacks", https://doi.org/10.5072/FK2/QAWS8O, Scholars Portal Dataverse, V6,
UNF:6:doAry72PFwD1Edcrhsj/Qw== [fileUNF]

### Replication Data for: Staffing for Effective Digital Preservation 2017: An NDSA Report (NDSAStaffingReport)

**Citation:** *NDSA Staffing Survey Working Group, 2017, "Replication Data for:
Staffing for Effective Digital Preservation 2017: An NDSA Report",
https://doi.org/10.7910/DVN/XBMAXP, Harvard Dataverse, V1,
UNF:6:UDt9tttqQKQvJoy72s+N+g== [fileUNF]*

### X-ray CT Scans of Polyodon spathula (Paddlefish) (TNHC 22770) (XRayScansOfPolyodonSpathula)

**Citation:** *The University of Texas High-Resolution X-ray CT Facility
(UTCT), 2018, "X-ray CT Scans of Polyodon spathula (Paddlefish) (TNHC 22770)",
https://doi.org/10.18738/T8/RGXVUG, Texas Data Repository Dataverse, V1*

**NB.** The file *8bitTIFF.zip* has been modified, as permissable under a CC0
license. The images, were converted from TIFF to JPEG and the resolution
reduced to 65% of the original to comply with GitHub filesize limits. The
aggregate (.zip) checksum `f09bcbfd13e0c94d7fc87a6618fa9ceb` becomes
`558ada30b0e8313b4281cdad8f538541` and this is now reflected in the
`metadata/dataset.json` file for the dataset.

## Notes on testing

The Dataverse sample data repository can only be used to test the way
Archivematica processes Dataverse contents and metadata. The result of
processing the these transfers is an Archivematica AIP.

To test the mechanism by which the Storage Service interacts with Dataverse and
how data is downloaded from it then a Dataverse Transfer Source still needs to
be configured.
