# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class CoverageEligibilityResponse:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: CoverageEligibilityResponse_StatusCode
    purpose: CoverageEligibilityResponse_PurposeCode
    patient: Reference
    serviced: CoverageEligibilityResponse_ServicedX
    created: DateTime
    requestor: Reference
    request: Reference
    outcome: CoverageEligibilityResponse_OutcomeCode
    disposition: String
    insurer: Reference
    insurance: CoverageEligibilityResponse_Insurance
    pre_auth_ref: String
    form: CodeableConcept
    error: CoverageEligibilityResponse_Errors


@dataclass
class CoverageEligibilityResponse_StatusCode:
    value: FinancialResourceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CoverageEligibilityResponse_PurposeCode:
    value: EligibilityResponsePurposeCode_Value
    id: String
    extension: Extension


@dataclass
class CoverageEligibilityResponse_ServicedX:
    date: Date
    period: Period


@dataclass
class CoverageEligibilityResponse_OutcomeCode:
    value: ClaimProcessingCode_Value
    id: String
    extension: Extension


@dataclass
class CoverageEligibilityResponse_Insurance:
    id: String
    extension: Extension
    modifier_extension: Extension
    coverage: Reference
    inforce: Boolean
    benefit_period: Period
    item: CoverageEligibilityResponse_Insurance_Items


@dataclass
class CoverageEligibilityResponse_Insurance_Items:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    product_or_service: CodeableConcept
    modifier: CodeableConcept
    provider: Reference
    excluded: Boolean
    name: String
    description: String
    network: CodeableConcept
    unit: CodeableConcept
    term: CodeableConcept
    benefit: CoverageEligibilityResponse_Insurance_Items_Benefit
    authorization_required: Boolean
    authorization_supporting: CodeableConcept
    authorization_url: Uri


@dataclass
class CoverageEligibilityResponse_Insurance_Items_Benefit:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    allowed: CoverageEligibilityResponse_Insurance_Items_Benefit_AllowedX
    used: CoverageEligibilityResponse_Insurance_Items_Benefit_UsedX


@dataclass
class CoverageEligibilityResponse_Insurance_Items_Benefit_AllowedX:
    unsigned_int: UnsignedInt
    string_value: String
    money: Money


@dataclass
class CoverageEligibilityResponse_Insurance_Items_Benefit_UsedX:
    unsigned_int: UnsignedInt
    string_value: String
    money: Money


@dataclass
class CoverageEligibilityResponse_Errors:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept

