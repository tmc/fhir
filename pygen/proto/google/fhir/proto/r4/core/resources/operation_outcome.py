# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class OperationOutcome:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    issue: OperationOutcome_Issue


@dataclass
class OperationOutcome_Issue:
    id: String
    extension: Extension
    modifier_extension: Extension
    severity: OperationOutcome_Issue_SeverityCode
    code: OperationOutcome_Issue_CodeType
    details: CodeableConcept
    diagnostics: String
    location: String
    expression: String


@dataclass
class OperationOutcome_Issue_SeverityCode:
    value: IssueSeverityCode_Value
    id: String
    extension: Extension


@dataclass
class OperationOutcome_Issue_CodeType:
    value: IssueTypeCode_Value
    id: String
    extension: Extension

