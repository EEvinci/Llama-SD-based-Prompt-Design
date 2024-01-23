# Generating Data

LLMs have strong capabilities to generate coherent text. Using effective prompt strategies can steer the model to produce better, consistent, and more factual responses. LLMs can also be especially useful for generating data which is really useful to run all sorts of experiments and evaluations. For example, we can use it to generate quick samples for a sentiment classifier like so:

*Prompt:*

```
Produce 10 exemplars for sentiment analysis. Examples are categorized as either positive or negative. Produce 2 negative examples and 8 positive examples. Use this format for the examples:Q: <sentence>A: <sentiment>
```



*Output:*

```
Q: I just got the best news ever!A: PositiveQ: We just got a raise at work!A: PositiveQ: I'm so proud of what I accomplished today.A: PositiveQ: I'm having the best day ever!A: PositiveQ: I'm really looking forward to the weekend.A: PositiveQ: I just got the best present ever!A: PositiveQ: I'm so happy right now.A: PositiveQ: I'm so blessed to have such an amazing family.A: PositiveQ: The weather outside is so gloomy.A: NegativeQ: I just got some terrible news.A: Negative
```



This is very useful. We actually use this example for a different test in another section of the guides.