# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ImmunizationEvaluation:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: ImmunizationEvaluation_StatusCode
    patient: Reference
    date: DateTime
    authority: Reference
    target_disease: CodeableConcept
    immunization_event: Reference
    dose_status: CodeableConcept
    dose_status_reason: CodeableConcept
    description: String
    series: String
    dose_number: ImmunizationEvaluation_DoseNumberX
    series_doses: ImmunizationEvaluation_SeriesDosesX


@dataclass
class ImmunizationEvaluation_StatusCode:
    value: ImmunizationEvaluationStatusCodesValueSet_Value
    id: String
    extension: Extension


@dataclass
class ImmunizationEvaluation_DoseNumberX:
    positive_int: PositiveInt
    string_value: String


@dataclass
class ImmunizationEvaluation_SeriesDosesX:
    positive_int: PositiveInt
    string_value: String

