# LLMs for Classification：Sentiment Classification with LLMs

## Background

This prompt tests an LLM's text classification capabilities by prompting it to classify a piece of text.

## Prompt

```
Classify the text into neutral, negative, or positiveText: I think the food was okay.Sentiment:
```



## Prompt Template

```
Classify the text into neutral, negative, or positiveText: {input}Sentiment:
```



## Code / API

GPT-4 (OpenAI)Mixtral MoE 8x7B Instruct (Fireworks)

```
from openai import OpenAIclient = OpenAI() response = client.chat.completions.create(    model="gpt-4",    messages=[        {        "role": "user",        "content": "Classify the text into neutral, negative, or positive\nText: I think the food was okay.\nSentiment:\n"        }    ],    temperature=1,    max_tokens=256,    top_p=1,    frequency_penalty=0,    presence_penalty=0)
```





## Reference

- [Prompt Engineering Guide(opens in a new tab)](https://www.promptingguide.ai/introduction/examples#text-classification) (16 March 2023)