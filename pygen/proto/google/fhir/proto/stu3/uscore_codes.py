# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.stu3.uscore
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class UsCoreBirthSexCode:
    value: UsCoreBirthSexCode_Value
    id: String
    extension: Extension

