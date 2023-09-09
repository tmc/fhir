# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.stu3.proto
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class AbstractTypeCode:
    value: AbstractTypeCode_Value
    id: String
    extension: Extension


@dataclass
class AggregationModeCode:
    value: AggregationModeCode_Value
    id: String
    extension: Extension


@dataclass
class BindingStrengthCode:
    value: BindingStrengthCode_Value
    id: String
    extension: Extension


@dataclass
class ConstraintSeverityCode:
    value: ConstraintSeverityCode_Value
    id: String
    extension: Extension


@dataclass
class SlicingRulesCode:
    value: SlicingRulesCode_Value
    id: String
    extension: Extension


@dataclass
class DiscriminatorTypeCode:
    value: DiscriminatorTypeCode_Value
    id: String
    extension: Extension


@dataclass
class PropertyRepresentationCode:
    value: PropertyRepresentationCode_Value
    id: String
    extension: Extension


@dataclass
class ReferenceVersionRulesCode:
    value: ReferenceVersionRulesCode_Value
    id: String
    extension: Extension


@dataclass
class AccountStatusCode:
    value: AccountStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ActionCardinalityBehaviorCode:
    value: ActionCardinalityBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class ActionConditionKindCode:
    value: ActionConditionKindCode_Value
    id: String
    extension: Extension


@dataclass
class ActionGroupingBehaviorCode:
    value: ActionGroupingBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class ActionListCode:
    value: ActionListCode_Value
    id: String
    extension: Extension


@dataclass
class ActionParticipantTypeCode:
    value: ActionParticipantTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ActionPrecheckBehaviorCode:
    value: ActionPrecheckBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class ActionRelationshipTypeCode:
    value: ActionRelationshipTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ActionRequiredBehaviorCode:
    value: ActionRequiredBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class ActionSelectionBehaviorCode:
    value: ActionSelectionBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class ActionTypeCode:
    value: ActionTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ActivityDefinitionCategoryCode:
    value: ActivityDefinitionCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class AdministrativeGenderCode:
    value: AdministrativeGenderCode_Value
    id: String
    extension: Extension


@dataclass
class AdverseEventCategoryCode:
    value: AdverseEventCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class AdverseEventCausalityAssessmentCode:
    value: AdverseEventCausalityAssessmentCode_Value
    id: String
    extension: Extension


@dataclass
class AdverseEventCausalityCode:
    value: AdverseEventCausalityCode_Value
    id: String
    extension: Extension


@dataclass
class AdverseEventCausalityMethodCode:
    value: AdverseEventCausalityMethodCode_Value
    id: String
    extension: Extension


@dataclass
class AdverseEventCausalityResultCode:
    value: AdverseEventCausalityResultCode_Value
    id: String
    extension: Extension


@dataclass
class AdverseEventOutcomeCode:
    value: AdverseEventOutcomeCode_Value
    id: String
    extension: Extension


@dataclass
class AdverseEventSeriousnessCode:
    value: AdverseEventSeriousnessCode_Value
    id: String
    extension: Extension


@dataclass
class AllergyIntoleranceSubstanceExposureRiskCode:
    value: AllergyIntoleranceSubstanceExposureRiskCode_Value
    id: String
    extension: Extension


@dataclass
class AllergyIntoleranceClinicalStatusCode:
    value: AllergyIntoleranceClinicalStatusCode_Value
    id: String
    extension: Extension


@dataclass
class AllergyIntoleranceCategoryCode:
    value: AllergyIntoleranceCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class AllergyIntoleranceCriticalityCode:
    value: AllergyIntoleranceCriticalityCode_Value
    id: String
    extension: Extension


@dataclass
class AllergyIntoleranceTypeCode:
    value: AllergyIntoleranceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class AllergyIntoleranceVerificationStatusCode:
    value: AllergyIntoleranceVerificationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class GenderStatusCode:
    value: GenderStatusCode_Value
    id: String
    extension: Extension


@dataclass
class AppointmentStatusCode:
    value: AppointmentStatusCode_Value
    id: String
    extension: Extension


@dataclass
class AssertionDirectionTypeCode:
    value: AssertionDirectionTypeCode_Value
    id: String
    extension: Extension


@dataclass
class AssertionOperatorTypeCode:
    value: AssertionOperatorTypeCode_Value
    id: String
    extension: Extension


@dataclass
class AssertionResponseTypesCode:
    value: AssertionResponseTypesCode_Value
    id: String
    extension: Extension


@dataclass
class AuditEventActionCode:
    value: AuditEventActionCode_Value
    id: String
    extension: Extension


@dataclass
class AuditEventOutcomeCode:
    value: AuditEventOutcomeCode_Value
    id: String
    extension: Extension


@dataclass
class BasicResourceTypesCode:
    value: BasicResourceTypesCode_Value
    id: String
    extension: Extension


@dataclass
class BundleTypeCode:
    value: BundleTypeCode_Value
    id: String
    extension: Extension


@dataclass
class CapabilityStatementKindCode:
    value: CapabilityStatementKindCode_Value
    id: String
    extension: Extension


@dataclass
class CarePlanActivityCategoryCode:
    value: CarePlanActivityCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class CarePlanActivityStatusCode:
    value: CarePlanActivityStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CarePlanIntentCode:
    value: CarePlanIntentCode_Value
    id: String
    extension: Extension


@dataclass
class CarePlanStatusCode:
    value: CarePlanStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CareTeamCategoryCode:
    value: CareTeamCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class CareTeamStatusCode:
    value: CareTeamStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ChargeItemStatusCode:
    value: ChargeItemStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ChoiceListOrientationCode:
    value: ChoiceListOrientationCode_Value
    id: String
    extension: Extension


@dataclass
class UseCode:
    value: UseCode_Value
    id: String
    extension: Extension


@dataclass
class ClassificationOrContextCode:
    value: ClassificationOrContextCode_Value
    id: String
    extension: Extension


@dataclass
class ClinicalImpressionStatusCode:
    value: ClinicalImpressionStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CodeSystemContentModeCode:
    value: CodeSystemContentModeCode_Value
    id: String
    extension: Extension


@dataclass
class CodeSystemHierarchyMeaningCode:
    value: CodeSystemHierarchyMeaningCode_Value
    id: String
    extension: Extension


@dataclass
class CommonTagsCode:
    value: CommonTagsCode_Value
    id: String
    extension: Extension


@dataclass
class CommunicationCategoryCode:
    value: CommunicationCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class CommunicationNotDoneReasonCode:
    value: CommunicationNotDoneReasonCode_Value
    id: String
    extension: Extension


@dataclass
class CompartmentTypeCode:
    value: CompartmentTypeCode_Value
    id: String
    extension: Extension


@dataclass
class CompositeMeasureScoringCode:
    value: CompositeMeasureScoringCode_Value
    id: String
    extension: Extension


@dataclass
class CompositionAttestationModeCode:
    value: CompositionAttestationModeCode_Value
    id: String
    extension: Extension


@dataclass
class CompositionStatusCode:
    value: CompositionStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ConceptMapEquivalenceCode:
    value: ConceptMapEquivalenceCode_Value
    id: String
    extension: Extension


@dataclass
class ConceptMapGroupUnmappedModeCode:
    value: ConceptMapGroupUnmappedModeCode_Value
    id: String
    extension: Extension


@dataclass
class PropertyTypeCode:
    value: PropertyTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ConditionalDeleteStatusCode:
    value: ConditionalDeleteStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ConditionalReadStatusCode:
    value: ConditionalReadStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ConditionCategoryCodesCode:
    value: ConditionCategoryCodesCode_Value
    id: String
    extension: Extension


@dataclass
class ConditionClinicalStatusCodesCode:
    value: ConditionClinicalStatusCodesCode_Value
    id: String
    extension: Extension


@dataclass
class ConditionStateCode:
    value: ConditionStateCode_Value
    id: String
    extension: Extension


@dataclass
class ConditionVerificationStatusCode:
    value: ConditionVerificationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ConformanceExpectationCode:
    value: ConformanceExpectationCode_Value
    id: String
    extension: Extension


@dataclass
class ConsentDataMeaningCode:
    value: ConsentDataMeaningCode_Value
    id: String
    extension: Extension


@dataclass
class ConsentExceptTypeCode:
    value: ConsentExceptTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ConsentStateCode:
    value: ConsentStateCode_Value
    id: String
    extension: Extension


@dataclass
class ContactEntityTypeCode:
    value: ContactEntityTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ContentTypeCode:
    value: ContentTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ContractResourceStatusCode:
    value: ContractResourceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ContributorTypeCode:
    value: ContributorTypeCode_Value
    id: String
    extension: Extension


@dataclass
class CopyNumberEventCode:
    value: CopyNumberEventCode_Value
    id: String
    extension: Extension


@dataclass
class DataAbsentReasonCode:
    value: DataAbsentReasonCode_Value
    id: String
    extension: Extension


@dataclass
class DataElementStringencyCode:
    value: DataElementStringencyCode_Value
    id: String
    extension: Extension


@dataclass
class TriggerTypeCode:
    value: TriggerTypeCode_Value
    id: String
    extension: Extension


@dataclass
class DataTypeCode:
    value: DataTypeCode_Value
    id: String
    extension: Extension


@dataclass
class FHIRAllTypesCode:
    value: FHIRAllTypesCode_Value
    id: String
    extension: Extension


@dataclass
class FHIRDefinedTypeCode:
    value: FHIRDefinedTypeCode_Value
    id: String
    extension: Extension


@dataclass
class FHIRDefinedTypeExtCode:
    value: str
    id: String
    extension: Extension


@dataclass
class DefinitionStatusCode:
    value: DefinitionStatusCode_Value
    id: String
    extension: Extension


@dataclass
class DefinitionTopicCode:
    value: DefinitionTopicCode_Value
    id: String
    extension: Extension


@dataclass
class DetectedIssueSeverityCode:
    value: DetectedIssueSeverityCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceUseStatementStatusCode:
    value: DeviceUseStatementStatusCode_Value
    id: String
    extension: Extension


@dataclass
class FHIRDeviceStatusCode:
    value: FHIRDeviceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class DiagnosisRoleCode:
    value: DiagnosisRoleCode_Value
    id: String
    extension: Extension


@dataclass
class DiagnosticReportStatusCode:
    value: DiagnosticReportStatusCode_Value
    id: String
    extension: Extension


@dataclass
class DigitalMediaTypeCode:
    value: DigitalMediaTypeCode_Value
    id: String
    extension: Extension


@dataclass
class DocumentModeCode:
    value: DocumentModeCode_Value
    id: String
    extension: Extension


@dataclass
class DocumentReferenceStatusCode:
    value: DocumentReferenceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class DocumentRelationshipTypeCode:
    value: DocumentRelationshipTypeCode_Value
    id: String
    extension: Extension


@dataclass
class AdmitSourceCode:
    value: AdmitSourceCode_Value
    id: String
    extension: Extension


@dataclass
class DietCode:
    value: DietCode_Value
    id: String
    extension: Extension


@dataclass
class DischargeDispositionCode:
    value: DischargeDispositionCode_Value
    id: String
    extension: Extension


@dataclass
class EncounterLocationStatusCode:
    value: EncounterLocationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class SpecialArrangementsCode:
    value: SpecialArrangementsCode_Value
    id: String
    extension: Extension


@dataclass
class EncounterStatusCode:
    value: EncounterStatusCode_Value
    id: String
    extension: Extension


@dataclass
class EncounterTypeCode:
    value: EncounterTypeCode_Value
    id: String
    extension: Extension


@dataclass
class EndpointStatusCode:
    value: EndpointStatusCode_Value
    id: String
    extension: Extension


@dataclass
class EntityNamePartQualifierCode:
    value: EntityNamePartQualifierCode_Value
    id: String
    extension: Extension


@dataclass
class EnteralFormulaAdditiveTypeCodeCode:
    value: EnteralFormulaAdditiveTypeCodeCode_Value
    id: String
    extension: Extension


@dataclass
class EpisodeOfCareStatusCode:
    value: EpisodeOfCareStatusCode_Value
    id: String
    extension: Extension


@dataclass
class EpisodeOfCareTypeCode:
    value: EpisodeOfCareTypeCode_Value
    id: String
    extension: Extension


@dataclass
class EventCapabilityModeCode:
    value: EventCapabilityModeCode_Value
    id: String
    extension: Extension


@dataclass
class EventStatusCode:
    value: EventStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ClaimPayeeResourceTypeCode:
    value: ClaimPayeeResourceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ExplanationOfBenefitStatusCode:
    value: ExplanationOfBenefitStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ExtensionContextCode:
    value: ExtensionContextCode_Value
    id: String
    extension: Extension


@dataclass
class FilterOperatorCode:
    value: FilterOperatorCode_Value
    id: String
    extension: Extension


@dataclass
class FlagCategoryCode:
    value: FlagCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class FlagPriorityCodesCode:
    value: FlagPriorityCodesCode_Value
    id: String
    extension: Extension


@dataclass
class FlagStatusCode:
    value: FlagStatusCode_Value
    id: String
    extension: Extension


@dataclass
class FinancialResourceStatusCode:
    value: FinancialResourceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class GoalAcceptanceStatusCode:
    value: GoalAcceptanceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class GoalCategoryCode:
    value: GoalCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class GoalPriorityCode:
    value: GoalPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class GoalRelationshipTypeCode:
    value: GoalRelationshipTypeCode_Value
    id: String
    extension: Extension


@dataclass
class GoalStatusCode:
    value: GoalStatusCode_Value
    id: String
    extension: Extension


@dataclass
class GoalStatusReasonCode:
    value: GoalStatusReasonCode_Value
    id: String
    extension: Extension


@dataclass
class GraphCompartmentRuleCode:
    value: GraphCompartmentRuleCode_Value
    id: String
    extension: Extension


@dataclass
class GroupTypeCode:
    value: GroupTypeCode_Value
    id: String
    extension: Extension


@dataclass
class GuidanceResponseStatusCode:
    value: GuidanceResponseStatusCode_Value
    id: String
    extension: Extension


@dataclass
class GuideDependencyTypeCode:
    value: GuideDependencyTypeCode_Value
    id: String
    extension: Extension


@dataclass
class GuidePageKindCode:
    value: GuidePageKindCode_Value
    id: String
    extension: Extension


@dataclass
class FamilyHistoryNotDoneReasonCode:
    value: FamilyHistoryNotDoneReasonCode_Value
    id: String
    extension: Extension


@dataclass
class FamilyHistoryStatusCode:
    value: FamilyHistoryStatusCode_Value
    id: String
    extension: Extension


@dataclass
class HL7WorkgroupCode:
    value: HL7WorkgroupCode_Value
    id: String
    extension: Extension


@dataclass
class TestScriptRequestMethodCodeCode:
    value: TestScriptRequestMethodCodeCode_Value
    id: String
    extension: Extension


@dataclass
class HTTPVerbCode:
    value: HTTPVerbCode_Value
    id: String
    extension: Extension


@dataclass
class IdentityAssuranceLevelCode:
    value: IdentityAssuranceLevelCode_Value
    id: String
    extension: Extension


@dataclass
class ImmunizationOriginCodesCode:
    value: ImmunizationOriginCodesCode_Value
    id: String
    extension: Extension


@dataclass
class ImmunizationRecommendationDateCriterionCodesCode:
    value: ImmunizationRecommendationDateCriterionCodesCode_Value
    id: String
    extension: Extension


@dataclass
class ImmunizationRecommendationStatusCodesCode:
    value: ImmunizationRecommendationStatusCodesCode_Value
    id: String
    extension: Extension


@dataclass
class ImmunizationStatusCodesCode:
    value: ImmunizationStatusCodesCode_Value
    id: String
    extension: Extension


@dataclass
class ImplantStatusCode:
    value: ImplantStatusCode_Value
    id: String
    extension: Extension


@dataclass
class InstanceAvailabilityCode:
    value: InstanceAvailabilityCode_Value
    id: String
    extension: Extension


@dataclass
class IssueSeverityCode:
    value: IssueSeverityCode_Value
    id: String
    extension: Extension


@dataclass
class IssueTypeCode:
    value: IssueTypeCode_Value
    id: String
    extension: Extension


@dataclass
class QuestionnaireItemTypeCode:
    value: QuestionnaireItemTypeCode_Value
    id: String
    extension: Extension


@dataclass
class LibraryTypeCode:
    value: LibraryTypeCode_Value
    id: String
    extension: Extension


@dataclass
class LinkageTypeCode:
    value: LinkageTypeCode_Value
    id: String
    extension: Extension


@dataclass
class LinkTypeCode:
    value: LinkTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ListEmptyReasonsCode:
    value: ListEmptyReasonsCode_Value
    id: String
    extension: Extension


@dataclass
class ExampleUseCodesforListCode:
    value: ExampleUseCodesforListCode_Value
    id: String
    extension: Extension


@dataclass
class ListModeCode:
    value: ListModeCode_Value
    id: String
    extension: Extension


@dataclass
class ListOrderCodesCode:
    value: ListOrderCodesCode_Value
    id: String
    extension: Extension


@dataclass
class ListStatusCode:
    value: ListStatusCode_Value
    id: String
    extension: Extension


@dataclass
class LocationModeCode:
    value: LocationModeCode_Value
    id: String
    extension: Extension


@dataclass
class LocationTypeCode:
    value: LocationTypeCode_Value
    id: String
    extension: Extension


@dataclass
class LocationStatusCode:
    value: LocationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ProbabilityDistributionTypeCode:
    value: ProbabilityDistributionTypeCode_Value
    id: String
    extension: Extension


@dataclass
class StructureMapContextTypeCode:
    value: StructureMapContextTypeCode_Value
    id: String
    extension: Extension


@dataclass
class StructureMapGroupTypeModeCode:
    value: StructureMapGroupTypeModeCode_Value
    id: String
    extension: Extension


@dataclass
class StructureMapInputModeCode:
    value: StructureMapInputModeCode_Value
    id: String
    extension: Extension


@dataclass
class StructureMapModelModeCode:
    value: StructureMapModelModeCode_Value
    id: String
    extension: Extension


@dataclass
class StructureMapSourceListModeCode:
    value: StructureMapSourceListModeCode_Value
    id: String
    extension: Extension


@dataclass
class StructureMapTargetListModeCode:
    value: StructureMapTargetListModeCode_Value
    id: String
    extension: Extension


@dataclass
class StructureMapTransformCode:
    value: StructureMapTransformCode_Value
    id: String
    extension: Extension


@dataclass
class MatchGradeCode:
    value: MatchGradeCode_Value
    id: String
    extension: Extension


@dataclass
class MeasureDataUsageCode:
    value: MeasureDataUsageCode_Value
    id: String
    extension: Extension


@dataclass
class MeasmntPrincipleCode:
    value: MeasmntPrincipleCode_Value
    id: String
    extension: Extension


@dataclass
class MeasurePopulationTypeCode:
    value: MeasurePopulationTypeCode_Value
    id: String
    extension: Extension


@dataclass
class MeasureReportStatusCode:
    value: MeasureReportStatusCode_Value
    id: String
    extension: Extension


@dataclass
class MeasureReportTypeCode:
    value: MeasureReportTypeCode_Value
    id: String
    extension: Extension


@dataclass
class MeasureScoringCode:
    value: MeasureScoringCode_Value
    id: String
    extension: Extension


@dataclass
class MeasureTypeCode:
    value: MeasureTypeCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationAdministrationCategoryCode:
    value: MedicationAdministrationCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationAdministrationStatusCode:
    value: MedicationAdministrationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationDispenseCategoryCode:
    value: MedicationDispenseCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationDispenseStatusCode:
    value: MedicationDispenseStatusCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationContainerCode:
    value: MedicationContainerCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationRequestCategoryCode:
    value: MedicationRequestCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationRequestIntentCode:
    value: MedicationRequestIntentCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationRequestPriorityCode:
    value: MedicationRequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationRequestStatusCode:
    value: MedicationRequestStatusCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationStatementCategoryCode:
    value: MedicationStatementCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationStatementStatusCode:
    value: MedicationStatementStatusCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationStatementTakenCode:
    value: MedicationStatementTakenCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationStatusCode:
    value: MedicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class MessageEventCode:
    value: MessageEventCode_Value
    id: String
    extension: Extension


@dataclass
class MessageHeaderResponseRequestCode:
    value: MessageHeaderResponseRequestCode_Value
    id: String
    extension: Extension


@dataclass
class ExampleMessageReasonCodesCode:
    value: ExampleMessageReasonCodesCode_Value
    id: String
    extension: Extension


@dataclass
class MessageSignificanceCategoryCode:
    value: MessageSignificanceCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class MessageTransportCode:
    value: MessageTransportCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceMetricCalibrationStateCode:
    value: DeviceMetricCalibrationStateCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceMetricCalibrationTypeCode:
    value: DeviceMetricCalibrationTypeCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceMetricCategoryCode:
    value: DeviceMetricCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceMetricColorCode:
    value: DeviceMetricColorCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceMetricOperationalStatusCode:
    value: DeviceMetricOperationalStatusCode_Value
    id: String
    extension: Extension


@dataclass
class HumanNameAssemblyOrderCode:
    value: HumanNameAssemblyOrderCode_Value
    id: String
    extension: Extension


@dataclass
class NameRepresentationUseCode:
    value: NameRepresentationUseCode_Value
    id: String
    extension: Extension


@dataclass
class NamingSystemIdentifierTypeCode:
    value: NamingSystemIdentifierTypeCode_Value
    id: String
    extension: Extension


@dataclass
class NamingSystemTypeCode:
    value: NamingSystemTypeCode_Value
    id: String
    extension: Extension


@dataclass
class AuditEventAgentNetworkTypeCode:
    value: AuditEventAgentNetworkTypeCode_Value
    id: String
    extension: Extension


@dataclass
class NoteTypeCode:
    value: NoteTypeCode_Value
    id: String
    extension: Extension


@dataclass
class NullFlavorCode:
    value: NullFlavorCode_Value
    id: String
    extension: Extension


@dataclass
class NutritionOrderStatusCode:
    value: NutritionOrderStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ObservationCategoryCodesCode:
    value: ObservationCategoryCodesCode_Value
    id: String
    extension: Extension


@dataclass
class ObservationRelationshipTypeCode:
    value: ObservationRelationshipTypeCode_Value
    id: String
    extension: Extension


@dataclass
class StatisticsCodeCode:
    value: StatisticsCodeCode_Value
    id: String
    extension: Extension


@dataclass
class ObservationStatusCode:
    value: ObservationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceComponentOperationalStatusCode:
    value: DeviceComponentOperationalStatusCode_Value
    id: String
    extension: Extension


@dataclass
class OperationKindCode:
    value: OperationKindCode_Value
    id: String
    extension: Extension


@dataclass
class OperationOutcomeCodesCode:
    value: OperationOutcomeCodesCode_Value
    id: String
    extension: Extension


@dataclass
class NarrativeStatusCode:
    value: NarrativeStatusCode_Value
    id: String
    extension: Extension


@dataclass
class OperationParameterUseCode:
    value: OperationParameterUseCode_Value
    id: String
    extension: Extension


@dataclass
class OrganizationTypeCode:
    value: OrganizationTypeCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceComponentParameterGroupCode:
    value: DeviceComponentParameterGroupCode_Value
    id: String
    extension: Extension


@dataclass
class ParticipantRequiredCode:
    value: ParticipantRequiredCode_Value
    id: String
    extension: Extension


@dataclass
class ParticipationStatusCode:
    value: ParticipationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class PlanDefinitionTypeCode:
    value: PlanDefinitionTypeCode_Value
    id: String
    extension: Extension


@dataclass
class PostalAddressUseTypeCode:
    value: PostalAddressUseTypeCode_Value
    id: String
    extension: Extension


@dataclass
class PractitionerRoleCode:
    value: PractitionerRoleCode_Value
    id: String
    extension: Extension


@dataclass
class PractitionerSpecialtyCode:
    value: PractitionerSpecialtyCode_Value
    id: String
    extension: Extension


@dataclass
class ProcedureProgressStatusCodesCode:
    value: ProcedureProgressStatusCodesCode_Value
    id: String
    extension: Extension


@dataclass
class ProvenanceEntityRoleCode:
    value: ProvenanceEntityRoleCode_Value
    id: String
    extension: Extension


@dataclass
class PublicationStatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class QualityTypeCode:
    value: QualityTypeCode_Value
    id: String
    extension: Extension


@dataclass
class MaxOccursCode:
    value: MaxOccursCode_Value
    id: String
    extension: Extension


@dataclass
class QuestionnaireResponseStatusCode:
    value: QuestionnaireResponseStatusCode_Value
    id: String
    extension: Extension


@dataclass
class QuestionnaireTextCategoriesCode:
    value: QuestionnaireTextCategoriesCode_Value
    id: String
    extension: Extension


@dataclass
class QuestionnaireItemUIControlCodesCode:
    value: QuestionnaireItemUIControlCodesCode_Value
    id: String
    extension: Extension


@dataclass
class QuestionnaireItemUsageModeCode:
    value: QuestionnaireItemUsageModeCode_Value
    id: String
    extension: Extension


@dataclass
class AllergyIntoleranceCertaintyCode:
    value: AllergyIntoleranceCertaintyCode_Value
    id: String
    extension: Extension


@dataclass
class AllergyIntoleranceSeverityCode:
    value: AllergyIntoleranceSeverityCode_Value
    id: String
    extension: Extension


@dataclass
class ReasonMedicationGivenCodesCode:
    value: ReasonMedicationGivenCodesCode_Value
    id: String
    extension: Extension


@dataclass
class ReferenceHandlingPolicyCode:
    value: ReferenceHandlingPolicyCode_Value
    id: String
    extension: Extension


@dataclass
class RelatedArtifactTypeCode:
    value: RelatedArtifactTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ObservationReferenceRangeMeaningCodesCode:
    value: ObservationReferenceRangeMeaningCodesCode_Value
    id: String
    extension: Extension


@dataclass
class TestReportActionResultCode:
    value: TestReportActionResultCode_Value
    id: String
    extension: Extension


@dataclass
class TestReportParticipantTypeCode:
    value: TestReportParticipantTypeCode_Value
    id: String
    extension: Extension


@dataclass
class TestReportResultCode:
    value: TestReportResultCode_Value
    id: String
    extension: Extension


@dataclass
class TestReportStatusCode:
    value: TestReportStatusCode_Value
    id: String
    extension: Extension


@dataclass
class RepositoryTypeCode:
    value: RepositoryTypeCode_Value
    id: String
    extension: Extension


@dataclass
class RequestIntentCode:
    value: RequestIntentCode_Value
    id: String
    extension: Extension


@dataclass
class RequestPriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class RequestStatusCode:
    value: RequestStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ResearchStudyStatusCode:
    value: ResearchStudyStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ResearchSubjectStatusCode:
    value: ResearchSubjectStatusCode_Value
    id: String
    extension: Extension


@dataclass
class PayeeResourceTypeCode:
    value: PayeeResourceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ResourceTypeCode:
    value: ResourceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ResourceValidationModeCode:
    value: ResourceValidationModeCode_Value
    id: String
    extension: Extension


@dataclass
class ResponseTypeCode:
    value: ResponseTypeCode_Value
    id: String
    extension: Extension


@dataclass
class RestfulCapabilityModeCode:
    value: RestfulCapabilityModeCode_Value
    id: String
    extension: Extension


@dataclass
class RestfulSecurityServiceCode:
    value: RestfulSecurityServiceCode_Value
    id: String
    extension: Extension


@dataclass
class RiskProbabilityCode:
    value: RiskProbabilityCode_Value
    id: String
    extension: Extension


@dataclass
class SearchComparatorCode:
    value: SearchComparatorCode_Value
    id: String
    extension: Extension


@dataclass
class SearchEntryModeCode:
    value: SearchEntryModeCode_Value
    id: String
    extension: Extension


@dataclass
class SearchModifierCodeCode:
    value: SearchModifierCodeCode_Value
    id: String
    extension: Extension


@dataclass
class SearchParamTypeCode:
    value: SearchParamTypeCode_Value
    id: String
    extension: Extension


@dataclass
class XPathUsageTypeCode:
    value: XPathUsageTypeCode_Value
    id: String
    extension: Extension


@dataclass
class SequenceTypeCode:
    value: SequenceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ServiceProvisionConditionsCode:
    value: ServiceProvisionConditionsCode_Value
    id: String
    extension: Extension


@dataclass
class ReferralMethodCode:
    value: ReferralMethodCode_Value
    id: String
    extension: Extension


@dataclass
class SlotStatusCode:
    value: SlotStatusCode_Value
    id: String
    extension: Extension


@dataclass
class SpecialValuesCode:
    value: SpecialValuesCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceSpecificationSpecTypeCode:
    value: DeviceSpecificationSpecTypeCode_Value
    id: String
    extension: Extension


@dataclass
class SpecimenStatusCode:
    value: SpecimenStatusCode_Value
    id: String
    extension: Extension


@dataclass
class StructureDefinitionKindCode:
    value: StructureDefinitionKindCode_Value
    id: String
    extension: Extension


@dataclass
class SubscriptionChannelTypeCode:
    value: SubscriptionChannelTypeCode_Value
    id: String
    extension: Extension


@dataclass
class SubscriptionStatusCode:
    value: SubscriptionStatusCode_Value
    id: String
    extension: Extension


@dataclass
class SubscriptionTagCode:
    value: SubscriptionTagCode_Value
    id: String
    extension: Extension


@dataclass
class SubstanceCategoryCodesCode:
    value: SubstanceCategoryCodesCode_Value
    id: String
    extension: Extension


@dataclass
class FHIRSubstanceStatusCode:
    value: FHIRSubstanceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class SupplyDeliveryStatusCode:
    value: SupplyDeliveryStatusCode_Value
    id: String
    extension: Extension


@dataclass
class SupplyItemTypeCode:
    value: SupplyItemTypeCode_Value
    id: String
    extension: Extension


@dataclass
class SupplyTypeCode:
    value: SupplyTypeCode_Value
    id: String
    extension: Extension


@dataclass
class SupplyRequestReasonCode:
    value: SupplyRequestReasonCode_Value
    id: String
    extension: Extension


@dataclass
class SupplyRequestStatusCode:
    value: SupplyRequestStatusCode_Value
    id: String
    extension: Extension


@dataclass
class SystemRestfulInteractionCode:
    value: SystemRestfulInteractionCode_Value
    id: String
    extension: Extension


@dataclass
class SystemVersionProcessingModeCode:
    value: SystemVersionProcessingModeCode_Value
    id: String
    extension: Extension


@dataclass
class TaskPerformerTypeCode:
    value: TaskPerformerTypeCode_Value
    id: String
    extension: Extension


@dataclass
class TemplateStatusCodeCode:
    value: TemplateStatusCodeCode_Value
    id: String
    extension: Extension


@dataclass
class TaskStatusCode:
    value: TaskStatusCode_Value
    id: String
    extension: Extension


@dataclass
class TestScriptOperationCodeCode:
    value: TestScriptOperationCodeCode_Value
    id: String
    extension: Extension


@dataclass
class TestScriptProfileDestinationTypeCode:
    value: TestScriptProfileDestinationTypeCode_Value
    id: String
    extension: Extension


@dataclass
class TestScriptProfileOriginTypeCode:
    value: TestScriptProfileOriginTypeCode_Value
    id: String
    extension: Extension


@dataclass
class TransactionModeCode:
    value: TransactionModeCode_Value
    id: String
    extension: Extension


@dataclass
class TypeDerivationRuleCode:
    value: TypeDerivationRuleCode_Value
    id: String
    extension: Extension


@dataclass
class TypeRestfulInteractionCode:
    value: TypeRestfulInteractionCode_Value
    id: String
    extension: Extension


@dataclass
class UDIEntryTypeCode:
    value: UDIEntryTypeCode_Value
    id: String
    extension: Extension


@dataclass
class UnknownContentCodeCode:
    value: UnknownContentCodeCode_Value
    id: String
    extension: Extension


@dataclass
class UsageContextTypeCode:
    value: UsageContextTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ConfidentialityClassificationCode:
    value: ConfidentialityClassificationCode_Value
    id: String
    extension: Extension


@dataclass
class VaccinationProtocolDoseStatuscodesCode:
    value: VaccinationProtocolDoseStatuscodesCode_Value
    id: String
    extension: Extension


@dataclass
class VaccinationProtocolDoseStatusReasoncodesCode:
    value: VaccinationProtocolDoseStatusReasoncodesCode_Value
    id: String
    extension: Extension


@dataclass
class SequenceStatusCode:
    value: SequenceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ResourceVersionPolicyCode:
    value: ResourceVersionPolicyCode_Value
    id: String
    extension: Extension


@dataclass
class VisionBaseCode:
    value: VisionBaseCode_Value
    id: String
    extension: Extension


@dataclass
class VisionEyesCode:
    value: VisionEyesCode_Value
    id: String
    extension: Extension

