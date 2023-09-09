# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Coverage:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: Coverage_StatusCode
    type: CodeableConcept
    policy_holder: Reference
    subscriber: Reference
    subscriber_id: String
    beneficiary: Reference
    dependent: String
    relationship: CodeableConcept
    period: Period
    payor: Reference
    class_value: Coverage_Class
    order: PositiveInt
    network: String
    cost_to_beneficiary: Coverage_CostToBeneficiary
    subrogation: Boolean
    contract: Reference


@dataclass
class Coverage_StatusCode:
    value: FinancialResourceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Coverage_Class:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    value: String
    name: String


@dataclass
class Coverage_CostToBeneficiary:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    value: Coverage_CostToBeneficiary_ValueX
    exception: Coverage_CostToBeneficiary_Exemption


@dataclass
class Coverage_CostToBeneficiary_ValueX:
    quantity: SimpleQuantity
    money: Money


@dataclass
class Coverage_CostToBeneficiary_Exemption:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    period: Period

