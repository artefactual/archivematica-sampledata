## Synthetic files created to be unknown to Siegfried and Fido

These files are designed to test various different format identification tools.
Each file format should be unknown at least to both Siegfried and Fido. It is
unlikely they will appear in a registry such as PRONOM in the near future.

### Format specification

The formats are broken down as follows:

<table>
	<tr>
		<td>magic number (6 bytes)</td>
		<td>version (2 bytes)</td>
		<td>year (2 bytes)</td>
	</tr>
	<tr>
		<td colspan="3">payload (42 bytes)</td>
	</tr>

<table>

The content is fairly arbitrary with the magic numbers being one of the
following:

* `ba 5e ba 11 00 FF`
* `ca 55 e7 7e 00 FF`
* `ca b0 05 e0 00 FF`
* `de ba 7a b1 e0 FF`
* `10 05 e1 ea f0 FF`

Version and year are as follows:

* Version: `00 01`
* Year (2019): `07 E3`

The 42 byte 'payload' consists of entirely null characters.

The `.format` extension is not currently known to PRONOM so neither Siegfried
or Fido will try to do anything with that. That however could change, and so
may be the one component of this small collection that may need changing over
time.

### Microservice Job output

The exit code of the `Identify file format` job will be non-zero indicating
that the file could not be identified.
