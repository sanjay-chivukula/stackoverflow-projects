"""
Stackoverflow: 66623164
Title: Find thresholds for binary classification.
Link: https://stackoverflow.com/questions/66623164/find-thresholds-for-binary-classification/
"""
from itertools import groupby


def find_thresholds(values: list, labels: list, case2_label: any) -> list:
    """ Returns thresholds for given examples of values and labels.

    :param values: list of values of any type for each example.
    :param labels: list of labels of any type for each example.
    :param case2_label: label value to assign for groups which satisfy Case 2.
                        This label must be different from the set of labels
                        assigned for the examples. Must be same type as label.
    :return thresholds: list of thresholds T, where T is (num[i] + num[i+1) / 2.
                        T should be computed for the below mentioned cases.

    Cases to compute threshold T:
     - Case 1: T is a threshold if it falls between two consecutive examples
               that do not belong to the same class.

     - Case 2: In the special case when a group of two  or more examples have
               the same value but belong to more than one class, then the cut
               points on either side of the examples are also thresholds.
               The examples with identical values cannot be separated.

    Expected: Lengths of values and labels must match.
              They must be greater than 1.
    Expected: If labels or values belong to custom type their __eq__() must be
              overridden appropriately.
    Assumption: The examples are grouped in increasing order.
    """
    assert (len(values) == len(labels))
    assert (len(values) > 1)

    def compress_group(vls):
        """Combines duplicate (values, labels) to single (value, label)."""
        val0, lab0 = next(vls[1])
        if all(lab == lab0 for val, lab in vls[1]):
            return val0, lab0
        return val0, case2_label

    # Pairing each value and label into a tuple and getting them as list.
    vl_combined = [(v, l) for v, l in zip(values, labels)]

    # Groups pairs with same values.
    vl_groups = groupby(vl_combined, lambda vc: vc[0])

    # For each such groups it compresses them into single tuple.
    vl_groups = map(lambda vl_group: compress_group(vl_group), vl_groups)

    # Output variable.
    thresholds = []

    # Getting the first group.
    prev_value, prev_label = next(vl_groups)

    for curr_value, curr_label in vl_groups:
        # If matches problem's cases compute and append threshold.
        # NOTE: The threshold computation can be passed as callable object
        # argument to this method and used here, to make it even more generic.
        if prev_label == case2_label or curr_label != prev_label:
            threshold = (prev_value + curr_value) / 2
            thresholds.append(threshold)

        # Update states.
        prev_value, prev_label = curr_value, curr_label

    return thresholds


if __name__ == "__main__":
    # Sample Case.
    # Find detailed test in test_break_sequence.py.
    test_values = [1, 1, 1, 2, 2, 2, 3]
    test_labels = [0, 0, 1, 1, 0, 1, 0]
    print(find_thresholds(test_values, test_labels, -1))
