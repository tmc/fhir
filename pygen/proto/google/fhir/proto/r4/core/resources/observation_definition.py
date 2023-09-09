# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ObservationDefinition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    code: CodeableConcept
    identifier: Identifier
    permitted_data_type: ObservationDefinition_PermittedDataTypeCode
    multiple_results_allowed: Boolean
    method: CodeableConcept
    preferred_report_name: String
    quantitative_details: ObservationDefinition_QuantitativeDetails
    qualified_interval: ObservationDefinition_QualifiedInterval
    valid_coded_value_set: Reference
    normal_coded_value_set: Reference
    abnormal_coded_value_set: Reference
    critical_coded_value_set: Reference


@dataclass
class ObservationDefinition_PermittedDataTypeCode:
    value: ObservationDataTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ObservationDefinition_QuantitativeDetails:
    id: String
    extension: Extension
    modifier_extension: Extension
    customary_unit: CodeableConcept
    unit: CodeableConcept
    conversion_factor: Decimal
    decimal_precision: Integer


@dataclass
class ObservationDefinition_QualifiedInterval:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: ObservationDefinition_QualifiedInterval_CategoryCode
    range: Range
    context: CodeableConcept
    applies_to: CodeableConcept
    gender: ObservationDefinition_QualifiedInterval_GenderCode
    age: Range
    gestational_age: Range
    condition: String


@dataclass
class ObservationDefinition_QualifiedInterval_CategoryCode:
    value: ObservationRangeCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class ObservationDefinition_QualifiedInterval_GenderCode:
    value: AdministrativeGenderCode_Value
    id: String
    extension: Extension

