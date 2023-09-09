# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.proto
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class FHIRPathReplacementList:
    replacement: Replacement


@dataclass
class Replacement:
    element_path: str
    expression_to_replace: str
    replacement_expression: str

