# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class CoverageEligibilityRequest:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: CoverageEligibilityRequest_StatusCode
    priority: CodeableConcept
    purpose: CoverageEligibilityRequest_PurposeCode
    patient: Reference
    serviced: CoverageEligibilityRequest_ServicedX
    created: DateTime
    enterer: Reference
    provider: Reference
    insurer: Reference
    facility: Reference
    supporting_info: CoverageEligibilityRequest_SupportingInformation
    insurance: CoverageEligibilityRequest_Insurance
    item: CoverageEligibilityRequest_Details


@dataclass
class CoverageEligibilityRequest_StatusCode:
    value: FinancialResourceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CoverageEligibilityRequest_PurposeCode:
    value: EligibilityRequestPurposeCode_Value
    id: String
    extension: Extension


@dataclass
class CoverageEligibilityRequest_ServicedX:
    date: Date
    period: Period


@dataclass
class CoverageEligibilityRequest_SupportingInformation:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    information: Reference
    applies_to_all: Boolean


@dataclass
class CoverageEligibilityRequest_Insurance:
    id: String
    extension: Extension
    modifier_extension: Extension
    focal: Boolean
    coverage: Reference
    business_arrangement: String


@dataclass
class CoverageEligibilityRequest_Details:
    id: String
    extension: Extension
    modifier_extension: Extension
    supporting_info_sequence: PositiveInt
    category: CodeableConcept
    product_or_service: CodeableConcept
    modifier: CodeableConcept
    provider: Reference
    quantity: SimpleQuantity
    unit_price: Money
    facility: Reference
    diagnosis: CoverageEligibilityRequest_Details_Diagnosis
    detail: Reference


@dataclass
class CoverageEligibilityRequest_Details_Diagnosis:
    id: String
    extension: Extension
    modifier_extension: Extension
    diagnosis: CoverageEligibilityRequest_Details_Diagnosis_DiagnosisX


@dataclass
class CoverageEligibilityRequest_Details_Diagnosis_DiagnosisX:
    codeable_concept: CodeableConcept
    reference: Reference

