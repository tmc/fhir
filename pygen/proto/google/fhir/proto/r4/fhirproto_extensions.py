# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.fhirproto
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class PrimitiveHasNoValue:
    id: String
    value_boolean: Boolean


@dataclass
class OperationOutcomeSubject:
    id: String
    value_reference: Reference


@dataclass
class Base64BinarySeparatorStride:
    id: String
    separator: String
    stride: PositiveInt

