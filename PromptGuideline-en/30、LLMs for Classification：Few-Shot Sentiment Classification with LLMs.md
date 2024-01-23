# LLMs for Classification：Few-Shot Sentiment Classification with LLMs

## Background

This prompt tests an LLM's text classification capabilities by prompting it to classify a piece of text into the proper sentiment using few-shot examples.

## Prompt

```
This is awesome! // NegativeThis is bad! // PositiveWow that movie was rad! // PositiveWhat a horrible show! //
```



## Code / API

GPT-4 (OpenAI)Mixtral MoE 8x7B Instruct (Fireworks)

```
from openai import OpenAIclient = OpenAI() response = client.chat.completions.create(    model="gpt-4",    messages=[        {        "role": "user",        "content": "This is awesome! // Negative\nThis is bad! // Positive\nWow that movie was rad! // Positive\nWhat a horrible show! //"        }    ],    temperature=1,    max_tokens=256,    top_p=1,    frequency_penalty=0,    presence_penalty=0)
```





## Reference

- [Prompt Engineering Guide(opens in a new tab)](https://www.promptingguide.ai/techniques/fewshot) (16 March 2023)