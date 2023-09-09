# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.fhirproto
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ValidationOutcome:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    issue: ValidationOutcome_Issue
    subject: Reference


@dataclass
class ValidationOutcome_Issue:
    id: String
    extension: Extension
    modifier_extension: Extension
    severity: ValidationOutcome_Issue_SeverityCode
    code: ValidationOutcome_Issue_CodeType
    details: CodeableConcept
    diagnostics: String
    location: String
    expression: String


@dataclass
class ValidationOutcome_Issue_SeverityCode:
    value: IssueSeverityCode_Value
    id: String
    extension: Extension


@dataclass
class ValidationOutcome_Issue_CodeType:
    value: IssueTypeCode_Value
    id: String
    extension: Extension

