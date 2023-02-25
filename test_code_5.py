import os,sys
import random
import pytest
from code_5 import get_melanoma_mortality_information_by_state
from code_5 import get_asthma_mortality_information_by_state
from code_5 import get_chronic_liver_mortality_by_state
from code_5 import get_missing_values_count_by_state

def check_if_file_exists():
    try:
        exists = os.path.exists("code_5.py")
        assert exists == True
    except:
        sys.exit()

def test_get_melanoma_mortality_information_by_state():
    check_if_file_exists()
    state_code = ['tx','va','ga','fl','ca','il','ny','nj','tn','co']
    value = [80.72,47.4,47.22,123.19,131.95,74.7,66.25,42.45,45.93,33.44]
    random_choice = random.randint(0,9)
    assert get_melanoma_mortality_information_by_state(state_code[random_choice]) == value[random_choice]

def test_get_asthma_mortality_information_by_state():
    state_code = ['tx','va','ga','fl','ca','il','ny','nj','tn','co']
    value = [41.31,26.01,27.08,37.53,64.92,43.81,57.5,29.81,22.42,18.55]
    check_if_file_exists()
    random_choice = random.randint(0,9)
    assert get_asthma_mortality_information_by_state(state_code[random_choice]) == value[random_choice]

def test_get_chronic_liver_mortality_by_state():
    state_code = ['tx','va','ga','fl','ca','il','ny','nj','tn','co']
    value = [11.74,9.72,9.08,12.42,15.3,9.52,7.45,8.39,13.57,18.93]
    check_if_file_exists()
    random_choice = random.randint(0,9)
    assert get_chronic_liver_mortality_by_state(state_code[random_choice]) == value[random_choice]

def test_get_missing_values_count_by_state():
    state_code = ['tx','va','ga','fl','ca','il','ny','nj','tn','co']
    value = [4583,5801,5423,4150,4554,8304,4433,5338,7457,5378]
    check_if_file_exists()
    random_choice = random.randint(0,9)
    assert get_missing_values_count_by_state(state_code[random_choice]) == value[random_choice]

