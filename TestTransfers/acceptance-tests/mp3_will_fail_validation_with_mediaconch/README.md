# MP3 files to fail validation policy check in Archivematica Acceptance Tests

This transfer consists of the following files, plus this `README.md`.

```bash
	fmt-134-signature-id-266-good.mp3
	fmt-134-signature-id-268-skeleton.mp3
	fmt-134-signature-id-280-skeleton.mp3
	fmt-134-signature-id-266-skeleton.mp3
	fmt-134-signature-id-269-skeleton.mp3
	fmt-134-signature-id-281-skeleton.mp3
	fmt-134-signature-id-267-skeleton.mp3
	fmt-134-signature-id-279-skeleton.mp3
	fmt-134-signature-id-282-skeleton.mp3
```
The expectation is that it will be used against a low-risk [Mediaconch][mc-1]
policy in the Archivematica Format Policy Register. All but one file should
fail thus testing the policy checking mechanism of the system.

The files marked `*-skeleton.mp3` are all from the
[PRONOM Skeleton Test Suite][mc-2] and so will pass Siegfried and Fido file
format identification. They contain zero-payload and so no additional
information can be extracted from them using tools such as [Mediainfo][mc-3].

The file marked `*-good.mp3` will pass validation.

The policy that these are designed to be checked against is as follows:
```python
import sys
from ammcpc import MediaConchPolicyCheckerCommand

# Valuate this constant with the text (XML) of the policy.
POLICY = """
<?xml version="1.0"?>
<policy type="and" name="MP3 has duration" license="CC-BY-SA-4.0+">
  <description>Rudimentary test to check for an MP3 having a duration value.</description>
  <rule name="Does the audio duration exist?" value="Duration" tracktype="General" occurrence="*" operator="exists">mp3</rule>
</policy>
""".strip()

# Valuate this constant with the name of the policy.
POLICY_NAME = "MP3 has duration"

if __name__ == '__main__':
    target = sys.argv[1]
    policy_checker = MediaConchPolicyCheckerCommand(
        policy=POLICY,
        policy_file_name=POLICY_NAME)
    sys.exit(policy_checker.check(target))
```

[mc-1]: https://mediaarea.net/MediaConch
[mc-2]: https://zenodo.org/record/3269467#.XR8-sWwzY5k
[mc-3]: https://mediaarea.net/en/MediaInfo
