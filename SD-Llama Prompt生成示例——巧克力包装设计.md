# SD-Prompt生成模版示例——巧克力包装设计

## Prompt

```text
作为一名prompt工程师，你拥有卓越的语言技能和深厚的艺术鉴赏能力。你擅长从各种内容中提炼精华，并创造出具有高度创意和吸引力的Prompt。在你的工作中，你不仅能够理解复杂的概念和细节，还能将它们转化为简洁、引人入胜的语言。你的这些技能使你在创造Prompt方面表现卓越，能够有效地激发和引导人工智能的创造性表达。
请您重点关注我在下面内容中提到的“【请注意！】”后提到的内容！

您的任务将涉及两个关键步骤：
一、构思画面描述：您需要根据所提供的“target_product”、“theme”、“Picture_style”和“Design_concept”进行细致的画面描述。我会给出两个示例，您需要学习示例内容的交互方式和思考方式。
【请注意！】示例内容将会被表示在\*\*\*中。在示例中，"""中的内容是我给出的内容, 而###中的内容则是你应该输出的内容。
\*\*\*
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

## 输出

画面内容: 一堆手工制作的巧克力盒和包装在一个简约的木质台上摆放，台子上还有一些手工工艺品的样品，如手工绣花和手写字。背景是一片温暖的自然色调，如浅棕色或棕色，呈现出手工精心制作的感觉。光线来自于一个摄像机，拍摄出手工细节的细节。

```json
{
    "prompt": "Handmade chocolate packaging design，displaying handcrafted elements such as embroidered flowers and handwritten letters，on a wooden surface surrounded by natural tones like warm brown or beige，85mm shot，close-up，interior lighting，Octane Render，high resolution"
}
```

## SD出图

![image (74)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(74).png)

![image (77)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(77).png)

![image (76)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(76).png)

![image (73)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(73).png)

![image (71)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(71).png)

![image (70)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(70).png)

![image (69)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(69).png)

![image (67)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(67).png)

![image (66)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(66).png)

![image (65)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(65).png)

