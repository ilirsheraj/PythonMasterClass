#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 01:31:35 2022

@author: ilirsheraj
"""
from prescription_data import patients

trial_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}


# Pop will keep removing patients until the set is empty without caring about order
# Ensures we wont make prescription for the same patient again
while trial_patients:
    patient = trial_patients.pop()
    print(patient, end = " : ")
    prescription = patients[patient]
    print(prescription)