# StructMap Sample Transfers

Example structMap transfers for demonstration and acceptance testing of
Archivematica structMap features.

## Examples

### Example 1: Minimal structMap Example

A minimal example of a custom logical structMap to help demonstrate and
document the concept.

**Example 1** provides additional contextual information about the content of
the AIP and attaches a label to the audio stream included.

The content is licensed as follows:

Short Listen: Ferdinand, the Misunderstood Bull by [With Good Reason][smap-1].
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/">Creative Commons Attribution 3.0 Unported License</a>&nbsp;<a rel="license" href="http://creativecommons.org/licenses/by/3.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/3.0/80x15.png" /></a>.

[smap-1]: https://soundcloud.com/withgoodreason/short-listen-ferdinand-the-misunderstood-bull

### Example 2: Single Object Example

A structMap can describe structure across space and time. For time-based media
we can generate structure using timestamps.

**Example 2** describes the contents of a single audio stream encoded as MP3.

*Example 2 is based on this worked example on the Library of Congress
[website](https://www.loc.gov/standards/mets/METSOverview.v2.html#structmap)
and uses `<area>` elements inside the `<fptr>` to indicate divisions within
portions of a single file.*

**Note:** The content license is the same as in Example 1.

### Example 3: Simple Book Example

A structMap can facilitate the [comprehension and navigation][smap-2] of a
digital transfer. Files with names, `page_01`, `page_02`, `page_03` do not
describe much on their own, and so a structMap can be used to attach labels
and describe the logical ordering of digital objects.

**Example 3** describes the structure of a book using a flat transfer layout.

[smap-2]: https://www.loc.gov/standards/mets/docs/mets.v1-9.html#structMap

### Example 4: Complex Structure Example

Organizing the content of a digital transfer into something other than that
which was submitted, more complex paths can be used in a transfer layout and
the structMap can still provide a logical representation of that material, e.g.
for display to the user or the creation of new structure emerging from the
AIP, i.e. a DIP.

**Example 4** describes the structure of a book using a transfer structured
using different directories.

### Example 5: Unicode encoded Example

It stands to reason that a structMap should be able to describe any content
submitted by the user. Example 5 encodes a structMap for consumption in
Spanish.

**Example 5** Demonstrates the mechanism's ability to manipulate data using
Unicode character encoding.
