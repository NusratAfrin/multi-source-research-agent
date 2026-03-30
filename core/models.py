from pydantic import BaseModel
from datetime import datetime


class ResearchQuery(BaseModel):
    question: str
    max_sources: int = 4


class Source(BaseModel):
    title: str
    url: str
    snippet: str
    source_type: str


class SearchPlan(BaseModel):
    sub_queries: list[str]
    reasoning: str


class ResearchReport(BaseModel):
    question: str
    summary: str
    sources: list[Source]
    generated_at: datetime = None

    def model_post_init(self, _):
        if not self.generated_at:
            self.generated_at = datetime.utcnow()
