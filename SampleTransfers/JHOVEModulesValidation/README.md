# JHOVE Module Validation Sample Transfers

This transfer contains files designed to test validation using JHOVE commands introduced in Archivematica 1.18.0. It includes both valid and invalid files to demonstrate passing and failing validation cases.

Files are organized into folders named after the corresponding JHOVE module used for validation. Within each folder, files follow a consistent naming convention:

* `pass.*` - Files that successfully pass validation.
* `fail.*` - Files that fail validation.

Most files originate from the `test-root` directory of [the JHOVE repository](https://github.com/openpreserve/jhove/), while others were artificially generated using Python scripts. Files below marked with an asterisk (\*) were intentionally corrupted by removing a few bytes from their middle section. Additionally, the `fail.warc` file was created using the same Python script as `pass.warc`, but with its `Content-Length` value manually altered to cause validation failure.

## File Summary

| JHOVE Module     | Validation File | Source   |
|------------------|-----------------|----------|
| **AIFF-HUL**     | pass.aiff       | [Original](https://github.com/openpreserve/jhove/blob/c1db6d76fff02470d012909ee15b1a969a5e7422/test-root/corpora/examples/modules/AIFF-hul/8-Bit-Noise-1.aif) |
|                  | fail.aiff       | Original |
| **GIF-HUL**      | pass.gif        | Original |
|                  | fail.gif *      | Original |
| **JPEG2000-HUL** | pass.jp2        | Original |
|                  | fail.jp2        | Original |
| **JPEG-HUL**     | pass.jpg        | Original |
|                  | fail.jpg *      | Original |
| **PDF-HUL**      | pass.pdf        | Original |
|                  | fail.pdf        | Original |
| **TIFF-HUL**     | pass.tif        | Original |
|                  | fail.tif        | Original |
| **WARC-KB**      | pass.warc       | Original |
|                  | fail.warc **    | Original |
| **WAVE-HUL**     | pass.wav        | Original |
|                  | fail.wav        | Original |

(\*) Files were corrupted by removing a few bytes in the middle.  
(\*\*) The `fail.warc` is the same `pass.warc` file with the `Content-Length` field altered.
