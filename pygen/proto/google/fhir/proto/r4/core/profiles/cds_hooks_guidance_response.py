# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class CDSHooksGuidanceResponse:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    request_identifier: Identifier
    identifier: Identifier
    module: CDSHooksGuidanceResponse_ModuleX
    status: CDSHooksGuidanceResponse_StatusCode
    subject: Reference
    encounter: Reference
    occurrence_date_time: DateTime
    performer: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    note: Annotation
    evaluation_message: Reference
    output_parameters: Reference
    result: Reference
    data_requirement: DataRequirement
    cds_hooks_endpoint: Uri


@dataclass
class CDSHooksGuidanceResponse_ModuleX:
    uri: Uri


@dataclass
class CDSHooksGuidanceResponse_StatusCode:
    value: GuidanceResponseStatusCode_Value
    id: String
    extension: Extension

