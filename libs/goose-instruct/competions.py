from pydantic import BaseModel
from functools import singledispatch


class OpenAICompletionsSource(BaseModel):
    api_key: str
    api_url: str
    region: str
    deployment: str
    model: str


@singledispatch
def completions[T](llm, prompt: str) -> T:
    pass


@completions.register
def _openai_completions[T](llm: OpenAICompletionsSource) -> T:
    pass  # call openai client, problem solved


# TODO Should be async only!
# TODO How well does typechecking work?
# TODO Should accept any pydantic type as its result type!
