# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class AdverseEvent:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    actuality: AdverseEvent_ActualityCode
    category: CodeableConcept
    event: CodeableConcept
    subject: Reference
    encounter: Reference
    date: DateTime
    detected: DateTime
    recorded_date: DateTime
    resulting_condition: Reference
    location: Reference
    seriousness: CodeableConcept
    severity: CodeableConcept
    outcome: CodeableConcept
    recorder: Reference
    contributor: Reference
    suspect_entity: AdverseEvent_SuspectEntity
    subject_medical_history: Reference
    reference_document: Reference
    study: Reference


@dataclass
class AdverseEvent_ActualityCode:
    value: AdverseEventActualityCode_Value
    id: String
    extension: Extension


@dataclass
class AdverseEvent_SuspectEntity:
    id: String
    extension: Extension
    modifier_extension: Extension
    instance: Reference
    causality: AdverseEvent_SuspectEntity_Causality


@dataclass
class AdverseEvent_SuspectEntity_Causality:
    id: String
    extension: Extension
    modifier_extension: Extension
    assessment: CodeableConcept
    product_relatedness: String
    author: Reference
    method: CodeableConcept

