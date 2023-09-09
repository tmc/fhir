# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MedicinalProductInteraction:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    subject: Reference
    description: String
    interactant: MedicinalProductInteraction_Interactant
    type: CodeableConcept
    effect: CodeableConcept
    incidence: CodeableConcept
    management: CodeableConcept


@dataclass
class MedicinalProductInteraction_Interactant:
    id: String
    extension: Extension
    modifier_extension: Extension
    item: MedicinalProductInteraction_Interactant_ItemX


@dataclass
class MedicinalProductInteraction_Interactant_ItemX:
    reference: Reference
    codeable_concept: CodeableConcept

