# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class EnrollmentResponse:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: EnrollmentResponse_StatusCode
    request: Reference
    outcome: EnrollmentResponse_OutcomeCode
    disposition: String
    created: DateTime
    organization: Reference
    request_provider: Reference


@dataclass
class EnrollmentResponse_StatusCode:
    value: FinancialResourceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class EnrollmentResponse_OutcomeCode:
    value: ClaimProcessingCode_Value
    id: String
    extension: Extension

