from langsmith import traceable


class Tracer:
    """
    Central place for LangSmith tracing.

    The rest of the application should not depend directly
    on LangSmith. If we ever replace the tracing provider,
    only this file should need to change.
    """

    @staticmethod
    def trace(name: str):
        return traceable(name=name)


tracer = Tracer()