# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MedicinalProductManufactured:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    manufactured_dose_form: CodeableConcept
    unit_of_presentation: CodeableConcept
    quantity: Quantity
    manufacturer: Reference
    ingredient: Reference
    physical_characteristics: ProdCharacteristic
    other_characteristics: CodeableConcept

