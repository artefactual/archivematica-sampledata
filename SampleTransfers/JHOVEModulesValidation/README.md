# JHOVE modules validation Sample Data

Sample JHOVE modules transfers that can be run to test files validation in Archivematica.

To use these as Archivematica transfers select the standard transfer type inside Archivematica, and then select the top-level folder "JhoveModuleValidation" to run the transfer.


## Datasets

### AIFF-HUL

**[pass.aiff](https://github.com/openpreserve/jhove/raw/refs/heads/integration/test-root/corpora/examples/modules/AIFF-hul/8-Bit-Noise-1.aif)**

**[fail.aiff](https://gist.github.com/replaceafill/48fbc414b563526a0139db649a0d0d9c)**

### GIF-HUL

**[pass.gif](https://github.com/openpreserve/jhove/blob/integration/test-root/corpora/examples/modules/GIF-hul/AA_Banner.gif)**

**[fail.gif](https://github.com/openpreserve/jhove/blob/integration/test-root/corpora/examples/modules/GIF-hul/hul-banner.gif?raw=true)** *(Corrupted file)*

### JPEG2000-HUL

**[pass.jp2](https://github.com/openpreserve/jhove/raw/refs/heads/integration/test-root/corpora/examples/modules/JPEG2000-hul/monochrome.jp2)**

**[fail.jp2](https://github.com/openpreserve/jhove/blob/refs/heads/integration/test-root/corpora/errors/modules/JPEG2000-hul/height_image_header_damaged.jp2)**

### JPEG-HUL

**[pass.jpg](https://github.com/openpreserve/jhove/blob/integration/test-root/corpora/examples/modules/JPEG-hul/20150213_140637.jpg)**

**[fail.jpg](https://github.com/openpreserve/jhove/blob/integration/test-root/corpora/examples/modules/JPEG-hul/AA_Banner.jpg)** *(Corrupted file)*

### PDF-HUL

**[pass.pdf](https://github.com/openpreserve/jhove/blob/integration/test-root/corpora/errors/modules/PDF-hul/pdf-hul-14-govdocs-489354.pdf)**

**[fail.pdf](https://github.com/openpreserve/format-corpus/blob/master/pdfCabinetOfHorrors/corruptionOneByteMissing.pdf)**

### TIFF-HUL

**[pass.tif](https://github.com/openpreserve/jhove/raw/refs/heads/integration/test-root/corpora/examples/modules/TIFF-hul/little-endian.tif)**

**[fail.tif](https://github.com/openpreserve/jhove/raw/refs/heads/integration/test-root/corpora/examples/modules/TIFF-hul/badfiles/peppers.tif)**

### WARC-KB

**[pass.warc](https://gist.github.com/replaceafill/e9c10cff981baddeba1ba3ce7e2f25f3)**

**[fail.warc](https://github.com/openpreserve/jhove/raw/refs/heads/integration/test-root/corpora/examples/modules/TIFF-hul/badfiles/peppers.tif)**

### WAVE-HUL

**[pass.wav](https://github.com/openpreserve/jhove/blob/integration/test-root/corpora/examples/modules/WAVE-hul/8-Bit-Noise-1.wav)**

**[fail.wav](https://github.com/openpreserve/jhove/blob/integration/test-root/corpora/errors/modules/WAVE-hul/wf-pcm-44khz-8bit-mono-chunk-id-above-valid-ascii.wav)**


## Notes on testing

Files are corrupted by removing few letters in middle of the file.

We used the same script for the *fail.aiff* and *pass.warc* file but modified a number in the Content-Length.
