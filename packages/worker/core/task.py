import functools
from typing import Any, Callable, Optional
from procrastinate import JobContext
from shared import JobResult
from .app import app
from .post_result import post_result


# Use this decorator to define tasks
def task(original_func: Optional[Callable] = None, **kwargs):
    """
    Task middleware to define procrastinate tasks and do something with the result
    Each task must take the JobContext as the first argument and a keyword argument named "resume_url"
    """

    def wrap(func: Callable) -> Callable:
        @functools.wraps(func)
        def new_func(*job_args, **job_kwargs) -> Any:
            # Get the context from the first argument of the task
            context: JobContext = job_args[0] if job_args else None
            # Attach resume_url to additional_context
            resume_url = job_kwargs.get("resume_url")
            if resume_url:
                context.additional_context["resume_url"] = resume_url

            try:
                result = func(*job_args, **job_kwargs)
                job_result = JobResult(
                    id=context.job.id if context else None,
                    status="succeeded",
                    task_name=context.job.task_name if context else "unknown",
                    worker_name=context.worker_name if context else "unknown",
                    worker_id=context.job.worker_id if context else None,
                    resume_url=context.additional_context.get("resume_url"),
                    result=result,
                )
                post_result(job_result)
                return result
            except Exception as e:
                # Catch unknown exceptions
                error_object = {
                    "type": type(e).__name__,
                    "message": str(e),
                }
                job_result = JobResult(
                    id=context.job.id if context else None,
                    status="failed",
                    task_name=context.job.task_name if context else "unknown",
                    worker_name=context.worker_name if context else "unknown",
                    worker_id=context.job.worker_id if context else None,
                    result=error_object,
                    resume_url=context.additional_context.get("resume_url"),
                )
                post_result(job_result)
                # Re-raise the exception to maintain the expected error behavior
                raise

        return app.task(**kwargs)(new_func)

    if original_func is None:
        return wrap

    return wrap(original_func)
