import numpy as np

# These values are from page 10 of the XFEL timing systems specification,
# version 2.2, updated following a screenshot of the bunch pattern decoder
# device.
CHARGE_MASK = 0xf

# Charge in nC for the 16 possible 4 bit combinations
CHARGE_VALUES = np.array([
    0.0, .02, .03, .04,
    .06, .09, .13, .18,
    .25, .36, .50, .71,
    1.0, 1.42, 2.0, 4.0,
])

LASER_MASK = 0x3ff << 4

LASER_I1_LASER1 = 1 << 4
LASER_I1_LASER2 = 1 << 5
LASER_I1_LASER3 = 1 << 6
LASER_I2_LASER1 = 1 << 7
LASER_SEED1 = 1 << 8
LASER_SEED2 = 1 << 8
LASER_SEED3 = 1 << 10
LASER_SEED4 = 1 << 11
LASER_SEED5 = 1 << 12
LASER_SEED6 = 1 << 13
LASER_SEED7 = 1 << 14
LASER_SEED8 = 1 << 15
LASER_SEED9 = 1 << 16

DESTINATION_MASK = 0xf << 18

# 16 possible bit combinations for destinations, only 9 used at present
DESTINATION_NONE = 0
DESTINATION_I1LST = 1  # Laser stand-alone
DESTINATION_T5D = 2    # SASE2 dump
DESTINATION_G1D = 3    # Gun dump/valve
DESTINATION_T4D = 4    # SASE1/3 dump
DESTINATION_ILD = 5    # Injector dump
DESTINATION_B1D = 6    # B1 dump
DESTINATION_B2D = 7    # B2 dump
DESTINATION_TLD = 8

EVT_TRIGGER_25 = 1 << 22  # ?

TDS_INJ = 1 << 31
TDS_BC1 = 1 << 30
TDS_BC2 = 1 << 29
WIRE_SCANNER = 1 << 28
PHOTON_LINE_DEFLECTION = 1 << 27  # Soft kick (e.g. SA3)
BEAM_DISTRIBUTION_KICK = 1 << 26
# ----------------------------------------------------------------------------

def get_charge(bunchpattern):
    """Extract charge values in nC from bunch pattern data

    Parameters
    ----------
    bunchpattern : int or numpy array of integers
      The bunch pattern data
    """
    charge_bits = bunchpattern & CHARGE_MASK
    return CHARGE_VALUES[charge_bits]
