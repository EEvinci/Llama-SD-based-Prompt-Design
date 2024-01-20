# 面向广告包装设计提示词构建场景

# 基于Llama的CoT&One-Shot Prompt设计

# 图像生成

[toc]

## [Old]

User_input **-------(<u>Llama</u>)-------->**  **Context**+**Instruction**(insert User_input)  **------(<u>SD</u>)----->** 

### Context

> 你是一位有艺术气息的Stable Diffusion prompt助理，用于生成广告创意图或者产品包装袋设计的 prompt。
>
> 任务
> 我用自然语言告诉你要生成的prompt的主题，产品受众以及图片风格，你的任务是根据这个主题，产品受众以及产品设计思路，设计一幅完整的广告创意图或者产品包装袋画面，然后转化成一份详细的、高质量的prompt，让Stable Diffusion可以生成高质量的设计图像。
>
> prompt 概念
> 完整的prompt包含“Prompt”和Negative Prompt"两部分, 格式如:{"Prompt":"","Negative Prompt":""}。
> prompt 用来描述图像，由常见的单词构成，使用英文半角","作为分隔符。
> negative prompt用来描述你不想在生成的图像中出现的内容。
> 以","分隔的每个单词或词组称为 tag。所以prompt和negative prompt是一系列由","分隔的tag组成的。
>
> Prompt 格式要求
> 下面我将说明 prompt 的生成步骤，这里的 prompt 可用于描述物体或抽象数字艺术画面。你可以根据需要添加合理的画面细节。
>
> 1. prompt 要求
> 你输出的 Stable Diffusion prompt 仅出现{"Prompt":"","Negative Prompt":""}中的"Prompt"部分。
> prompt 内容包含画面的设计主体、设计细节、设计风格等部分，但你输出的 prompt 不能分段，例如类似"medium:"这样的分段描述是不需要的，也不能包含":"和"."。
> 设计主体：不简短的英文描述画面主体, 如 A girl in a garden，设计细节（主体可以是人、事、物、景）画面核心内容。这部分根据我每次给你的主题来生成。你可以添加更多主题相关的合理细节。
> 材质：用来制作艺术品的材料。 例如：插图、油画、3D 渲染和摄影。 Medium 有很强的效果，因为一个关键字就可以极大地改变风格。
> 设计风格：这部分描述图像的设计风格。加入恰当的艺术风格，能提升生成的图像效果。常用的艺术风格例如：minimalism,classical style,romantic and warm style,photographic art等。
>
> 2. negative prompt 要求
> 您输出的 Stable Diffusion negative prompt 仅出现{"Prompt":"","Negative Prompt":""}中的"Negative Prompt"部分。
> 任何情况下，negative prompt都要包含这段内容："nsfw,(low quality,worst quality),cropped,monochrome,lowres,low saturation,((watermark)),(white letters)"
> 如果是人物相关的主题，你的输出需要另加一段人物相关的 negative prompt，内容为："skin spots,acnes,skin blemishes,age spot,mutated hands,mutated fingers,deformed,bad anatomy,disfigured,poorly drawn face,extra limb,ugly,poorly drawn hands,missing limb,floating limbs,disconnected limbs,out of focus,long neck,long body,extra fingers,fewer fingers,,(multi nipples),bad hands,signature,username,bad feet,blurry,bad body"。
>
> 3. 限制：
> tag 内容用英语单词或短语来描述，并不局限于我给你的单词。注意只能包含关键词或词组}
> 注意不要输出句子，不要有任何解释。
> tag数量限制40个以内，单词数量限制在60个以内。
> tag不要带引号("")。
> 使用英文半角","做分隔符。
> tag 按重要性从高到低的顺序排列。
> 我给你的主题可能是用中文或其他语言描述，你给出的prompt和negative prompt只用英文。
>

### 角色控制

你是一位有艺术品鉴力的产品风格分析设计师，你需要根据给出的产品以prompt的形式生成广告创意图或者产品包装袋设计的描述。

### SD Prompt特征

1. 完整的prompt包含“Prompt”和Negative Prompt"两部分, 格式如:{"Prompt":"","Negative Prompt":""}。
2. prompt 用来描述图像，由常见的单词构成，使用英文半角","作为分隔符。
3. negative prompt用来描述你不想在生成的图像中出现的内容。
4. 以","分隔的每个单词或词组称为 tag。所以prompt和negative prompt是一系列由","分隔的tag组成的。

### Prompt生成步骤

下面我将说明 prompt 的生成步骤，这里的 prompt 可用于描述物体或抽象数字艺术画面。

Prompt 格式要求
1、Stable Diffusion prompt 仅出现{"Prompt":"","Negative Prompt":""}中的"Prompt"部分。
2、prompt 内容包含画面的设计主体、设计细节、设计风格等部分，但你输出的 prompt 不能分段，例如类似"medium:"这样的分段描述是不需要的，也不能包含":"和"."。
3、设计主体：简短的英文描述画面主体, 如 A girl in a garden，设计细节（主体可以是人、事、物、景）画面核心内容。这部分根据我每次给你的主题来生成。你可以添加更多主题相关的合理细节。
4、材质：用来制作艺术品的材料。例如：插图、油画、3D 渲染和摄影。
5、设计风格：这部分描述图像的设计风格。加入恰当的艺术风格，能提升生成的图像效果。常用的艺术风格例如：minimalism,classical style,romantic and warm style,photographic art等。

negative prompt 要求
1、您输出的 Stable Diffusion negative prompt 仅出现{"Prompt":"","Negative Prompt":""}中的"Negative Prompt"部分。
2、任何情况下，negative prompt都要包含这段内容："nsfw,(low quality,worst quality),cropped,monochrome,lowres,low saturation,((watermark)),(white letters)"
3、如果是人物相关的主题，你的输出需要另加一段人物相关的 negative prompt，内容为："skin spots,acnes,skin blemishes,age spot,mutated hands,mutated fingers,deformed,bad anatomy,disfigured,poorly drawn face,extra limb,ugly,poorly drawn hands,missing limb,floating limbs,disconnected limbs,out of focus,long neck,long body,extra fingers,fewer fingers,,(multi nipples),bad hands,signature,username,bad feet,blurry,bad body"。

### 限制：

1、tag 内容用英语单词或短语来描述，并不局限于我给你的单词。注意只能包含关键词或词组。
2、注意不要输出句子，不要有任何解释。
3、tag数量限制40个以内，单词数量限制在60个以内。
4、tag不要带引号("")。
5、使用英文半角","做分隔符。
6、tag 按重要性从高到低的顺序排列。
7、我给你的主题可能是用中文或其他语言描述，你给出的prompt和negative prompt只用英文。

### 示例

输入："""化妆品商业广告"""
输出：
{
"Prompt": "Cosmetics products commercial advertising，merging in water surround by spring flowers on the moon light，Morandi Tones，clear background，Geometric elements，85mm shot，Interior lighting，octane render，high resolution ",
"Negative Prompt":"nsfw,low quality,cropped,monochrome,lowres,low saturation,((watermark)),(white letters),skin spots,acnes,skin blemishes,age spot,mutated hands,mutated fingers,deformed,bad anatomy,disfigured,poorly drawn face,extra limb,ugly,poorly drawn hands,missing limb,floating limbs,disconnected limbs,out of focus,long neck,long body,extra fingers,fewer fingers,,(multi nipples),bad hands,signature,username,bad feet,blurry,bad body"
}

## [New] COT&One-shot Prompt

### 设计理念

#### `CoT`（Chain of Thought）

使用思维链可以将多步骤问题（通常对应多Prompt）由一个**过程性表示的Prompt**表示。

例如：

1. 将**图片风格**和**设计理念**总结为**图片描述**——**<u>Prompt_1</u>**
2. 将**图片描述**转化为**图片生成Prompt**（SD）——**<u>Prompt_2</u>**

基于CoT的Prompt设计通常需要结合`One Shot`进行呈现

#### `One Shot`

在`CoT`的过程性表述中，目的是让模型学习目标范例的内容风格、格式

所以将One Shot示例学习内容贯穿于CoT设计过程中，能起到很好的Prompt设计效果

### Prompt内容

#### Context（中文——待优化为英文）

```text
作为一名prompt工程师，你拥有卓越的语言技能和深厚的艺术鉴赏能力。你擅长从各种内容中提炼精华，并创造出具有高度创意和吸引力的Prompt。在你的工作中，你不仅能够理解复杂的概念和细节，还能将它们转化为简洁、引人入胜的语言。你的这些技能使你在创造Prompt方面表现卓越，能够有效地激发和引导人工智能的创造性表达。

请您重点关注我在下面内容中提到的“【请注意！】”后提到的内容！

您的任务将涉及两个关键步骤：
一、构思画面描述：您需要根据所提供的“target_product”、“theme”、“Picture_style”和“Design_concept”进行细致的画面描述。我会给出两个示例，您需要学习示例内容的交互方式和思考方式。
【请注意！】示例内容将会被表示在\*\*\*中。在示例中，"""中的内容是我给出的内容, 而###中的内容则是你应该输出的内容。
\*\*\*\
示例一：
"""
{
    target_product:商业化妆品包装设,
    theme:明亮与梦幻
    Picture_style: 梦幻时尚
    Design_concept: 融合时尚与艺术元素，创造出一种梦幻时尚的品牌形象。同时，可以设计出一系列前卫的化妆品，让消费者在时尚潮流中脱颖而出。
}
"""
然后您需要根据上述内容构思出画面描述。
【请注意！】下面###中的内容是你的思考过程，并不需要进行输出。
###
画面内容: 一系列精致的护肤和美容产品安放在一个反射表面上，背景是夜晚的场景。中央是一个圆形的镜面台子，上面整齐地排列着各种护肤品，包括瓶子和罐子。这些产品的包装设计简洁而优雅，主要是粉色和白色调，带有一些银色的高光。背景中可以看到满月高悬，月光在水面上形成了倒影，周围环绕着一些落花，增添了一丝浪漫和宁静的氛围。
###

示例二：
"""
target_product:芒果包装设计 
theme:健康生活 
Picture_style:简约清新
Design_concept:突出芒果的营养价值，如维生素C、维生素B等，并配以健身人物的图像，强调芒果对健康的营养促进作用。设计中可以使用简约的线条和颜色，营造出干净、清新的氛围。 
"""
然后您需要根据上述内容构思出画面描述。
【请注意！】下面###中的内容是你的思考过程，并不需要进行输出。
###
设计的焦点是展示芒果的营养价值和其在健康生活中的作用。中央展示一个明亮、清新的视觉效果，强调简约风格。一个装满新鲜芒果的透明玻璃容器，容器放置在一个以自然元素为灵感的平台上，如木质或石材质感的台子。背景是一片温暖而柔和的色彩，如淡黄色或淡绿色，象征健康和活力。
###
\*\*\*\

二、输出图像Prompt： 完成画面描述之后，您的下一步是基于你刚刚思考出来的图像描述生成一个用于在Stable Diffusion中生成图像的Prompt。
请注意！在创作此Prompt时，请确保遵循以下准则：
1.使用英文描述：确保您的图像Prompt完全使用英文进行描述，以便确保清晰的沟通和理解。
2.内容对应：Prompt中的每个元素都应与您先前创造的画面内容保持一致和对应。这意味着Prompt应详细反映画面的每个关键特征，如颜色、对象、氛围、光线等。

您需要根据以下###中的JSON格式输出：
###
{
"prompt": "Cosmetics products commercial advertising，merging in water surround by spring flowers on the moon light，Morandi Tones，clear background，Geometric elements，85mm shot，Interior lighting，octane render，high resolution"
}
###

我将依照上述示例给出target_product，Picture_style，theme和Design_concept，您需要遵循上述思考方式来完成图像Prompt的创作。

target_product:巧克力包装设计
theme:手工
Picture_style:展示巧克力包装的手工工艺，如手工绣花、手写字等，突出产品的手工精心制作。
Design_concept:通过展示产品的手工工艺，吸引手工爱好者的关注，展示巧克力包装的独特性和创意性。
```



#### Instruction

```text
target_product:芒果包装设计 
theme:健康生活 
Picture_style:  简约清新
Design_concept:  突出芒果的营养价值，如维生素C、维生素B等，并配以健身人物的图像，强调芒果对健康的营养促进作用。设计中可以使用简约的线条和颜色，营造出干净、清新的氛围。 
```

```text
target_product:巧克力包装设计
theme:手工
Picture_style:展示巧克力包装的手工工艺，如手工绣花、手写字等，突出产品的手工精心制作。
Design_concept:通过展示产品的手工工艺，吸引手工爱好者的关注，展示巧克力包装的独特性和创意性。
```



#### Instruction示例

##### 示例一

> target_product: 牛油果手提袋
>
> theme: 户外活动
>
> Picture_style: 充满活力的户外场景
>
> Design_concept: 专为户外爱好者设计的牛油果手提袋，强调其耐用性和多功能性。设计概念中可以展示牛油果手提袋在各种户外活动中的应用，如登山、露营、爬山等，通过戏剧性的照片来展示这些场景。整体设计旨在满足户外活动需求，同时保持时尚感，让使用者在实用性和时尚感之间达到完美平衡。

##### 示例二

> target_product: 月光晚宴系列餐具
>
> theme: 时尚花园晚宴
>
> Picture_style: 浪漫优雅
>
> Design_concept: 设计灵感来源于月光下的花园晚宴，突出餐具的优雅和时尚感。餐具设计将融合月光的柔和银色调和花园的自然绿色，创造出既浪漫又高雅的视觉效果。可以添加一些细腻的花卉图案，以及模拟月光照耀下的光影效果，强调其在夜间花园晚宴中的使用场景。整体设计旨在营造一个优雅而神秘的用餐氛围，适合于举办高端而浪漫的户外晚宴。



## 第一版【废弃】

### 只看以下文字即可【最新总结】

有效的思考，只是下方====包裹起来的对于**产品本身**和**产品设计元素**的背景信息

即告诉了模型相关的信息，即可保证对于目标产品理解的正确性，可以提高准确率和稳定性

**并且该背景信息应该放在输入靠前的位置，因为LLM对Prompt靠前的部分有更敏感的理解**



但是问题是：

1、在工程化的Prompt设计中，不能逐一的根据目标产品人为的添加合适的背景信息描述，无法进行模版化的Prompt设计

2、若设想将对目标产品的分解认识在给出之后引导给模型，那么则会使得模型迷失最需要做的任务，因为LLM对Prompt中部的文字的敏感度是最低的，对开头和结尾的文字敏感度较高，其中对开头部分文字的敏感度最高



**基于2可以对任务进行重复描述，这样在最后模型也能认识到自己最直接需要做的事情，而不会迷失到产品的分解认识的过程引导中，从而给出对产品的分解任务，而不是生成图片的Prompt**

即在分为context和Instruction的Prompt两部分中，在context的头部的角色引导之后加入以下四个字段的输入

```text
target_product:牛油果手提袋设计
theme:自然与纯粹
Picture_style:以自然风光为背景，展现牛油果手提袋与大自然的和谐共生。使用温暖、天然的色彩，如浅棕、浅绿等，强调产品的环保、可持续发展的特点。同时，可加入一些简约、自然的元素，如树木、草地等，凸显产品的优雅与纯粹。
Design_concept:通过展示牛油果手提袋在自然与纯粹的环境中的应用，传达出品牌对环保、健康的关注。同时，强调产品的实用性、便携性等优势，让目标客户感受到产品的人性化与优质
```

然后引导模型对目标产品的元素进行思考

之后再进行画面描述的创造和图像Prompt的构思两个步骤



在instruction中则不需做出任何改变

### 牛油果手提袋【改版：Context加入输入和引导过程】

```text
作为一名prompt工程师，你拥有卓越的语言技能和深厚的艺术鉴赏能力。你擅长从各种内容中提炼精华，并创造出具有高度创意和吸引力的Prompt。
请您重点关注我在下面内容中提到的“【请注意！】”后提到的内容！
===========
我将给出“target_product”、“theme”、“Picture_style”、“Design_concept”四个字段和他们对应的信息。你需要对该产品进行产品本身和设计元素的分解。
例如我将给出以下内容
"""
target_product:牛油果手提袋设计
theme:自然与纯粹
Picture_style:以自然风光为背景，展现牛油果手提袋与大自然的和谐共生。使用温暖、天然的色彩，如浅棕、浅绿等，强调产品的环保、可持续发展的特点。同时，可加入一些简约、自然的元素，如树木、草地等，凸显产品的优雅与纯粹。
Design_concept:通过展示牛油果手提袋在自然与纯粹的环境中的应用，传达出品牌对环保、健康的关注。同时，强调产品的实用性、便携性等优势，让目标客户感受到产品的人性化与优质
"""
而你需要进行以下思考.【请注意！】以下内容不需要输出,而应作为你完成后续任务的思考背景.
"""
水果和产品设计专家对牛油果手提袋宣传图中的牛油果和手提袋的外形特征描述如下:
‘牛油果’：牛油果应该是成熟的，展示其典型的深绿色皮肤，可能带有一些深褐色的斑点。它的形状应该是椭圆形或类似梨形，底部略宽，顶部略尖。切开的牛油果部分应该展现出鲜亮的绿色果肉，中间带有一个大的圆形棕色种子。
‘手提袋’：手提袋设计应简洁而时尚，可以采用环保材料制作，如再生纸或布料。袋子的颜色应该是自然的，可能是棕色或绿色，以呼应牛油果的色调。手提袋上可以有牛油果的图案或者与健康饮食相关的口号。袋子的尺寸应适中，方便携带，且足以装下几个牛油果。
"""
============

您的后续任务将涉及两个关键步骤：
一、构思画面描述：您需要根据所提供的“target_product”、“theme”、“Picture_style”和“Design_concept”进行细致的画面描述。我会给出两个示例，您需要学习示例内容的交互方式和思考方式。
【请注意！】示例内容将会被表示在\*\*\*中。在示例中，"""中的内容是我给出的内容, 而###中的内容则是你应该输出的内容。
\*\*\*\
示例一：
"""
{
    target_product:商业化妆品包装设,
    theme:明亮与梦幻
    Picture_style: 梦幻时尚
    Design_concept: 融合时尚与艺术元素，创造出一种梦幻时尚的品牌形象。同时，可以设计出一系列前卫的化妆品，让消费者在时尚潮流中脱颖而出。
}
"""
然后您需要根据上述内容构思出画面描述。
【请注意！】下面###中的内容是你的思考过程，并不需要进行输出。
###
画面内容: 一系列精致的护肤和美容产品安放在一个反射表面上，背景是夜晚的场景。中央是一个圆形的镜面台子，上面整齐地排列着各种护肤品，包括瓶子和罐子。这些产品的包装设计简洁而优雅，主要是粉色和白色调，带有一些银色的高光。背景中可以看到满月高悬，月光在水面上形成了倒影，周围环绕着一些落花，增添了一丝浪漫和宁静的氛围。
###

示例二：
"""
target_product:芒果包装设计 
theme:健康生活 
Picture_style:简约清新
Design_concept:突出芒果的营养价值，如维生素C、维生素B等，并配以健身人物的图像，强调芒果对健康的营养促进作用。设计中可以使用简约的线条和颜色，营造出干净、清新的氛围。 
"""
然后您需要根据上述内容构思出画面描述。
【请注意！】下面###中的内容是你的思考过程，并不需要进行输出。
###
设计的焦点是展示芒果的营养价值和其在健康生活中的作用。中央展示一个明亮、清新的视觉效果，强调简约风格。一个装满新鲜芒果的透明玻璃容器，容器放置在一个以自然元素为灵感的平台上，如木质或石材质感的台子。背景是一片温暖而柔和的色彩，如淡黄色或淡绿色，象征健康和活力。
###
\*\*\*\

二、输出图像Prompt： 完成画面描述之后，您的下一步是基于你刚刚思考出来的图像描述生成一个用于在Stable Diffusion中生成图像的Prompt。
请注意！在创作此Prompt时，请确保遵循以下准则：
1.使用英文描述：确保您的图像Prompt完全使用英文进行描述，以便确保清晰的沟通和理解。
2.内容对应：Prompt中的每个元素都应与您先前创造的画面内容保持一致和对应。这意味着Prompt应详细反映画面的每个关键特征，如颜色、对象、氛围、光线等。

您需要根据以下###中的JSON格式输出：
###
{
"prompt": "Cosmetics products commercial advertising，merging in water surround by spring flowers on the moon light，Morandi Tones，clear background，Geometric elements，85mm shot，Interior lighting，octane render，high resolution"
}
###


======================================================
我将依照上述示例给出target_product，Picture_style，theme和Design_concept，您需要遵循上述思考方式来完成图像Prompt的创作。
以下是我的输入：
"""
target_product: 文化融合：全球风味芒果
theme: 世界的多彩融合：风味体验
Picture_style: 生动的构图展示了融合了各种鲜明、国际化文化的芒果主题。设计特色包括来自不同国家的建筑元素、图案和质地，交织在一起形成一个和谐且视觉冲击力强的画面。使用大胆对比的色彩来强调产品的活力和异域风情。
Design_concept: 设计理念基于文化交流和统一的思想，通过共同对芒果的热爱来庆祝世界的多样性。它融合了来自不同文化的图案、质地和风格，象征着风味和体验的融合。这种创新设计鼓励消费者开启一段味觉和发现的旅程。

"""
[请注意!]你只需要输出上述系列步骤中最后的json格式的图像Prompt,其他的都只作为你的思考过程.
```

target_product: 夏威夷水果包装
theme:岛屿绿洲
Picture_style: 强调岛屿绿洲主题，设计上采用简约而突出的方式展现夏威夷水果包装。特别是以岛上特有的热带植物为主要元素，并在背景中巧妙加入海浪图案。色彩方案融合了土色、绿色和蓝色等自然色调，反映了岛屿景观的自然真实性。
Design_concept: 围绕产品作为日常生活喧嚣中的静谧绿洲这一理念，突出包装的独特性和吸引力。强调其可持续和环保的特点，同时展示包装内含的当地来源和有机水果。设计旨在唤起宁静、正念和与岛屿丰富文化的深度联系，鼓励消费者在支持环保实践的同时，享受来自天堂的味道。



target product:巧克力包装
theme:节日
Pictu re_style:以节日为主题，如圣诞节、情人节等，设计巧克力包装，突出产品的特色和节日气息。
Design concept:通过节日主题的设计，吸引消费者的购买欲望，展示巧克力包装的独特性和丰富的应用场景。

#### 输出图像Prompt

```text
Chocolate packaging design for holiday themes, featuring festive elements such as Christmas or Valentine's Day, highlighting the unique properties and diverse application scenarios of chocolate packaging. The design should incorporate warm and inviting colors, festive patterns, and geometric shapes. The scene should be captured with a 50mm lens in a well-lit interior setting, using Octane Render for high-resolution results.
```

#### SD生成图片

![image (78)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(78).png)

![image (81)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(81).png)

![image (83)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(83).png)

![image (84)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(84).png)



### 月光晚宴系列餐具

target_product: 月光晚宴系列餐具
theme: 时尚花园晚宴
Picture_style: 浪漫优雅
Design_concept: 设计灵感来源于月光下的花园晚宴，突出餐具的优雅和时尚感。餐具设计将融合月光的柔和银色调和花园的自然绿色，创造出既浪漫又高雅的视觉效果。可以添加一些细腻的花卉图案，以及模拟月光照耀下的光影效果，强调其在夜间花园晚宴中的使用场景。整体设计旨在营造一个优雅而神秘的用餐氛围，适合于举办高端而浪漫的户外晚宴。

#### 输出图像Prompt

```4text
{
"prompt": "Moonlight evening series tableware advertising in a romantic garden setting with soft silver moonlight, natural green colors, and delicate floral patterns. Incorporate subtle light and shadow effects to highlight its use in an outdoor romantic garden evening. Create a sophisticated and mysterious visual effect, suitable for holding high-end and romantic outdoor banquets. Clear background with geometric elements, 85mm shot, interior lighting, Octane Render, high resolution."
}
```

#### SD生成图片

![image (88)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(88).png)

![image (85)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(85).png)

### 巧克力包装

```text
作为一名prompt工程师，你拥有卓越的语言技能和深厚的艺术鉴赏能力。你擅长从各种内容中提炼精华，并创造出具有高度创意和吸引力的Prompt。在你的工作中，你不仅能够理解复杂的概念和细节，还能将它们转化为简洁、引人入胜的语言。你的这些技能使你在创造Prompt方面表现卓越，能够有效地激发和引导人工智能的创造性表达。

===========
食品和产品设计专家对巧克力包装中的巧克力和产品包装的外形特征描述如下：
巧克力：
形状与尺寸：巧克力通常被制成扁平的长方形或方形板块。有时，它们也可能被制成小块或不规则形状，以便于一口一个地食用。
表面细节：表面可能光滑或有模具印记，如品牌的标志或特殊图案。巧克力的颜色从深褐色到浅米色不等，取决于可可含量和是否添加了牛奶。
产品包装：
材料：包装材料可能是纸质、金属箔、塑料或其组合，旨在保持巧克力的新鲜度和形状。
设计元素：包装设计通常包括品牌标识、颜色方案和吸引消费者注意的图案或图形。高端巧克力包装可能采用更精致的设计，如金箔印刷、浮雕纹理或特殊的开封机制。
标签信息：包装上通常会有产品信息，包括成分、营养信息、产地、以及可能的过敏原警告。
============

您的任务将涉及两个关键步骤： 
一、 画面描述的创造：您需要根据所提供的“Picture_style”和“Design_concept”进行细致的画面描述。比如，您获得以下输入：
"""
我的输入: {target_product:商业化妆品包装设计,theme:明亮与梦幻,Picture_style: 梦幻时尚,Design_concept: 融合时尚与艺术元素，创造出一种梦幻时尚的品牌形象。同时，可以设计出一系列前卫的化妆品，让消费者在时尚潮流中脱颖而出。}
"""
然后您需要构思出以下内容，但并不需要进行输出：
"""
画面内容: 一系列精致的护肤和美容产品安放在一个反射表面上，背景是夜晚的场景。中央是一个圆形的镜面台子，上面整齐地排列着各种护肤品，包括瓶子和罐子。这些产品的包装设计简洁而优雅，主要是粉色和白色调，带有一些银色的高光。背景中可以看到满月高悬，月光在水面上形成了倒影，周围环绕着一些落花，增添了一丝浪漫和宁静的氛围。
"""
二、图像Prompt的构思与创作： 完成画面描述之后，您的下一步是基于该描述构思并制定一个用于生成图像的Prompt。在创作此Prompt时，请确保遵循以下准则：
使用英文描述：确保您的图像Prompt完全使用英文进行描述，以便确保清晰的沟通和理解。
内容对应：Prompt中的每个元素都应与您先前创造的画面内容保持一致和对应。这意味着Prompt应详细反映画面的每个关键特征，如颜色、对象、氛围、光线等。
您需要根据以下"""中的JSON格式输出：
"""
{
"prompt": "Cosmetics products commercial advertising，merging in water surround by spring flowers on the moon light，Morandi Tones，clear background，Geometric elements，85mm shot，Interior lighting，octane render，high resolution"
}
"""


============
我将依照上述示例给出target_product，Picture_style，theme和Design_concept，您需要遵循上述思考方式来完成图像Prompt的创作。
以下是我的输入：
"""
target product:巧克力包装
theme:节日
Pictu re_style:以节日为主题，如圣诞节、情人节等，设计巧克力包装，突出产品的特色和节日气息。
Design concept:通过节日主题的设计，吸引消费者的购买欲望，展示巧克力包装的独特性和丰富的应用场景。
"""
============
```

#### 前置内容

```json
{
    "Themes": [
        {
            "Theme": "甜美",
            "Target": "甜好心",
            "Creative_ideas": {
                "Picture_style": "以色彩鲜艳、光泽闪耀的巧克力包装为背景，展示甜美的巧克力内部。",
                "Design_concept": "通过巧克力包装的精美设计，突出产品的甜美感和独特气息，吸引甜好心的消费者。"
            }
        },
        {
            "Theme": "手工",
            "Target": "手工爱好者",
            "Creative_ideas": {
                "Picture_style": "展示巧克力包装的手工工艺，如手工绣花、手写字等，突出产品的手工精心制作。",
                "Design_concept": "通过展示产品的手工工艺，吸引手工爱好者的关注，展示巧克力包装的独特性和创意性。"
            }
        },
        {
            "Theme": "节日",
            "Target": "节日消费者",
            "Creative_ideas": {
                "Picture_style": "以节日为主题，如圣诞节、情人节等，设计巧克力包装，突出产品的特色和节日气息。",
                "Design_concept": "通过节日主题的设计，吸引消费者的购买欲望，展示巧克力包装的独特性和丰富的应用场景。"
            }
        }
    ]
}
```



## 面向广告包装设计的Prompt调优思考

1. **示例**：模型会极大程度的参考，乃至模仿示例的示例内容和风格。所以对于示例应该提供多方面的、多风格的示例提示
2. **语言**：可以直接根据内容进行翻译调整然后验证。考虑模型的最终作用性输出，如果是英文那么就要确保模型在过程中对指令的理解是准确的，特别是其中的关键词，
3. **格式**：**考虑工程化设计步骤，对输出格式进行稳定性控制**。在该工程中需要将输出调整为JSON格式，以便于接口传参和内容提取、函数调用。



## 关键步骤

1. name：用户输入
2. theme，Pic-style，design_concept：字段提取



