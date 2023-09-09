# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class EnrollmentRequest:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: EnrollmentRequest_StatusCode
    created: DateTime
    insurer: Reference
    provider: Reference
    candidate: Reference
    coverage: Reference


@dataclass
class EnrollmentRequest_StatusCode:
    value: FinancialResourceStatusCode_Value
    id: String
    extension: Extension

