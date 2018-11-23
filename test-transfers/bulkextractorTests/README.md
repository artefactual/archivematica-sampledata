## artefactual/sample-data/TestTransfers/bulkextractorTests

Files that can generate matches using the full 
[Bulk Extractor](http://www.forensicswiki.org/wiki/Bulk_extractor) suite. 

### Archivematica User Interface

The Appraisal tab of Archivematica can be used to view Bulk Extractor output 
for content that contains: 

* Credit Card Numbers (CCN)
* Social Security Numbers (SSN/PII (Personally Identifiable Information))

Social Security Numbers must be prefixed with 'SSN:' (optionally followed by a 
space character) to be identified.

### Archival Information Package (AIP)

The AIP produced by Archivematica will also contain the complete output of the
Bulk Extractor tool, helping users to identify information such as:

* Telephone Numbers
* Email Addresses
* Internet Domain Names

The files in this location that are not related to CCNs or SSNs can be used 
against Archivematica or Bulk Extractor to more thoroughly test the system's 
capabilities.