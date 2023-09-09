# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ChargeItemDefinition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    title: String
    derived_from_uri: Uri
    part_of: Canonical
    replaces: Canonical
    status: ChargeItemDefinition_StatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    copyright: Markdown
    approval_date: Date
    last_review_date: Date
    effective_period: Period
    code: CodeableConcept
    instance: Reference
    applicability: ChargeItemDefinition_Applicability
    property_group: ChargeItemDefinition_PropertyGroup


@dataclass
class ChargeItemDefinition_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ChargeItemDefinition_Applicability:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    language: String
    expression: String


@dataclass
class ChargeItemDefinition_PropertyGroup:
    id: String
    extension: Extension
    modifier_extension: Extension
    applicability: ChargeItemDefinition_Applicability
    price_component: ChargeItemDefinition_PropertyGroup_PriceComponent


@dataclass
class ChargeItemDefinition_PropertyGroup_PriceComponent:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ChargeItemDefinition_PropertyGroup_PriceComponent_TypeCode
    code: CodeableConcept
    factor: Decimal
    amount: Money


@dataclass
class ChargeItemDefinition_PropertyGroup_PriceComponent_TypeCode:
    value: InvoicePriceComponentTypeCode_Value
    id: String
    extension: Extension

