#=============================================================================#
#                          MODEL DEFINITION FILE                              #
#=============================================================================#
import numpy as np


#-----------------------------------------------------------------------------#
# Function defining the model.                                                #
#                                                                             #
#  pDict       = Dictionary of parameters, created by parsing inParms, below. #
#  x           = Array of x values                                            #
#-----------------------------------------------------------------------------#
def model(pDict, x):
    """Simple linear model."""
    
    # Calculate the complex fractional q and u spectra
    ymod = pDict["m"] * x + pDict["c"]
    return ymod


#-----------------------------------------------------------------------------#
# Parameters for the above model.                                             #
#                                                                             #
# Each parameter is defined by a dictionary with the following keywords:      #
#   parname    ...   parameter name used in the model function above          #
#   label      ...   latex style label used by plotting functions             #
#   value      ...   value of the parameter if priortype = "fixed"            #
#   bounds     ...   [low, high] limits of the prior                          #
#   priortype  ...   "uniform", "normal", "log" or "fixed"                    #
#   wrap       ...   set > 0 for periodic parameters (e.g., for an angle)     #
#-----------------------------------------------------------------------------#
inParms = [
    {"parname":   "m",
     "label":     "$m$",
     "value":     0.5,
     "bounds":    [1e-3, 1e3],
     "priortype": "uniform",
     "wrap":      0},
    
    {"parname":   "c",
     "label":     "$c$",
     "value":     0.0,
     "bounds":    [-100, +100],
     "priortype": "uniform",
     "wrap":      1},
]


#-----------------------------------------------------------------------------#
# Arguments controlling the Nested Sampling algorithm                         #
#-----------------------------------------------------------------------------#
nestArgsDict = {"n_live_points": 1000,
                "verbose": False}
