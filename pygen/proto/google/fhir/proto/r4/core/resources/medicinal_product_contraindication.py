# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MedicinalProductContraindication:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    subject: Reference
    disease: CodeableConcept
    disease_status: CodeableConcept
    comorbidity: CodeableConcept
    therapeutic_indication: Reference
    other_therapy: MedicinalProductContraindication_OtherTherapy
    population: Population


@dataclass
class MedicinalProductContraindication_OtherTherapy:
    id: String
    extension: Extension
    modifier_extension: Extension
    therapy_relationship_type: CodeableConcept
    medication: MedicinalProductContraindication_OtherTherapy_MedicationX


@dataclass
class MedicinalProductContraindication_OtherTherapy_MedicationX:
    codeable_concept: CodeableConcept
    reference: Reference

