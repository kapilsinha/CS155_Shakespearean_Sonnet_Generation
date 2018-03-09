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

####################
# HMM FUNCTIONS
####################

# Modified function for Miniproject 3 (now takes a list of texts as opposed to a single text)
def parse_observations(texts):
    total_obs = []
    obs_counter = 0
    obs_map = {}
    for text in texts:
        # Convert text to dataset.
        lines = [line.split() for line in text.split('\n') if line.split()]
        obs = []
        for line in lines:
            obs_elem = []
            for word in line:
                word = re.sub(r'[^\w]', '', word).lower()
                if word not in obs_map:
                    # Add unique words to the observations map.
                    obs_map[word] = obs_counter
                    obs_counter += 1

                # Add the encoded word.
                obs_elem.append(obs_map[word])

            # Add the encoded sequence.
            obs.append(obs_elem)
        total_obs.append(obs)
    return total_obs, obs_map

# Function from solutions in Set 6 to change text to data but in reverse
def parse_observations_backwards(texts):
    total_obs = []
    obs_counter = 0
    obs_map = {}
    for text in texts:
        # Convert text to dataset.
        lines = [line.split() for line in text.split('\n') if line.split()]
        obs = []
        for line in lines:
            line = line[::-1]

            obs_elem = []
            for word in line:
                word = re.sub(r'[^\w]', '', word).lower()
                if word not in obs_map:
                    # Add unique words to the observations map.
                    obs_map[word] = obs_counter
                    obs_counter += 1

                # Add the encoded word.
                obs_elem.append(obs_map[word])

            # Add the encoded sequence.
            obs.append(obs_elem)
        total_obs.append(obs)
    return total_obs, obs_map

def obs_map_reverser(obs_map):
    obs_map_r = {}

    for key in obs_map:
        obs_map_r[obs_map[key]] = key

    return obs_map_r

def sample_sentence(hmm, obs_map, syllable_dict, num_syllables=10):
    # Get reverse map.
    obs_map_r = obs_map_reverser(obs_map)

    # Sample and convert sentence.
    emission, states = hmm.generate_emission(syllable_dict, num_syllables)
    sentence = [obs_map_r[i] for i in emission]

    return ' '.join(sentence).capitalize() + ';'

def sample_pair(hmm, obs_map, syllable_dict, rhyming_dict, num_syllables=10):
    # Get reverse map.
    obs_map_r = obs_map_reverser(obs_map)

    random_rhyme = np.random.randint(0, len(rhyming_dict) - 1)

    rhyme_pair = rhyming_dict[random_rhyme]

    emission1, states1 = hmm.generate_emission_rhyme(syllable_dict, \
                            num_syllables, obs_map[rhyme_pair[0]])
    emission2, states2 = hmm.generate_emission_rhyme(syllable_dict, \
                            num_syllables, obs_map[rhyme_pair[1]])

    # Sample and convert sentence.
    sentence1 = [obs_map_r[i] for i in emission1]
    sentence2 = [obs_map_r[i] for i in emission2]

    sentence1 = list(reversed(sentence1))
    sentence2 = list(reversed(sentence2))

    sentence1 = ' '.join(sentence1).capitalize() + ';'
    sentence2 = ' '.join(sentence2).capitalize() + ';'

    return sentence1, sentence2
