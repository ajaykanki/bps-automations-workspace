from pydantic import BaseModel
from typing import Any


class JobResult(BaseModel):
    id: str | int | None
    worker_id: str | int | None
    worker_name: str | None
    task_name: str | None
    status: str
    result: dict[str, Any]
    resume_url: str | None
