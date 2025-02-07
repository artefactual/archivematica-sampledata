# JHOVE Module Validation Sample Transfers

This transfer contains files designed to test validation using JHOVE commands introduced in Archivematica 1.18.0. It includes both valid and invalid files to demonstrate passing and failing validation cases.

Files are organized into folders named after the corresponding JHOVE module used for validation. Within each folder, files follow a consistent naming convention:

* `pass.*` - Files that successfully pass validation.
* `fail.*` - Files that fail validation.

Most files originate from the
`test-root` directory of [the JHOVE repository](https://github.com/openpreserve/jhove/), while others were artificially generated using Python scripts. Files below marked with an asterisk (\*) were intentionally corrupted by removing a few bytes from their middle section. Additionally, the
`fail.warc` file was created using the same Python script as `pass.warc`, but with its
`Content-Length` value manually altered to cause validation failure.

## File Summary

| JHOVE Module     | Validation File | Source                                                                                                                                                                                          |
| ---------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AIFF-HUL**     | pass.aiff       | [Original](https://github.com/openpreserve/jhove/blob/7306ffaf773577ba34abb21157c1cea38e219731/test-root/corpora/examples/modules/AIFF-hul/8-Bit-Noise-1.aif)                                   |
|                  | fail.aiff       | [Original](https://gist.github.com/replaceafill/48fbc414b563526a0139db649a0d0d9c)                                                                                                               |
| **GIF-HUL**      | pass.gif        | [Original](https://github.com/openpreserve/jhove/blob/7306ffaf773577ba34abb21157c1cea38e219731/test-root/corpora/examples/modules/GIF-hul/AA_Banner.gif)                                        |
|                  | fail.gif \*     | [Original](https://github.com/openpreserve/jhove/blob/7306ffaf773577ba34abb21157c1cea38e219731/test-root/corpora/examples/modules/GIF-hul/hul-banner.gif)                                       |
| **JPEG2000-HUL** | pass.jp2        | [Original](https://github.com/openpreserve/jhove/blob/7306ffaf773577ba34abb21157c1cea38e219731/test-root/corpora/examples/modules/JPEG2000-hul/monochrome.jp2)                                  |
|                  | fail.jp2        | [Original](https://github.com/openpreserve/jhove/blob/7306ffaf773577ba34abb21157c1cea38e219731/test-root/corpora/errors/modules/JPEG2000-hul/height_image_header_damaged.jp2)                   |
| **JPEG-HUL**     | pass.jpg        | [Original](https://github.com/openpreserve/jhove/blob/7306ffaf773577ba34abb21157c1cea38e219731/test-root/corpora/examples/modules/JPEG-hul/20150213_140637.jpg)                                 |
|                  | fail.jpg \*     | [Original](https://github.com/openpreserve/jhove/blob/7306ffaf773577ba34abb21157c1cea38e219731/test-root/corpora/examples/modules/JPEG-hul/AA_Banner.jpg)                                       |
| **PDF-HUL**      | pass.pdf        | [Original](https://github.com/openpreserve/jhove/blob/7306ffaf773577ba34abb21157c1cea38e219731/test-root/corpora/errors/modules/PDF-hul/pdf-hul-14-govdocs-489354.pdf)                          |
|                  | fail.pdf        | [Original](https://github.com/openpreserve/jhove/blob/7306ffaf773577ba34abb21157c1cea38e219731/test-root/corpora/errors/modules/PDF-hul/corruptionOneByteMissing.pdf)                           |
| **TIFF-HUL**     | pass.tif        | [Original](https://github.com/openpreserve/jhove/blob/7306ffaf773577ba34abb21157c1cea38e219731/test-root/corpora/examples/modules/TIFF-hul/little-endian.tif)                                   |
|                  | fail.tif        | [Original](https://github.com/openpreserve/jhove/blob/7306ffaf773577ba34abb21157c1cea38e219731/test-root/corpora/examples/modules/TIFF-hul/badfiles/peppers.tif)                                |
| **WARC-KB**      | pass.warc       | [Original](https://gist.github.com/replaceafill/e9c10cff981baddeba1ba3ce7e2f25f3)                                                                                                               |
|                  | fail.warc \*\*  |                                                                                                                                                                                                 |
| **WAVE-HUL**     | pass.wav        | [Original](https://github.com/openpreserve/jhove/blob/7306ffaf773577ba34abb21157c1cea38e219731/test-root/corpora/examples/modules/WAVE-hul/8-Bit-Noise-1.wav)                                   |
|                  | fail.wav        | [Original](https://github.com/openpreserve/jhove/blob/7306ffaf773577ba34abb21157c1cea38e219731/test-root/corpora/errors/modules/WAVE-hul/wf-pcm-44khz-8bit-mono-chunk-id-above-valid-ascii.wav) |

(\*) Files were corrupted by removing a few bytes in the middle.  
(\*\*) The `fail.warc` is the same `pass.warc` file with the `Content-Length` field altered.
