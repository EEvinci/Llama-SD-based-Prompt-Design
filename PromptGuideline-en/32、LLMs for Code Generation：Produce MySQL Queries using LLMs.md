# LLMs for Code Generation：Produce MySQL Queries using LLMs

## Background

This prompt tests an LLM's code generation capabilities by prompting it to generate a valid MySQL query by providing information about the database schema.

## Prompt

```
"""
Table departments, columns = [DepartmentId, DepartmentName]
Table students, columns = [DepartmentId, StudentId, StudentName]
Create a MySQL query for all students in the Computer Science Department
"""
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
        "content": "\"\"\"\nTable departments, columns = [DepartmentId, DepartmentName]\nTable students, columns = [DepartmentId, StudentId, StudentName]\nCreate a MySQL query for all students in the Computer Science Department\n\"\"\""
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