# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MedicinalProductUndesirableEffect:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    subject: Reference
    symptom_condition_effect: CodeableConcept
    classification: CodeableConcept
    frequency_of_occurrence: CodeableConcept
    population: Population

