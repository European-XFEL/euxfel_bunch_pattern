import numpy as np

# These values are from page 10 of the XFEL timing systems specification,
# version 2.2
CHARGE_MASK = 0xf

CHARGE_VALUES = [
    0.0, .02, .03, .04,
    .06, .09, .13, .18,
    .25, .36, .50, .71,
    1.0, 1.42, 2.0, np.inf,
]

LASER_MASK = 0x3ff << 4

LASER_I1_LASER1 = 1 << 4
LASER_I1_LASER2 = 1 << 5
LASER_I1_LASER3 = 1 << 6
LASER_I2_LASER1 = 1 << 7
LASER_I2_LASER2 = 1 << 8
LASER_SEED1 = 1 << 9
LASER_SEED2 = 1 << 10
LASER_SEED3 = 1 << 11
LASER_SEED4 = 1 << 12
LASER_SEED5 = 1 << 13

PATH_MASK = 0x3f << 16

PATH_SASE5 = 1 << 16
PATH_SASE4 = 1 << 17
PATH_SASE3 = 1 << 18
PATH_SASE2 = 1 << 19
PATH_SASE1 = 1 << 20
PATH_MAIN_DUMP = 1 << 21

TDS_INJ = 1 << 31
TDS_BC1 = 1 << 30
TDS_BC2 = 1 << 29
WIRE_SCANNER = 1 << 28
PHOTON_LINE_DEFLECTION = 1 << 27
# ----------------------------------------------------------------------------
