# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.stu3.ml
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class EventLabel:
    id: String
    extension: Extension
    patient: Reference
    type: Coding
    event_time: DateTime
    source: Reference
    label: EventLabel_Label


@dataclass
class EventLabel_Label:
    id: String
    class_name: Coding
    class_value: EventLabel_Label_ClassValue


@dataclass
class EventLabel_Label_ClassValue:
    boolean: Boolean
    decimal: Decimal
    integer: Integer
    string_value: String
    date_time: DateTime


@dataclass
class EventTrigger:
    id: String
    type: Coding
    event_time: DateTime
    source: Reference

