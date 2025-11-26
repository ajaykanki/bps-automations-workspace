import time
from core import task
from procrastinate import JobContext


@task(name="add", pass_context=True)
def add(context: JobContext, a: int, b: int) -> int:
    print("Executing task add")
    print("Sleeping for 5 seconds")
    time.sleep(5)
    return {
        "output": a + b,
    }
