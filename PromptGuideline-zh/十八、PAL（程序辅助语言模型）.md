# PAL（程序辅助语言模型）

[Gao等人（2022）(opens in a new tab)](https://arxiv.org/abs/2211.10435)提出了一种使用LLMs读取自然语言问题并生成程序作为中间推理步骤的方法。被称为程序辅助语言模型（PAL），它与思维链提示不同，因为它不是使用自由形式文本来获得解决方案，而是将解决步骤卸载到类似Python解释器的编程运行时中。

![PAL](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fpal.dfc96526.png&w=1920&q=75)

图片来源：[Gao等人（2022）(opens in a new tab)](https://arxiv.org/abs/2211.10435)

让我们以LangChain和OpenAI GPT-3为例。我们有兴趣开发一个简单的应用程序，它能够解释所提出的问题，并利用Python解释器提供答案。

具体来说，我们有兴趣创建一个功能，允许使用LLM回答需要日期理解的问题。我们将为LLM提供一个提示，其中包括一些示例，这些示例是从[这里(opens in a new tab)](https://github.com/reasoning-machines/pal/blob/main/pal/prompt/date_understanding_prompt.py)采用的。

这是我们需要导入的包：

```
import openaifrom datetime import datetimefrom dateutil.relativedelta import relativedeltaimport osfrom langchain.llms import OpenAIfrom dotenv import load_dotenv
```

让我们先配置一些环境：

```
load_dotenv() # API configurationopenai.api_key = os.getenv("OPENAI_API_KEY") # for LangChainos.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
```

设置模型实例：

```
llm = OpenAI(model_name='text-davinci-003', temperature=0)
```

设置提示+问题：

```
question = "Today is 27 February 2023. I was born exactly 25 years ago. What is the date I was born in MM/DD/YYYY?" DATE_UNDERSTANDING_PROMPT = """# Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?# If 2015 is coming in 36 hours, then today is 36 hours before.today = datetime(2015, 1, 1) - relativedelta(hours=36)# One week from today,one_week_from_today = today + relativedelta(weeks=1)# The answer formatted with %m/%d/%Y isone_week_from_today.strftime('%m/%d/%Y')# Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?# If the first day of 2019 is a Tuesday, and today is the first Monday of 2019, then today is 6 days later.today = datetime(2019, 1, 1) + relativedelta(days=6)# The answer formatted with %m/%d/%Y istoday.strftime('%m/%d/%Y')# Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?# If the concert was scheduled to be on 06/01/1943, but was delayed by one day to today, then today is one day later.today = datetime(1943, 6, 1) + relativedelta(days=1)# 10 days ago,ten_days_ago = today - relativedelta(days=10)# The answer formatted with %m/%d/%Y isten_days_ago.strftime('%m/%d/%Y')# Q: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?# It is 4/19/1969 today.today = datetime(1969, 4, 19)# 24 hours later,later = today + relativedelta(hours=24)# The answer formatted with %m/%d/%Y istoday.strftime('%m/%d/%Y')# Q: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?# If Jane thought today is 3/11/2002, but today is in fact Mar 12, then today is 3/12/2002.today = datetime(2002, 3, 12)# 24 hours later,later = today + relativedelta(hours=24)# The answer formatted with %m/%d/%Y islater.strftime('%m/%d/%Y')# Q: Jane was born on the last day of Feburary in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?# If Jane was born on the last day of Feburary in 2001 and today is her 16-year-old birthday, then today is 16 years later.today = datetime(2001, 2, 28) + relativedelta(years=16)# Yesterday,yesterday = today - relativedelta(days=1)# The answer formatted with %m/%d/%Y isyesterday.strftime('%m/%d/%Y')# Q: {question}""".strip() + '\n'
```

```
llm_out = llm(DATE_UNDERSTANDING_PROMPT.format(question=question))print(llm_out)
```

```
exec(llm_out)print(born)
```



这将输出以下内容：`02/27/1998`