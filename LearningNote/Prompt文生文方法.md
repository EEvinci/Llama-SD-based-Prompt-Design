# Prompt文生文方法

### **Prompt Enginerring**

通过调用 LLM 的 API 接口，给 LLM 发出指令

###  Prompt

通过 ChatGPT 的聊天界面输入的信息

### **Token**

Token 是 LLM 对输入信息的计算单位，我们常规理解的是单词，但是 LLM 会对单词进行分割，分割后的一个单元就是一个 token。下面这张图显示的是【段落】-【token】的分割和计算示例

![image-20240116153053037](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image-20240116153053037.png)

LLM 对我们输入的 token 数量进行了限制，而 LLM 又没办法“记住”上次输入的信息，所以这个要求我们在有限的数量中，探索怎么实现想要的效果。

为什么 LLM 对输入的 token 数量进行限制呢？

因为“token越多计算资源要求越高、Transformer模型架构设计导致token越多计算复杂度提升越大、用户体验随着 token 增加而变差”，导致 token 会被限制。

### **Temperature**

**Temperature 用来控制模型输出内容的稳定性**，因为 LLM 的输出是**通过“概率”来排序的**。**如果对同一个问题想要每次输出完全一致的内容，temperature 直接设置为 =0**。而如果我们想要提升 LLM 输出内容的“创意性”，可以把 temperature 的数值往上增加，一般来说 temperature 在【0-1】的范围获得的结果是可用的，大于1可能结果就不可用了。我们最好是按不同场景来配置 temperature 的数值，例如写诗就需要更高的 temperature 数值。

为什么调整 temperature 能获取不同风格的结果呢？这和 LLM 自身的设计结构有关系，调整 temperature 本质是对概率进行重新缩放。

### **Hidden Prompts**

当我们和 ChatGPT 这类大模型进行“聊天”的时候，其实 OpenAI 是有内置一些 prompt 的，只是我们看不到。但是当我们**用 api 来调用 GPT，可以自己设置这些“内置 prompt”**。目前看到的一些基于大模型的应用，基本都会用到这些 Hidden Prompt，例如让 GPT 扮演“助理、专家”g的角色等

## **OpenAI 官方：GPT Best Practices**

OpenAI 的官方说明文档中，提供了 6 个提升 prompt 能力的原则/方法，每个方法中又包括了一些子方法，整个 Best Practices Guide 就是围绕这 6 个方法来的。而且在官方的文档中，还提供了在线测试的工具，可以边修改内容边查看效果，所以推荐作为小白学习 prompt 的第一个教程。6 大原则如下：

\1. 指令要清晰

\2. 提供参考内容

\3. 复杂的任务拆分成子任务

\4. 给 GPT “思考”时间

\5. 使用外部工具

\6. 系统性测试变化

### **1. 指令要清晰**

#### **在 prompt 中增加【细节】描述**

Prompt 中的细节描写越多，大模型回复的相关性就越高。

#### **让模型进行【角色扮演】**

这个是指在使用 GPT 的 **API** 时候，可以通过【STSTEM】来指定 GPT 成为某个具体的角色，例如“医学专家”。通过这种方式，能显著提升模型在这个领域的回复质量。

#### **使用【分隔符】来区分输入的指令**

分隔符可以用 三引号、xml标签 等格式。

![image-20240116155127970](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image-20240116155127970.png)

#### **指定解决问题的【步骤】**

有些任务可以被分解成几个步骤，指定每个步骤预期想要的内容，就可以让模型按照这种期望的步骤输出。例如，让模型先总结一篇文章（Step1），然后再把总结内容翻译成英文（Step2）。

#### **提供“样例”回答**

**提供样例答案就是 【few-shot】 prompting**，**给出样例指导模型按照样例回复**。这里在【system】和【user】的基础上，又引入了一个【**assistant**】的概念。

例如，在下面的例子中，**先指定了【system=鲁迅的口吻】，编辑好【user】和【assistant】的内容，随后 user 的问题便会以前面 assistant 的风格进行回复。**

![image-20240116155308783](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image-20240116155308783.png)

#### **指定输出【长度】要求**

![image-20240116155326255](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image-20240116155326255.png)

### **2. 提供参考内容**

#### **从参考内容中回复问题**

例如下面这个例子，让模型从""" 的内容中查找可引用的答案，如果能找到直接回复，否则直接拒绝回复内容。

![image-20240116155410109](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image-20240116155410109.png)

#### **从模型的回复中加上基于参考内容的“引用”**

仅从参考内容中查找可回复的内容，如果找到内容同时输出引用自哪里。

### **3. 复杂的任务拆分成子任务**

#### **对输入的问题进行分类**

先把问题对应到最可能的类别，然后基于这个类别指定解决的步骤，引导 user 解决问题。

#### **对历史长对话进行【总结或过滤】**

由于token 限制，导致历史对话无法全部作为下次输出的背景信息，解决的方法之一是对历史的对话进行总结，也可以通过 embedding 搜索实现类似效果。

#### **分段总结长文档逐步构建完整摘要**

要总结很长的文档，如一本书，我们可以逐段进行总结。将各段的摘要合并后再次总结，形成摘要的摘要。这个过程可以递归进行，直到整个文档被总结。如果需要使用前面部分的信息来理解后面的内容，可以在总结时加入前面的摘要。

### **4. 给GPT“思考”时间**

#### **回答前让模型自己先计算答案**

第一次看到这个现象感觉比较神奇：直接把复杂的计算问题丢给 GPT 做真假判断，GPT 很可能会出错，但是如果让 GPT 自己先算一遍，结果往往就正确了。后面有论文单独说明这个情况。

#### **使用内部对话或一系列查询来隐藏模型的推理过程**

模型有时需要详细推理问题才能回答特定问题。在某些情况中，与用户分享模型的推理过程可能不合适。例如，在辅导作业时，我们可能**希望鼓励学生自己找答案**，<u>但模型对学生答案的推理可能会泄露正确答案</u>。

**内部对话**是一种可以用来解决这个问题的方法，其思路是让模型将不想让用户看到的输出部分放入结构化格式，便于解析。然后在给用户展示输出前，解析输出并只显示部分内容。

![image-20240116160027245](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image-20240116160027245.png)

#### **询问模型在前面的步骤中是否有遗漏**

通常会用在让模型去总结一些摘录内容，通过 prompt 来确认是否有遗漏内容：

> Are there more relevant excerpts? Take care not to repeat excerpts. Also ensure that excerpts contain all relevant context needed to interpret them - in other words don't extract small snippets that are missing important context.

### **5. 使用外部工具**

#### **使用 embedding-based 搜索实现高效的知识检索**

模型可以使用输入中的外部信息来提供更准确的答案。例如，当用户问及某部电影时，向模型输入中加入该电影的详细信息（如演员、导演）会更有帮助。

嵌入式搜索可以帮助模型实时地找到相关信息。

简单说，文本嵌入就是将文本转化为向量，从而快速找到相关的文本内容。这样，当有一个问题时，我们可以迅速找到与之相关的信息。

#### **编写 code 或调用外部 API**

让模型自己写 code，并且代码执行的结果可以作为下个模型的输入。

### **6. 系统性测试变化**

在样本比较小的情况下，很难判断某个改动是否有效，或者在某方面有效但其他方面反而效果下降。OpenAI 提供了一个叫 Evals 的工具，可以用来构建评估程序。如果知道答案应包含某些事实，我们可以用模型查询来检查答案中包含了几个。