# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class LipidProfile:
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
    status: LipidProfile_StatusCode
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    encounter: Reference
    effective: LipidProfile_EffectiveX
    issued: Instant
    performer: Reference
    results_interpreter: Reference
    specimen: Reference
    result: Reference
    imaging_study: Reference
    media: LipidProfile_Media
    conclusion: String
    presented_form: Attachment


@dataclass
class LipidProfile_StatusCode:
    value: DiagnosticReportStatusCode_Value
    id: String
    extension: Extension


@dataclass
class LipidProfile_EffectiveX:
    date_time: DateTime
    period: Period


@dataclass
class LipidProfile_Media:
    id: String
    extension: Extension
    modifier_extension: Extension
    comment: String
    link: Reference

