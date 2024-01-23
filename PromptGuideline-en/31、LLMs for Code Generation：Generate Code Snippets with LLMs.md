# LLMs for Code Generation：Generate Code Snippets with LLMs

## Background

This prompt tests an LLM's code generation capabilities by prompting it to generate the corresponding code snippet given details about the program through a comment using `/* <instruction> */`.

## Prompt

```
/*
Ask the user for their name and say "Hello"
*/
```



## Code / API

GPT-4 (OpenAI)Mixtral MoE 8x7B Instruct (Fireworks)

```
from openai import OpenAI
client = OpenAI()
 
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
        "role": "user",
        "content": "/*\nAsk the user for their name and say \"Hello\"\n*/"
        }
    ],
    temperature=1,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
```





## Reference

- [Prompt Engineering Guide(opens in a new tab)](https://www.promptingguide.ai/introduction/examples#code-generation) (16 March 2023)