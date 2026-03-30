from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class TraceEvent:
    agent: str
    event: str
    data: Any = None
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())


class Tracer:
    def __init__(self):
        self.events: list[TraceEvent] = []

    def log(self, agent: str, event: str, data: Any = None):
        self.events.append(TraceEvent(agent=agent, event=event, data=data))

    def summary(self):
        return [{"agent": e.agent, "event": e.event, "ts": e.timestamp} for e in self.events]
