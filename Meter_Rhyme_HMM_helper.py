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
    # Since this is the last word and we want the last syllable in
    # the line to be stressed (and all syllables alternating), we have:
    # if number of syllables in last word is even -> it must start with unstressed
    # if number of syllables in last word is odd -> it must start with stressed
    # Check number of syllables in both ending words. You have hard-coded rules
    # for this (which technically we shouldn't do but makes life easier):
    # if([] in syllable_dict[rhyme_pair[0]]):
    #     num_syllables_1 = syllable_dict[rhyme_pair[0]][1][0]
    # else:
    #     num_syllables_1 = syllable_dict[rhyme_pair[0]][0][0]

    # if([] in syllable_dict[rhyme_pair[1]]):
    #     num_syllables_2 = syllable_dict[rhyme_pair[1]][1][0]
    # else:
    #     num_syllables_2 = syllable_dict[rhyme_pair[1]][0][0]
    # ^^ Ignore (I was going to handle a case that we shouldn't need to ^^
    # Check if each word starts with a stressed syllable or unstressed syllable (or both)

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
