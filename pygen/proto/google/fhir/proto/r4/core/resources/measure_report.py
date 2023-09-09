# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MeasureReport:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: MeasureReport_StatusCode
    type: MeasureReport_TypeCode
    measure: Canonical
    subject: Reference
    date: DateTime
    reporter: Reference
    period: Period
    improvement_notation: CodeableConcept
    group: MeasureReport_Group
    evaluated_resource: Reference


@dataclass
class MeasureReport_StatusCode:
    value: MeasureReportStatusCode_Value
    id: String
    extension: Extension


@dataclass
class MeasureReport_TypeCode:
    value: MeasureReportTypeCode_Value
    id: String
    extension: Extension


@dataclass
class MeasureReport_Group:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    population: MeasureReport_Group_Population
    measure_score: Quantity
    stratifier: MeasureReport_Group_Stratifier


@dataclass
class MeasureReport_Group_Population:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    count: Integer
    subject_results: Reference


@dataclass
class MeasureReport_Group_Stratifier:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    stratum: MeasureReport_Group_Stratifier_StratifierGroup


@dataclass
class MeasureReport_Group_Stratifier_StratifierGroup:
    id: String
    extension: Extension
    modifier_extension: Extension
    value: CodeableConcept
    component: MeasureReport_Group_Stratifier_StratifierGroup_Component
    population: MeasureReport_Group_Stratifier_StratifierGroup_StratifierGroupPopulation
    measure_score: Quantity


@dataclass
class MeasureReport_Group_Stratifier_StratifierGroup_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: CodeableConcept


@dataclass
class MeasureReport_Group_Stratifier_StratifierGroup_StratifierGroupPopulation:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    count: Integer
    subject_results: Reference

