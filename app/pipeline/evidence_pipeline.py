from app.pipeline.pipeline_result import PipelineResult

from app.pipeline.stages.ai_stage import AIStage
from app.pipeline.stages.event_classification_stage import EventClassificationStage
from app.pipeline.stages.intelligence_stage import IntelligenceStage
from app.pipeline.stages.signal_stage import SignalStage
from app.pipeline.stages.importance_stage import ImportanceStage
from app.pipeline.stages.catalyst_stage import CatalystStage
from app.pipeline.stages.risk_stage import RiskStage
from app.pipeline.stages.decision_stage import DecisionStage
from app.pipeline.stages.notification_stage import NotificationStage


class EvidencePipeline:

    def __init__(self):

        self.stages = [

            AIStage(),

            EventClassificationStage(),

            IntelligenceStage(),

            SignalStage(),

            ImportanceStage(),

            CatalystStage(),

            RiskStage(),

            DecisionStage(),

            NotificationStage()

        ]

    def process(self, evidence):

        result = PipelineResult()

        result.evidence = evidence

        for stage in self.stages:

            result = stage.process(result)

        return result