# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MedicinalProductPharmaceutical:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    administrable_dose_form: CodeableConcept
    unit_of_presentation: CodeableConcept
    ingredient: Reference
    device: Reference
    characteristics: MedicinalProductPharmaceutical_Characteristics
    route_of_administration: MedicinalProductPharmaceutical_RouteOfAdministration


@dataclass
class MedicinalProductPharmaceutical_Characteristics:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    status: CodeableConcept


@dataclass
class MedicinalProductPharmaceutical_RouteOfAdministration:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    first_dose: Quantity
    max_single_dose: Quantity
    max_dose_per_day: Quantity
    max_dose_per_treatment_period: Ratio
    max_treatment_period: Duration
    target_species: MedicinalProductPharmaceutical_RouteOfAdministration_TargetSpecies


@dataclass
class MedicinalProductPharmaceutical_RouteOfAdministration_TargetSpecies:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    withdrawal_period: MedicinalProductPharmaceutical_RouteOfAdministration_TargetSpecies_WithdrawalPeriod


@dataclass
class MedicinalProductPharmaceutical_RouteOfAdministration_TargetSpecies_WithdrawalPeriod:
    id: String
    extension: Extension
    modifier_extension: Extension
    tissue: CodeableConcept
    value: Quantity
    supporting_information: String

