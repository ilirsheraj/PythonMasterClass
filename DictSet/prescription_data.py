#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 00:53:32 2022

@author: ilirsheraj
"""
# This is a situation where remove is more appropriate

# drugs: (Name of the drug, brief description of its function)
amlodipine = ("amlodipine", "Blood pressure")
buspirone = ("buspirone", "Anxiety disorders")
carbimazole = ("carbimazole", "Antithyroid agent")
citalopram = ("citalopram", "Antidepressant")
edoxaban = ("edoxaban", "anti-coagulant")
erythromycin = ("erythromycin", "Antibiotic")
lusinopril = ("lusinopril", "High blood pressure")
metformin = ("metformin", "Type 2 diabetes")
methotrexate = ("methotrexate", "Rheumatoid arthritis")
paracetamol = ("paracetamol", "Painkiller")
propranol = ("propranol", "Beta blocker")
simvastatin = ("simvastatin", "High cholesterol")
warfarin = ("warfarin", "anti-coagulant")

# Drugs that shouldn't be taken together
# A list of sets
adverse_interactions = [
    {metformin, amlodipine},
    {simvastatin, erythromycin},
    {citalopram, buspirone},
    {warfarin, citalopram},
    {warfarin, edoxaban},
    {warfarin, erythromycin},
    {warfarin, amlodipine},
]

# Patient prescriptions: Dictionary of the sets
patients = {
    "Anne": {methotrexate, paracetamol},
    "Bob": {carbimazole, erythromycin, methotrexate, paracetamol},
    "Charley": {buspirone, lusinopril, metformin},
    "Denise": {amlodipine, lusinopril, metformin, warfarin},
    "Eddie": {amlodipine, propranol, simvastatin, warfarin},
    "Frank": {buspirone, citalopram, propranol, warfarin},
    "Georgia": {carbimazole, edoxaban, warfarin},
    "Helmut": {erythromycin, paracetamol, propranol, simvastatin},
    "Izabella": {amlodipine, citalopram, simvastatin, warfarin},
    "John": {simvastatin},
    "Kenny": {amlodipine, citalopram, metformin},
}