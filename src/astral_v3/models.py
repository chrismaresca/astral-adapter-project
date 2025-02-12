# ------------------------------------------------------------
# Models
# ------------------------------------------------------------


"""
LLM Models available for use.
"""



# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------

# Built-in imports
from typing import Literal, TypeAlias, Union

# ------------------------------------------------------------
# Models
# ------------------------------------------------------------

OpenAIModels = Literal[
    "gpt-4o",
    "gpt-4o-01-10-24",
    "gpt-4o-01-15-24",
    "gpt-4o-12-17-24",
    "o1",
    "o1-01-10-24",
    "o1-01-15-24",
    "o1-12-17-24",
    "o1-mini",
    "o1-mini-01-10-24",
    "o1-mini-01-15-24",
    "o1-mini-12-17-24",
    "o3-mini",
    "o3-mini-2025-01-31",
]

AnthropicModels = Literal[
    "claude-3-5-haiku-20241022",
    "claude-3-5-sonnet",
    "claude-3-5-sonnet-20241022",
    "claude-3-haiku",
    "claude-3-opus",
    "claude-3-opus-20240229",
]

ModelName: TypeAlias = Union[OpenAIModels, AnthropicModels]