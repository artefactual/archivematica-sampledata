#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""To run the tests::

    $ python -m unittest tests.test_createtransfers
"""
import unittest

import createtransfers


class TestCreateTransfers(unittest.TestCase):

    def test_calculate_total_size(self):
        """ We want to be able to provide some useful feedback about what
        users will be creating when they run this function. The values used
        are fairly sensitive and can become quite high if used without care.
        """

        # Folder structure named tuple to return. This should look like
        # the strcuture that we're using inside the create structure code
        # itself. Attributes: depth, dirs, files.
        structure = createtransfers.FolderStructure

        # Some values to test. The values here demonstrate how quickly the
        # structure of what we're creating can explode if not carefully
        # configured. Results are calculated using the following formula:
        #
        # dirs = (no_dirs^depth) + (no_dirs^depth-1) + (no_dirs^depth-n...)
        # files = no_files * dirs
        #
        res = [{"input": structure(5, 3, 4),
                "output": structure(5, 363, 1452)},
               {"input": structure(2, 3, 2),
                "output": structure(2, 12, 24)},
               {"input": structure(10, 2, 1),
                "output": structure(10, 2046, 2046)},
               {"input": structure(2, 2, 2),
                "output": structure(2, 6, 12)},
               {"input": structure(8, 12, 3),
                "output": structure(8, 469070940, 1407212820)},
               ]

        testfunc = createtransfers.calculate_total_size

        for r in res:
            output = testfunc(r["input"])

            self.assertEqual(output.dirs, r["output"].dirs)
            self.assertEqual(output.files, r["output"].files)
            self.assertEqual(output.depth, r["output"].depth)


if __name__ == '__main__':
    unittest.main()
