## artefactual/sample-data/TestTransfers/virusTests 

Files with viruses that can trigger a positive match in ClamAV. 

### Checksums

In case a filesystem were to modify the files e.g. remove the definition from
the file, then compare what is received with checksum.md5. 

### Sample Output

     cmd: clamscan --max-filesize 32M *

     test.1M.eicar.with-virus: Eicar-Test-Signature FOUND
     test.1M.nukem.with-virus: Win.Trojan.Nukem-1 FOUND
     test.1M.null.no-virus: OK
     test.30M.eicar.with-virus: Eicar-Test-Signature FOUND
     test.30M.nukem.with-virus: Win.Trojan.Nukem-1 FOUND
     test.30M.null.no-virus: OK
     test.zip.eicar.with-virus.zip: Eicar-Test-Signature FOUND

