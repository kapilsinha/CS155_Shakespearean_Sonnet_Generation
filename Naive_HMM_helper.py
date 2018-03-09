########################################
# CS/CNS/EE 155 2018
# Problem Set 6
#
# Author:       Andrew Kang
# Description:  Set 6 HMM helper
########################################

import re
import numpy as np
from Overall_HMM_helper import obs_map_reverser

####################
# HMM FUNCTIONS
####################

def sample_sentence(hmm, obs_map, num_syllables=10):
    # Get reverse map.
    obs_map_r = obs_map_reverser(obs_map)

    # Sample and convert sentence.
    emission, states = hmm.generate_emission(num_syllables)
    sentence = [obs_map_r[i] for i in emission]

    return ' '.join(sentence).capitalize() + ';'