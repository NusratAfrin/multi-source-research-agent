from groq import Groq
from core.models import ResearchQuery, Source, ResearchReport
from core.tracer import Tracer
from dotenv import load_dotenv

load_dotenv()
client = Groq()


def run(query: ResearchQuery, sources: list[Source], tracer: Tracer) -> ResearchReport:
    tracer.log("synthesis_agent", "started", {"num_sources": len(sources)})

    sources_text = "\n\n".join(
        f"[{i+1}] {s.title} ({s.source_type})\n{s.snippet}"
        for i, s in enumerate(sources)
    )

    prompt = f"""You are a research synthesis agent. Using ONLY the sources below,
write a clear, factual 3-4 paragraph summary answering the research question.
Cite sources using [1], [2] etc. Do not add information not in the sources.

Question: {query.question}

Sources:
{sources_text}"""

    resp = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
    )
    summary = resp.choices[0].message.content
    tracer.log("synthesis_agent", "completed")

    return ResearchReport(question=query.question, summary=summary, sources=sources)
