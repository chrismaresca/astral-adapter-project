# -------------------------------------------------------------------------------- #
# LLM Provider Adapters
# -------------------------------------------------------------------------------- #

"""
This module contains adapter classes and functions for converting between the ValidatedLLMInterface
and provider-specific TypedDicts for OpenAI and Anthropic.
"""

# -------------------------------------------------------------------------------- #
# Imports
# -------------------------------------------------------------------------------- #

# Built-in imports
from typing import Generic, TypeVar

# Pydantic imports
from pydantic import BaseModel

# Interface imports
from astral_v3.interface import ValidatedLLMInterface

# -------------------------------------------------------------------------------- #
# Adapter Classes
# Adapter classes or functions here
# Use the OpenAI and Anthropic Docs to find out the TypedDicts to create.
# Reminder: The Adapter should take a ValidatedLLMInterface and return a Provider Specific TypedDict.
# Reminder: The Adapeter should be Generic and either a class or function.
# Feel free to add other imports you need and create other files in the src directory.

# -------------------------------------------------------------------------------- #


# -------------------------------------------------------------------------------- #
# Main
# -------------------------------------------------------------------------------- #

"""
Validation code to test adapter conversion between ValidatedLLMInterface and provider TypedDicts
"""


def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
