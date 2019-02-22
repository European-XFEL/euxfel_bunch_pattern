import numpy as np
import bunch_pattern

def test_get_charge():
    a = np.arange(16)
    np.testing.assert_array_equal(bunch_pattern.get_charge(a),
                                  bunch_pattern.CHARGE_VALUES)

    # Higher bits shouldn't interfere with the charges
    np.testing.assert_array_equal(bunch_pattern.get_charge(a + (0xff << 4)),
                                  bunch_pattern.CHARGE_VALUES)
