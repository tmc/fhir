# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class InsurancePlan:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: InsurancePlan_StatusCode
    type: CodeableConcept
    name: String
    alias: String
    period: Period
    owned_by: Reference
    administered_by: Reference
    coverage_area: Reference
    contact: InsurancePlan_Contact
    endpoint: Reference
    network: Reference
    coverage: InsurancePlan_Coverage
    plan: InsurancePlan_Plan


@dataclass
class InsurancePlan_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class InsurancePlan_Contact:
    id: String
    extension: Extension
    modifier_extension: Extension
    purpose: CodeableConcept
    name: HumanName
    telecom: ContactPoint
    address: Address


@dataclass
class InsurancePlan_Coverage:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    network: Reference
    benefit: InsurancePlan_Coverage_CoverageBenefit


@dataclass
class InsurancePlan_Coverage_CoverageBenefit:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    requirement: String
    limit: InsurancePlan_Coverage_CoverageBenefit_Limit


@dataclass
class InsurancePlan_Coverage_CoverageBenefit_Limit:
    id: String
    extension: Extension
    modifier_extension: Extension
    value: Quantity
    code: CodeableConcept


@dataclass
class InsurancePlan_Plan:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    type: CodeableConcept
    coverage_area: Reference
    network: Reference
    general_cost: InsurancePlan_Plan_GeneralCost
    specific_cost: InsurancePlan_Plan_SpecificCost


@dataclass
class InsurancePlan_Plan_GeneralCost:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    group_size: PositiveInt
    cost: Money
    comment: String


@dataclass
class InsurancePlan_Plan_SpecificCost:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    benefit: InsurancePlan_Plan_SpecificCost_PlanBenefit


@dataclass
class InsurancePlan_Plan_SpecificCost_PlanBenefit:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    cost: InsurancePlan_Plan_SpecificCost_PlanBenefit_Cost


@dataclass
class InsurancePlan_Plan_SpecificCost_PlanBenefit_Cost:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    applicability: CodeableConcept
    qualifiers: CodeableConcept
    value: Quantity

