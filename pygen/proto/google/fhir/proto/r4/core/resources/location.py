# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Location:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: Location_StatusCode
    operational_status: Coding
    name: String
    alias: String
    description: String
    mode: Location_ModeCode
    type: CodeableConcept
    telecom: ContactPoint
    address: Address
    physical_type: CodeableConcept
    position: Location_Position
    managing_organization: Reference
    part_of: Reference
    hours_of_operation: Location_HoursOfOperation
    availability_exceptions: String
    endpoint: Reference


@dataclass
class Location_StatusCode:
    value: LocationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Location_ModeCode:
    value: LocationModeCode_Value
    id: String
    extension: Extension


@dataclass
class Location_Position:
    id: String
    extension: Extension
    modifier_extension: Extension
    longitude: Decimal
    latitude: Decimal
    altitude: Decimal


@dataclass
class Location_HoursOfOperation:
    id: String
    extension: Extension
    modifier_extension: Extension
    days_of_week: Location_HoursOfOperation_DaysOfWeekCode
    all_day: Boolean
    opening_time: Time
    closing_time: Time


@dataclass
class Location_HoursOfOperation_DaysOfWeekCode:
    value: DaysOfWeekCode_Value
    id: String
    extension: Extension

