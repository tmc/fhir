# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ComputablePlanDefinition:
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
    status: ComputablePlanDefinition_StatusCode
    experimental: Boolean
    subject: ComputablePlanDefinition_SubjectX
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
    goal: ComputablePlanDefinition_Goal
    action: ComputablePlanDefinition_Action


@dataclass
class ComputablePlanDefinition_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ComputablePlanDefinition_SubjectX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class ComputablePlanDefinition_Goal:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    description: CodeableConcept
    priority: CodeableConcept
    start: CodeableConcept
    addresses: CodeableConcept
    documentation: RelatedArtifact
    target: ComputablePlanDefinition_Goal_Target


@dataclass
class ComputablePlanDefinition_Goal_Target:
    id: String
    extension: Extension
    modifier_extension: Extension
    measure: CodeableConcept
    detail: ComputablePlanDefinition_Goal_Target_DetailX
    due: Duration


@dataclass
class ComputablePlanDefinition_Goal_Target_DetailX:
    quantity: Quantity
    range: Range
    codeable_concept: CodeableConcept


@dataclass
class ComputablePlanDefinition_Action:
    id: String
    extension: Extension
    modifier_extension: Extension
    prefix: String
    title: String
    description: String
    text_equivalent: String
    priority: ComputablePlanDefinition_Action_PriorityCode
    code: CodeableConcept
    reason: CodeableConcept
    documentation: RelatedArtifact
    goal_id: Id
    subject: ComputablePlanDefinition_Action_SubjectX
    trigger: TriggerDefinition
    condition: ComputablePlanDefinition_Action_Condition
    input: DataRequirement
    output: DataRequirement
    related_action: ComputablePlanDefinition_Action_RelatedAction
    timing: ComputablePlanDefinition_Action_TimingX
    participant: ComputablePlanDefinition_Action_Participant
    type: CodeableConcept
    grouping_behavior: ComputablePlanDefinition_Action_GroupingBehaviorCode
    selection_behavior: ComputablePlanDefinition_Action_SelectionBehaviorCode
    required_behavior: ComputablePlanDefinition_Action_RequiredBehaviorCode
    precheck_behavior: ComputablePlanDefinition_Action_PrecheckBehaviorCode
    cardinality_behavior: ComputablePlanDefinition_Action_CardinalityBehaviorCode
    definition: ComputablePlanDefinition_Action_DefinitionX
    transform: Canonical
    dynamic_value: ComputablePlanDefinition_Action_DynamicValue
    action: ComputablePlanDefinition_Action


@dataclass
class ComputablePlanDefinition_Action_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class ComputablePlanDefinition_Action_SubjectX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class ComputablePlanDefinition_Action_Condition:
    id: String
    extension: Extension
    modifier_extension: Extension
    kind: ComputablePlanDefinition_Action_Condition_KindCode
    expression: Expression


@dataclass
class ComputablePlanDefinition_Action_Condition_KindCode:
    value: ActionConditionKindCode_Value
    id: String
    extension: Extension


@dataclass
class ComputablePlanDefinition_Action_RelatedAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    action_id: Id
    relationship: ComputablePlanDefinition_Action_RelatedAction_RelationshipCode
    offset: ComputablePlanDefinition_Action_RelatedAction_OffsetX


@dataclass
class ComputablePlanDefinition_Action_RelatedAction_RelationshipCode:
    value: ActionRelationshipTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ComputablePlanDefinition_Action_RelatedAction_OffsetX:
    duration: Duration
    range: Range


@dataclass
class ComputablePlanDefinition_Action_TimingX:
    date_time: DateTime
    age: Age
    period: Period
    duration: Duration
    range: Range
    timing: Timing


@dataclass
class ComputablePlanDefinition_Action_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ComputablePlanDefinition_Action_Participant_TypeCode
    role: CodeableConcept


@dataclass
class ComputablePlanDefinition_Action_Participant_TypeCode:
    value: ActionParticipantTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ComputablePlanDefinition_Action_GroupingBehaviorCode:
    value: ActionGroupingBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class ComputablePlanDefinition_Action_SelectionBehaviorCode:
    value: ActionSelectionBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class ComputablePlanDefinition_Action_RequiredBehaviorCode:
    value: ActionRequiredBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class ComputablePlanDefinition_Action_PrecheckBehaviorCode:
    value: ActionPrecheckBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class ComputablePlanDefinition_Action_CardinalityBehaviorCode:
    value: ActionCardinalityBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class ComputablePlanDefinition_Action_DefinitionX:
    canonical: Canonical
    uri: Uri


@dataclass
class ComputablePlanDefinition_Action_DynamicValue:
    id: String
    extension: Extension
    modifier_extension: Extension
    path: String
    expression: Expression

