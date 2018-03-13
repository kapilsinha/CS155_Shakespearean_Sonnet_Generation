########################################
# CS/CNS/EE 155 2018
# Problem Set 6
#
# Author:       Andrew Kang
# Description:  Set 6 HMM helper
########################################

import re
import numpy as np

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
        # concatenated every pair of sublists
        lines = [ x+y for x,y in zip(lines[0::2], lines[1::2]) ]
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
