# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ClinicalImpression:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: ClinicalImpression_StatusCode
    status_reason: CodeableConcept
    code: CodeableConcept
    description: String
    subject: Reference
    encounter: Reference
    effective: ClinicalImpression_EffectiveX
    date: DateTime
    assessor: Reference
    previous: Reference
    problem: Reference
    investigation: ClinicalImpression_Investigation
    protocol: Uri
    summary: String
    finding: ClinicalImpression_Finding
    prognosis_codeable_concept: CodeableConcept
    prognosis_reference: Reference
    supporting_info: Reference
    note: Annotation


@dataclass
class ClinicalImpression_StatusCode:
    value: ClinicalImpressionStatusValueSet_Value
    id: String
    extension: Extension


@dataclass
class ClinicalImpression_EffectiveX:
    date_time: DateTime
    period: Period


@dataclass
class ClinicalImpression_Investigation:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    item: Reference


@dataclass
class ClinicalImpression_Finding:
    id: String
    extension: Extension
    modifier_extension: Extension
    item_codeable_concept: CodeableConcept
    item_reference: Reference
    basis: String

