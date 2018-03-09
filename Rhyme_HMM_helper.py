########################################
# CS/CNS/EE 155 2018
# Problem Set 6
#
# Author:       Andrew Kang
# Description:  Set 6 HMM helper
########################################

import re
import numpy as np
import random
from Overall_HMM_helper import obs_map_reverser

####################
# HMM FUNCTIONS
####################

def sample_pair(hmm, obs_map, rhyming_dict, num_syllables=10):
    # Get reverse map.
    obs_map_r = obs_map_reverser(obs_map)
    random_rhyme = np.random.randint(0, len(rhyming_dict) - 1)
    rhyme_pair = rhyming_dict[random_rhyme]
    emission1, states1 = \
        hmm.generate_emission(num_syllables, obs_map[rhyme_pair[0]])
    emission2, states2 = \
        hmm.generate_emission(num_syllables, obs_map[rhyme_pair[1]])

    # Sample and convert sentence.
    sentence1 = [obs_map_r[i] for i in emission1]
    sentence2 = [obs_map_r[i] for i in emission2]

    sentence1 = list(reversed(sentence1))
    sentence2 = list(reversed(sentence2))

    sentence1 = ' '.join(sentence1).capitalize() + ';'
    sentence2 = ' '.join(sentence2).capitalize() + ';'

    return sentence1, sentence2
