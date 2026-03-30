from core.models import ResearchQuery
from core.tracer import Tracer
from agents import planner_agent, search_agent, synthesis_agent
from rich.console import Console
from rich.panel import Panel

console = Console()


def run(question: str) -> dict:
    tracer = Tracer()
    query = ResearchQuery(question=question)

    console.print(f"\n[bold cyan]Question:[/bold cyan] {question}\n")

    console.print("[bold]1. Planner agent[/bold] — breaking question into sub-queries...")
    plan = planner_agent.run(query, tracer)
    console.print(f"   Sub-queries: {plan.sub_queries}")

    console.print("[bold]2. Search agent[/bold] — fetching sources...")
    sources = search_agent.run(plan, tracer)
    console.print(f"   Found {len(sources)} sources")

    console.print("[bold]3. Synthesis agent[/bold] — writing summary...")
    report = synthesis_agent.run(query, sources, tracer)

    console.print(Panel(report.summary, title="Research Summary", border_style="green"))

    console.print("\n[bold]Sources:[/bold]")
    for i, s in enumerate(report.sources):
        console.print(f"  [{i+1}] [{s.source_type}] {s.title}")
        if s.url:
            console.print(f"       {s.url}")

    return {
        "summary": report.summary,
        "sources": [s.model_dump() for s in report.sources],
        "trace": tracer.summary(),
    }
