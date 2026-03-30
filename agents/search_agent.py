from core.models import SearchPlan, Source
from core.tracer import Tracer
from tools import wikipedia_tool, arxiv_tool


def run(plan: SearchPlan, tracer: Tracer) -> list[Source]:
    tracer.log("search_agent", "started", {"num_queries": len(plan.sub_queries)})
    sources = []

    for query in plan.sub_queries:
        wiki = wikipedia_tool.search(query)
        if wiki["snippet"] and wiki["snippet"] != "No result found.":
            sources.append(Source(**wiki))

        if len(sources) < 4:
            papers = arxiv_tool.search(query, max_results=1)
            for paper in papers:
                sources.append(Source(**paper))

    tracer.log("search_agent", "completed", {"sources_found": len(sources)})
    return sources[:6]
