import numpy as np
import bunch_pattern

import pytest

def test_get_charge():
    a = np.arange(16)
    np.testing.assert_array_equal(bunch_pattern.get_charge(a),
                                  bunch_pattern.CHARGE_VALUES)

    # Higher bits shouldn't interfere with the charges
    np.testing.assert_array_equal(bunch_pattern.get_charge(a + (0xff << 4)),
                                  bunch_pattern.CHARGE_VALUES)

def test_indices_at_destination():
    a = np.arange(9) << 18
    res = bunch_pattern.indices_at_destination(a, bunch_pattern.DESTINATION_T4D)
    np.testing.assert_array_equal(res, [4])

    with pytest.raises(ValueError):
        # Only DESTINATION_ constants can be used
        bunch_pattern.indices_at_destination(
            a, bunch_pattern.PHOTON_LINE_DEFLECTION)

    with pytest.raises(ValueError):
        bunch_pattern.indices_at_destination(a, bunch_pattern.DESTINATION_MASK)
