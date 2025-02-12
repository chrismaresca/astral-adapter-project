# LLM Provider Adapters Project

## Overview

This project is a test project for the LLM Provider Adapters. You're job is to create the adapter classes and functions for converting between the ValidatedLLMInterface and provider-specific TypedDicts for OpenAI and Anthropic.

You shouldn't need an API key to run the project as you're just responsible for creating the adapter classes and ensure it validates properly and is typed safely through the lifecycle of the TypedDicts.

### IMPORTANT

OpenAI has a NotGiven type that is not the same as None. Feel free to just use None, unless you want to copy the NotGiven type from OpenAI's source code.

## OpenAI Docs

[https://platform.openai.com/docs/api-reference/introduction](https://platform.openai.com/docs/api-reference/introduction)

## Anthropic Docs

[https://docs.anthropic.com/en/api/reference](https://docs.anthropic.com/en/api/getting-started)

## Installation

1. Install uv - a faster package manager for Python

```bash
pipx install uv
```

2. Install the dependencies - this will create a virtual environment and install the dependencies

```bash
uv sync
```

## Run Main

```bash
uv run -m src.main
```
