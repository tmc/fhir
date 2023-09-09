# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ImmunizationRecommendation:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    patient: Reference
    date: DateTime
    authority: Reference
    recommendation: ImmunizationRecommendation_Recommendation


@dataclass
class ImmunizationRecommendation_Recommendation:
    id: String
    extension: Extension
    modifier_extension: Extension
    vaccine_code: CodeableConcept
    target_disease: CodeableConcept
    contraindicated_vaccine_code: CodeableConcept
    forecast_status: CodeableConcept
    forecast_reason: CodeableConcept
    date_criterion: ImmunizationRecommendation_Recommendation_DateCriterion
    description: String
    series: String
    dose_number: ImmunizationRecommendation_Recommendation_DoseNumberX
    series_doses: ImmunizationRecommendation_Recommendation_SeriesDosesX
    supporting_immunization: Reference
    supporting_patient_information: Reference


@dataclass
class ImmunizationRecommendation_Recommendation_DateCriterion:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: DateTime


@dataclass
class ImmunizationRecommendation_Recommendation_DoseNumberX:
    positive_int: PositiveInt
    string_value: String


@dataclass
class ImmunizationRecommendation_Recommendation_SeriesDosesX:
    positive_int: PositiveInt
    string_value: String

