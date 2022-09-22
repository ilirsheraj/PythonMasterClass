#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 00:56:32 2022

@author: ilirsheraj
"""
from prescription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia"]

# # Remove warfarin and add Edoxaban
# for patient in trial_patients:
#     prescription = patients[patient]
#     prescription.remove(warfarin)
#     prescription.add(edoxaban)
#     print(patient, prescription)


# # Replace remove by discard
# # Remove warfarin and add Edoxaban
# for patient in trial_patients:
#     prescription = patients[patient]
#     prescription.discard(warfarin)
#     prescription.add(edoxaban)
#     print(patient, prescription)
    
# Lets add a patient who's in nanger of killing
trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny", "John"]


# # Remove warfarin and add Edoxaban using discard
# for patient in trial_patients:
#     prescription = patients[patient]
#     prescription.discard(warfarin)
#     prescription.add(edoxaban)
#     print(patient, prescription)
    

# # We use remove instead (It will crash, so we won't add the drug and save the patient)
# # Crash is better than killing
# # Remove warfarin and add Edoxaban using discard
# for patient in trial_patients:
#     prescription = patients[patient]
#     prescription.remove(warfarin)
#     prescription.add(edoxaban)
#     print(patient, prescription)
    

# # Lets improve the code to check if warfarin is in the set
# # This is a slow approach though (Exception is better)
# for patient in trial_patients:
#     prescription = patients[patient]
#     if warfarin in prescription:
#         prescription.remove(warfarin)
#         prescription.add(edoxaban)
#     else:
#         print(f"Patient {patient} is not taking warfarin "
#               f"Please remove {patient} from the trial")
#     print(patient, prescription)


# Let's use exception (better with exceution speed) and get same output
for patient in trial_patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"Patient {patient} is not taking warfarin "
              f"Please remove {patient} from the trial")
    print(patient, prescription)