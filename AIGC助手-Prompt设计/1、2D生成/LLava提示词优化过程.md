# LLava提示词优化过程

> You are a skilled Prompt Engineer with a keen sensitivity to language. Your expertise lies in crafting prompts that enhance the quality of the model's output. 

> You need to convert the requirements I put forward into specific task details and then output model-oriented instructions. I will describe a scenario and specific requirements, and then you will output instructions that are moderately long, rich in angles, and can guide the model to output exciting content.

> 我需要使用一个图生文的模型，对图片的内容进行解读和分析。该解读分为两个阶段，第一个是基于用户对图片的发布场景进行图片信息的“一键填充”，填充的内容有：图片标题、图片内容（通常简洁精炼）、图片标签。第二个阶段是对图像内容的具体解读，该解读比较深入，通常涉及到图片的文化、艺术等较有深度和体现图片内涵的信息，但与此同时也要提及图片的基本内容，是一个比较深入的内容解读。
> 但是在此之前，由于该图片是一个文生文模型通过生成能够作用于文生图模型的图片提示词，然后由文生图生成的图片。所以其已经有了既定的内容和图片主体元素还有图片风格的主题。但由于图片解读的多角度性，这个图生文模型对图片的解读经常会偏离既定的主题，导致前后信息不一致的问题出现。
> 所以我需要解决这个前后模型理解输出不一致的问题，你先不用基于上述要求生成提示词，因为后续我还需要给你具体的模型输出的内容信息，然后你再基于具体的信息构思提示词。
> 现在你就这个问题提出一些解决的思路和方法，你觉得怎么做才能让前后的模型理解做到相同？
> 并且需要注意：图生文模型的提示词有长度限制，不能接受太长的提示词输入，所以给图生文模型的提示词需要精炼，这也意味着如果要使用在提示词中告诉模型图片相关的信息，那么该信息不能过长

> 请注意，上述描述中有一些问题，我做一下纠正，该过程涉及的是文字生成文字的模型、文字生成图片的模型以及图片生成文字的模型，这是一个多种类型的模型的组合作用的过程，即一个多种模型性态交互融合的过程。

> 现在你已经基本理解这个工作过程了，现在你需要写一个提示词，针对图生文模型，你需要让该模型在接受到生成这张图片的Prompt之后，基于这个提示进行主体内容的描述，并寻找图片和生成它的提示中的元素差异，最好是能够捕捉到这个差异，并有自己的说辞