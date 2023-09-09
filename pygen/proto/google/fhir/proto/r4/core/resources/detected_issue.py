# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class DetectedIssue:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: DetectedIssue_StatusCode
    code: CodeableConcept
    severity: DetectedIssue_SeverityCode
    patient: Reference
    identified: DetectedIssue_IdentifiedX
    author: Reference
    implicated: Reference
    evidence: DetectedIssue_Evidence
    detail: String
    reference: Uri
    mitigation: DetectedIssue_Mitigation


@dataclass
class DetectedIssue_StatusCode:
    value: ObservationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class DetectedIssue_SeverityCode:
    value: DetectedIssueSeverityCode_Value
    id: String
    extension: Extension


@dataclass
class DetectedIssue_IdentifiedX:
    date_time: DateTime
    period: Period


@dataclass
class DetectedIssue_Evidence:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    detail: Reference


@dataclass
class DetectedIssue_Mitigation:
    id: String
    extension: Extension
    modifier_extension: Extension
    action: CodeableConcept
    date: DateTime
    author: Reference

