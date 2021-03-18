import unittest
from break_sequence import find_thresholds

unique_label = "UNIQUE"


class TestFindThresholds(unittest.TestCase):
    """ Test class for find_thresholds().
    
    Tests if the output list of threshold functions properly. Only considers the 
    special cases for testing.
    F - Failed group.
    P - Some positive label/group.
    N - Some negative label/group.
    V - any label/group other than F.
    """

    def test_PFP(self):
        """ Test for case 01: P, F, P."""
        test_values = [1, 2, 2, 2, 3]
        test_labels = [1, 1, 0, 1, 1]
        expected_output = [1.5, 2.5]

        output = find_thresholds(test_values, test_labels, unique_label)
        self.assertListEqual(output, expected_output)

    def test_PFN(self):
        """ Test for case 02: P, F, N."""
        test_values = [1, 2, 2, 2, 3]
        test_labels = [1, 1, 0, 1, 0]
        expected_output = [1.5, 2.5]

        output = find_thresholds(test_values, test_labels, unique_label)
        self.assertListEqual(output, expected_output)

    def test_NFP(self):
        """ Test for case 03: N, F, P."""
        test_values = [1, 2, 2, 2, 3]
        test_labels = [0, 1, 0, 1, 1]
        expected_output = [1.5, 2.5]

        output = find_thresholds(test_values, test_labels, unique_label)
        self.assertListEqual(output, expected_output)

        test_values = [1, 2, 2, 2, 3, 3, 3]
        test_labels = [0, 1, 0, 1, 1, 1, 1]
        expected_output = [1.5, 2.5]

        output = find_thresholds(test_values, test_labels, unique_label)
        self.assertListEqual(output, expected_output)

    def test_NFN(self):
        """ Test for case 04: N, F, N."""
        test_values = [1, 2, 2, 2, 3]
        test_labels = [0, 1, 0, 1, 0]
        expected_output = [1.5, 2.5]

        output = find_thresholds(test_values, test_labels, unique_label)
        self.assertListEqual(output, expected_output)

    def test_VFF(self):
        """ Test for case 05: V, F, F."""
        test_values = [0, 1, 1, 1, 2, 2, 2]
        test_labels = [0, 0, 0, 1, 1, 0, 1]
        expected_output = [0.5, 1.5]

        output = find_thresholds(test_values, test_labels, unique_label)
        self.assertListEqual(output, expected_output)

    def test_FFV(self):
        """ Test for case 06: F, F, V."""
        test_values = [1, 1, 1, 2, 2, 2, 3]
        test_labels = [0, 0, 1, 1, 0, 1, 0]
        expected_output = [1.5, 2.5]

        output = find_thresholds(test_values, test_labels, unique_label)
        self.assertListEqual(output, expected_output)

    def test_FFF(self):
        """ Test for case 07: F, F, F."""
        test_values = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        test_labels = [0, 0, 1, 1, 0, 1, 1, 1, 0]
        expected_output = [1.5, 2.5]

        output = find_thresholds(test_values, test_labels, unique_label)
        self.assertListEqual(output, expected_output)

    def test_VFFV(self):
        """ Test for case 08: V, F, F, V."""
        test_values = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3]
        test_labels = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0]
        expected_output = [0.5, 1.5, 2.5]

        output = find_thresholds(test_values, test_labels, unique_label)
        self.assertListEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
