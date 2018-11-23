## Broken Package Format Types

The files in this directory attempt to break the package extract
functionality of Archivematica. The files all present a signature
that might be interpreted by the system as an archive file format
of some form or another, e.g. `.zip`, `.gz` etc.

All files should fail at the *'Extract contents from compressed
archives'* job in Archivematica. The behaviour from there depends
on how Archivematica is configured.

### Files in this set

* `gz/x-fmt-266-signature-id-201.gz` - skeleton file created against
  PRONOM release v93.
* `rar_1/fmt-411-signature-id-591.rar` - skeleton file created against
  PRONOM release v93.
* `rar_2/skeleton-x-fmt-264-signature-id-590.rar` - skeleton file
  created against PRONOM release v93.
* `tar/skeleton-x-fmt-265-signature-id-265.tar` - skeleton file
   created against PRONOM release v93.
* `zip/broken-cp437.zip` - Manually created and manually broken
  file that should have a cp437 encoded filename inside it.

**NB:** Skeleton files contain the bare minimum of information to be
matched against a specific version of DROID/PRONOM. They do not
actually reflect a 'real' archive format, that is, there are no files
inside them to be discovered by Archivematica's tooling. Most zip-like
tools should consider these files to be 'corrupt' and so should always
trigger a failure state.
