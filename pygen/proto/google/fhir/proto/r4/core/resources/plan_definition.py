# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class PlanDefinition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    subtitle: String
    type: CodeableConcept
    status: PlanDefinition_StatusCode
    experimental: Boolean
    subject: PlanDefinition_SubjectX
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    usage: String
    copyright: Markdown
    approval_date: Date
    last_review_date: Date
    effective_period: Period
    topic: CodeableConcept
    author: ContactDetail
    editor: ContactDetail
    reviewer: ContactDetail
    endorser: ContactDetail
    related_artifact: RelatedArtifact
    library: Canonical
    goal: PlanDefinition_Goal
    action: PlanDefinition_Action


@dataclass
class PlanDefinition_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class PlanDefinition_SubjectX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class PlanDefinition_Goal:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    description: CodeableConcept
    priority: CodeableConcept
    start: CodeableConcept
    addresses: CodeableConcept
    documentation: RelatedArtifact
    target: PlanDefinition_Goal_Target


@dataclass
class PlanDefinition_Goal_Target:
    id: String
    extension: Extension
    modifier_extension: Extension
    measure: CodeableConcept
    detail: PlanDefinition_Goal_Target_DetailX
    due: Duration


@dataclass
class PlanDefinition_Goal_Target_DetailX:
    quantity: Quantity
    range: Range
    codeable_concept: CodeableConcept


@dataclass
class PlanDefinition_Action:
    id: String
    extension: Extension
    modifier_extension: Extension
    prefix: String
    title: String
    description: String
    text_equivalent: String
    priority: PlanDefinition_Action_PriorityCode
    code: CodeableConcept
    reason: CodeableConcept
    documentation: RelatedArtifact
    goal_id: Id
    subject: PlanDefinition_Action_SubjectX
    trigger: TriggerDefinition
    condition: PlanDefinition_Action_Condition
    input: DataRequirement
    output: DataRequirement
    related_action: PlanDefinition_Action_RelatedAction
    timing: PlanDefinition_Action_TimingX
    participant: PlanDefinition_Action_Participant
    type: CodeableConcept
    grouping_behavior: PlanDefinition_Action_GroupingBehaviorCode
    selection_behavior: PlanDefinition_Action_SelectionBehaviorCode
    required_behavior: PlanDefinition_Action_RequiredBehaviorCode
    precheck_behavior: PlanDefinition_Action_PrecheckBehaviorCode
    cardinality_behavior: PlanDefinition_Action_CardinalityBehaviorCode
    definition: PlanDefinition_Action_DefinitionX
    transform: Canonical
    dynamic_value: PlanDefinition_Action_DynamicValue
    action: PlanDefinition_Action


@dataclass
class PlanDefinition_Action_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class PlanDefinition_Action_SubjectX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class PlanDefinition_Action_Condition:
    id: String
    extension: Extension
    modifier_extension: Extension
    kind: PlanDefinition_Action_Condition_KindCode
    expression: Expression


@dataclass
class PlanDefinition_Action_Condition_KindCode:
    value: ActionConditionKindCode_Value
    id: String
    extension: Extension


@dataclass
class PlanDefinition_Action_RelatedAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    action_id: Id
    relationship: PlanDefinition_Action_RelatedAction_RelationshipCode
    offset: PlanDefinition_Action_RelatedAction_OffsetX


@dataclass
class PlanDefinition_Action_RelatedAction_RelationshipCode:
    value: ActionRelationshipTypeCode_Value
    id: String
    extension: Extension


@dataclass
class PlanDefinition_Action_RelatedAction_OffsetX:
    duration: Duration
    range: Range


@dataclass
class PlanDefinition_Action_TimingX:
    date_time: DateTime
    age: Age
    period: Period
    duration: Duration
    range: Range
    timing: Timing


@dataclass
class PlanDefinition_Action_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: PlanDefinition_Action_Participant_TypeCode
    role: CodeableConcept


@dataclass
class PlanDefinition_Action_Participant_TypeCode:
    value: ActionParticipantTypeCode_Value
    id: String
    extension: Extension


@dataclass
class PlanDefinition_Action_GroupingBehaviorCode:
    value: ActionGroupingBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class PlanDefinition_Action_SelectionBehaviorCode:
    value: ActionSelectionBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class PlanDefinition_Action_RequiredBehaviorCode:
    value: ActionRequiredBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class PlanDefinition_Action_PrecheckBehaviorCode:
    value: ActionPrecheckBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class PlanDefinition_Action_CardinalityBehaviorCode:
    value: ActionCardinalityBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class PlanDefinition_Action_DefinitionX:
    canonical: Canonical
    uri: Uri


@dataclass
class PlanDefinition_Action_DynamicValue:
    id: String
    extension: Extension
    modifier_extension: Extension
    path: String
    expression: Expression

