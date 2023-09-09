# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class OrganizationAffiliation:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    active: Boolean
    period: Period
    organization: Reference
    participating_organization: Reference
    network: Reference
    code: CodeableConcept
    specialty: CodeableConcept
    location: Reference
    healthcare_service: Reference
    telecom: ContactPoint
    endpoint: Reference

