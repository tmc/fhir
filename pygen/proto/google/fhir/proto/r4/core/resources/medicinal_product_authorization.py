# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MedicinalProductAuthorization:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    subject: Reference
    country: CodeableConcept
    jurisdiction: CodeableConcept
    status: CodeableConcept
    status_date: DateTime
    restore_date: DateTime
    validity_period: Period
    data_exclusivity_period: Period
    date_of_first_authorization: DateTime
    international_birth_date: DateTime
    legal_basis: CodeableConcept
    jurisdictional_authorization: MedicinalProductAuthorization_JurisdictionalAuthorization
    holder: Reference
    regulator: Reference
    procedure: MedicinalProductAuthorization_Procedure


@dataclass
class MedicinalProductAuthorization_JurisdictionalAuthorization:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    country: CodeableConcept
    jurisdiction: CodeableConcept
    legal_status_of_supply: CodeableConcept
    validity_period: Period


@dataclass
class MedicinalProductAuthorization_Procedure:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    type: CodeableConcept
    date: MedicinalProductAuthorization_Procedure_DateX
    application: MedicinalProductAuthorization_Procedure


@dataclass
class MedicinalProductAuthorization_Procedure_DateX:
    period: Period
    date_time: DateTime

