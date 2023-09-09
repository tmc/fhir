# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Organization:
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
    type: CodeableConcept
    name: String
    alias: String
    telecom: ContactPoint
    address: Address
    part_of: Reference
    contact: Organization_Contact
    endpoint: Reference


@dataclass
class Organization_Contact:
    id: String
    extension: Extension
    modifier_extension: Extension
    purpose: CodeableConcept
    name: HumanName
    telecom: ContactPoint
    address: Address

