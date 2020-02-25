# Upload DIP to ArchivesSpace using a matching CSV

This transfer uses an ArchivesSpace ID CSV file (`archivesspaceids.csv`) to
match objects in a transfer with a resource in ArchivesSpace.

This transfer consists of one CSV file, three images, and one markdown file:

```
metadata/archivesspaceids.csv
hooded-pitcher-plant.png
ornamental-onion.png
pepperbox-poppy.png
README.md
```

How to use this sample transfer:

1. Connect your Archivematica instance and your ArchivesSpace instance. See
[ArchivesSpace DIP Upload][as-1] in the Archivematica user manual.

2. The ArchivesSpace ID CSV file in this transfer uses ArchivesSpace reference IDs
that exist in Artefactual's test ArchivesSpace repository as of 2020-01-21. You
may need to modify the reference IDs to match a resource in your ArchivesSpace
instance. For more information on setting up the ArchivesSpace ID CSV file, see
[Upload a DIP to ArchivesSpace][as-2].

3. Start the transfer in Archivematica. At the normalization microservice,
normalize the SIP for access.

4. At the Upload DIP microservice, select `Upload DIP to ArchivesSpace`.

5. You will be taken to the ArchivesSpace matching screen. Click on **Review
matches** to confirm that all four objects (the PNG files and the README) are
being matched to the ArchivesSpace resource.

6. Click **Finish matching**. This will take you back to the Ingest tab. The
Upload DIP microservice should complete without error.

7. Review the resource in ArchivesSpace. All four objects should be listed as
Digital Objects under Instances.

[as-1]: https://www.archivematica.org/docs/latest/user-manual/administer/dashboard-admin/#dashboard-as
[as-2]: https://www.archivematica.org/docs/latest/user-manual/access/access/#upload-a-dip-to-archivesspace
