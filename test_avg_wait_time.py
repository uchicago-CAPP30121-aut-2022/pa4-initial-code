'''
Polling places: test code for avg_wait_time
'''

import csv
import pytest
import util
import sys
import os

# Handle the fact that the grading code may not
# be in the same directory as implementation
sys.path.insert(0, os.getcwd())

from simulate import find_avg_wait_time

# DO NOT REMOVE THESE LINES OF CODE
# pylint: disable-msg= invalid-name, missing-docstring


DATA_DIR = "./test-data/"

with open(DATA_DIR + "avg_wait_time.csv") as f:
    reader = csv.DictReader(f)

    configs = []
    for row in reader:
        config = (row["config_file"],
                  int(row["num_trials"]),
                  int(row["num_booths"]),
                  float(row["avg_wait_time"])
                 )
        configs.append(config)

def run_test(precincts_file, num_trials, num_booths, avg_wait_time):
    p, seed = util.load_precinct(precincts_file)

    avg_wt = find_avg_wait_time(p, num_booths, num_trials, initial_seed=seed)

    assert avg_wt == pytest.approx(avg_wait_time)

@pytest.mark.parametrize("precincts_file,num_trials,num_booths,avg_wait_time", configs)
def test_simulate(precincts_file, num_trials, num_booths, avg_wait_time):
    run_test(DATA_DIR + precincts_file, num_trials, num_booths, avg_wait_time)
