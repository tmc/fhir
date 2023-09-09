# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.stu3.fhirproto
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
class Base64BinarySeparatorStride:
    id: String
    separator: String
    stride: PositiveInt

