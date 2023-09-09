# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Subscription:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    status: Subscription_StatusCode
    contact: ContactPoint
    end: Instant
    reason: String
    criteria: String
    error: String
    channel: Subscription_Channel


@dataclass
class Subscription_StatusCode:
    value: SubscriptionStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Subscription_Channel:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: Subscription_Channel_TypeCode
    endpoint: Url
    payload: Subscription_Channel_PayloadCode
    header: String


@dataclass
class Subscription_Channel_TypeCode:
    value: SubscriptionChannelTypeCode_Value
    id: String
    extension: Extension


@dataclass
class Subscription_Channel_PayloadCode:
    id: String
    extension: Extension
    value: str

