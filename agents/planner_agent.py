from groq import Groq
from core.models import ResearchQuery, SearchPlan
from core.tracer import Tracer
from dotenv import load_dotenv
import json

load_dotenv()
client = Groq()


def run(query: ResearchQuery, tracer: Tracer) -> SearchPlan:
    tracer.log("planner_agent", "started", {"question": query.question})

    prompt = f"""You are a research planning agent. Break this research question into 2-3
focused sub-queries suitable for searching Wikipedia and arXiv.

Question: {query.question}

Respond ONLY with valid JSON:
{{
  "sub_queries": ["query 1", "query 2", "query 3"],
  "reasoning": "one sentence on why you chose these sub-queries"
}}"""

    resp = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
    )
    data = json.loads(resp.choices[0].message.content)
    plan = SearchPlan(**data)
    tracer.log("planner_agent", "completed", {"sub_queries": plan.sub_queries})
    return plan
