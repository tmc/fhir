# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class VisionPrescription:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: VisionPrescription_StatusCode
    created: DateTime
    patient: Reference
    encounter: Reference
    date_written: DateTime
    prescriber: Reference
    lens_specification: VisionPrescription_LensSpecification


@dataclass
class VisionPrescription_StatusCode:
    value: FinancialResourceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class VisionPrescription_LensSpecification:
    id: String
    extension: Extension
    modifier_extension: Extension
    product: CodeableConcept
    eye: VisionPrescription_LensSpecification_EyeCode
    sphere: Decimal
    cylinder: Decimal
    axis: Integer
    prism: VisionPrescription_LensSpecification_Prism
    add: Decimal
    power: Decimal
    back_curve: Decimal
    diameter: Decimal
    duration: SimpleQuantity
    color: String
    brand: String
    note: Annotation


@dataclass
class VisionPrescription_LensSpecification_EyeCode:
    value: VisionEyesCode_Value
    id: String
    extension: Extension


@dataclass
class VisionPrescription_LensSpecification_Prism:
    id: String
    extension: Extension
    modifier_extension: Extension
    amount: Decimal
    base: VisionPrescription_LensSpecification_Prism_BaseCode


@dataclass
class VisionPrescription_LensSpecification_Prism_BaseCode:
    value: VisionBaseCode_Value
    id: String
    extension: Extension

