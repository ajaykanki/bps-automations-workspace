from shared import JobResult
from pprint import pprint


def post_result(result: JobResult) -> None:
    print("post_result")
    pprint(result.model_dump())
