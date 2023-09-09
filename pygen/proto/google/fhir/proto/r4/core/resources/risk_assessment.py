# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class RiskAssessment:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    parent: Reference
    status: RiskAssessment_StatusCode
    method: CodeableConcept
    code: CodeableConcept
    subject: Reference
    encounter: Reference
    occurrence: RiskAssessment_OccurrenceX
    condition: Reference
    performer: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    basis: Reference
    prediction: RiskAssessment_Prediction
    mitigation: String
    note: Annotation


@dataclass
class RiskAssessment_StatusCode:
    value: ObservationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class RiskAssessment_OccurrenceX:
    date_time: DateTime
    period: Period


@dataclass
class RiskAssessment_Prediction:
    id: String
    extension: Extension
    modifier_extension: Extension
    outcome: CodeableConcept
    probability: RiskAssessment_Prediction_ProbabilityX
    qualitative_risk: CodeableConcept
    relative_risk: Decimal
    when: RiskAssessment_Prediction_WhenX
    rationale: String


@dataclass
class RiskAssessment_Prediction_ProbabilityX:
    decimal: Decimal
    range: Range


@dataclass
class RiskAssessment_Prediction_WhenX:
    period: Period
    range: Range

