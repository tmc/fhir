# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MedicinalProductIndication:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    subject: Reference
    disease_symptom_procedure: CodeableConcept
    disease_status: CodeableConcept
    comorbidity: CodeableConcept
    intended_effect: CodeableConcept
    duration: Quantity
    other_therapy: MedicinalProductIndication_OtherTherapy
    undesirable_effect: Reference
    population: Population


@dataclass
class MedicinalProductIndication_OtherTherapy:
    id: String
    extension: Extension
    modifier_extension: Extension
    therapy_relationship_type: CodeableConcept
    medication: MedicinalProductIndication_OtherTherapy_MedicationX


@dataclass
class MedicinalProductIndication_OtherTherapy_MedicationX:
    codeable_concept: CodeableConcept
    reference: Reference

