# -------------------------------------------------------------------------------- #
# Intelligence Client Request Parameter Types and Schemas
# -------------------------------------------------------------------------------- #


"""

This module contains the types for intelligence client request parameters and schemas.

"""

# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------

# Built-in imports
from typing import Any, Dict, List, Optional, Union, TypeAlias, Literal, Generic, TypeVar

# pydantic imports
from pydantic import BaseModel, Field, computed_field

# Message Types
from .messages import Message, MessageListType

# Models
from .models import ModelName

# ------------------------------------------------------------
# Structured Output Response Type
# ------------------------------------------------------------

StructuredOutputResponse = TypeVar('StructuredOutputResponse', bound=BaseModel)


# -------------------------------------------------------------------------------- #
# Reasoning Effort Types
# -------------------------------------------------------------------------------- #

ReasoningEffort: TypeAlias = Literal["low", "medium", "high"]


# -------------------------------------------------------------------------------- #
# Tool Choice Types
# -------------------------------------------------------------------------------- #

ToolChoiceOption: TypeAlias = Union[Literal["auto"], None, 'ToolChoice']

# -------------------------------------------------------------------------------- #
# Tool Choice Model
# -------------------------------------------------------------------------------- #


class ToolChoice(BaseModel):
    """
    The tool choice for the LLM.
    """
    function_name: Optional[str] = Field(description="The name of the function to be used.")

    @computed_field
    @property
    def type(self) -> bool:
        return self.type == "function"


# -------------------------------------------------------------------------------- #
# Tool Model
# -------------------------------------------------------------------------------- #


class Tool(BaseModel):
    """
    A tool is a function that can be called by the LLM.
    """
    name: str = Field(description="The name of the tool to be used.")
    description: str = Field(
        description="The description of the tool to be used.")
    parameters: Dict[str, Any] = Field(
        description="The parameters of the tool to be used.")
    strict: bool = Field(description="Whether the tool is strict.")

    @computed_field
    @property
    def type(self) -> bool:
        return self.type == "function"


# -------------------------------------------------------------------------------- #
# Request Model Settings Models
# -------------------------------------------------------------------------------- #


class ModelSettings(BaseModel):
    """
    The settings for the model.
    """
    temperature: Optional[float] = Field(description="The temperature of the model.", default=None)
    top_p: Optional[float] = Field(description="The top p of the model.", default=None)


# ------------------------------------------------------------
# LLM Interface
# ------------------------------------------------------------

class LLMInterface(BaseModel):
    """
    Base call parameters for LLM calls.
    """
    messages: MessageListType = Field(description="The messages to be sent to the LLM.")
    model: ModelName = Field(description="The model to be used for the LLM call.")
    user: Optional[str] = Field(description="The user to be used for the LLM call.")
    tools: Optional[List[Tool]] = Field(description="The tools to be used for the LLM call.")
    tool_choice: Optional[ToolChoiceOption] = Field(description="The tool choice to be used for the LLM call.")
    reasoning_effort: Optional[ReasoningEffort] = Field(description="The reasoning effort to be used for the LLM call.")
    structured_model: Optional[StructuredOutputResponse] = Field(description="The structured model to be used for the LLM call.")

# -------------------------------------------------------------------------------- #
# Validated Base AI Call Params Models
# -------------------------------------------------------------------------------- #


class ValidatedLLMInterface(LLMInterface):
    """
    Validated base call parameters for LLM calls.
    """
    messages: List[Message] = Field(description="The messages to be sent to the LLM.")
    tool_choice: ToolChoiceOption = Field(description="The tool choice to be used for the LLM call.")
    structured_model: Optional[StructuredOutputResponse] = Field(description="The structured model to be used for the LLM call.")


