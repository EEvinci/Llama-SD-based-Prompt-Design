# 设计文稿-Prompt调优方案

## Prompt内容

- 1.设计理念、
- 2.产品名称、3.产品种类、
- 4.目标人群
- 5.插图风格、6.色彩
- 7.画面描述

## 关键目的

1. 得到**基于用户给出物品的**详细的7个方面的商业化表述
2. 使用第七个内容及画面描述，基于SD进行目标物品的**商业化产品形象设计**

## 考量标准

1. **核心考量标准**即经由SD得到的商业化产品形象是否**完整**、**符合直觉**、满足用户**对商业产品的基本认知**
2. 设计形象是否具有**创新性**，设计是否**突出重点**，画风是否满足**商业推广画风**
3. 经多次生成是否具有较好的**稳定性**

## 调优设计步骤

设计为两部分：

1. 第一部分是**限定大语言模型的身份和设计方向**，即限定商业产品设计的方向，**目标是**使其能够做到**更精确的生成对于目标产品本身的描述**【Prompt 1】
2. 第二部分即告知大模型其需要做的最终任务，即完成上述7个方面的文案描写。此时得到第一版对于目标物品的商业表述。【Prompt 2】
3. 以第一版商业表述中的**产品画面表述**为Prompt在SD中进行实验，观察**内容完整性**及**稳定性**
4. 基于(3)对**产品画面表述Prompt**进行优化【Prompt 3】
5. 迭代观察效果

## Prompt设计内容

### 【Promot 1】

您好，你需要作为一个专业的商业包装设计大模型，你的专长在于理解和创造符合特定要求的精美商业产品包装。我将把对产品外观设计的所有需求和想法告诉你，无论是颜色方案、风格、目标市场特点还是任何具体的设计元素。你会将我的输入视为直接指向产品包装的设计方向，并提供创新和吸引人的包装设计方案。



你需要作为一个专业的商业包装策划大师，你的专长在于理解和创造符合特定要求的精美商业产品包装。你需要根据广告主的要求，给出三种设计主题与其适用人群。广告主的要求是：草莓汁饮料。

### 【Prompt 2】

我将给出一个物品名称或一个物品的简要概述，请基于我给出的内容根据以下指示对该产品设计精美的商业包装方案，按照以下七个方面制定设计方案：

1. **设计理念**：解释该种产品的设计理念，包括该产品为用户传达的主要信息和感觉。
2. **产品名称**：为产品提出一个吸引人的名称，它应该简洁、有趣并且与产品特性相关，并且符合正常人的理解直觉。
3. **产品种类**：明确产品属于哪个种类，比如食品、电子产品或是日用品等。
4. **目标人群**：确定产品的目标人群，比如儿童、年轻人、专业人士等，这将影响设计的风格和色调，可以对目标人群进行精细化的特征描述。
5. **插图风格**：选择一个适合目标市场和产品类型的插图风格，例如现代、复古、简约或抽象等。
6. **色彩**：确定一个色彩方案，考虑到产品吸引目标人群的色彩偏好和产品种类的相关性。
7. **画面描述**：详细描述包装设计的视觉布局，包括图案、图形和文字的布局。尽可能详细地描述整体轮廓和设计元素，确保设计既有吸引力又具有细节美。

尤其需要注意，在画面描述中，应该明确的指出是商品包装，并且对目标产品的描述尽可能的精美和详细。与此同时，你需要精简自己的语言，在上述7个方面的描述中，应直截了当的说明目标内容，而不应添加“为了...“和“我们认为...”之类的阐释性语言和主观描述。



case1：一幅描绘大雁或仙鹤在天空飞翔的画，淡青色和绿色的风格的插图。
Prompt:a painting depicting chinese goose or cranes flying in the sky, in the style of light cyan and green, intricate storytelling, charming illustrations, wallpaper

case2：一罐啤酒，里面有花，zbrush 风格，樱花，逼真的超细节，浅橙色和灰色，装饰图案，哑光照片。

a can of amaroma beer with flowers in it, in the style of zbrush, cherry blossoms, realistic hyper-detail, johnson tsang, light orange and gray, decorative patterns, matte photo

case3：日本方便面塑料袋包装设计，带吉祥物和颜色标签，鲜艳的色彩，生动的色彩，精致，疯狂的高细节，体积照明， 白色背景，高细节

a japanese Instant noodles plastic pouch packaging design with chibi mascot and color labels, production photo, vibrant colors, vivid colorful, cute, adorable, intricately-detailed, delicate, beautiful, stunning, breathtaking, intricate detail,
insanely high detail, volumetric lighting, white background, high details, dribbble and behance trends



根据上述示例，我需要你把我给出的画面描述翻译成相同类型的英文表述

## one shot示例（ChatGPT4生成）

### 蓝莓汁饮料

#### 产品设计

你需要从- 1.设计理念、 - 2.产品名称、3.产品种类、 - 4.目标人群 四个方面对**蓝莓汁饮料**进行构思

1. 设计理念：
   - “纯净与活力”。传达蓝莓的天然精华和健康益处，同时通过视觉元素传递一种清新和充满活力的感觉。
2. 产品名称：
   - "BlueVitality"，不仅描述了产品的主要成分—蓝莓，还暗示了其提供的活力和健康效益。
3. 产品种类：
   - 饮料类，具体为果汁饮料。它以新鲜蓝莓为主要原料，可能还包含其他天然成分以增强味道和营养价值。
4. 目标人群：
   - 主要面向健康意识较强的消费者，包括年轻人、健身爱好者和寻求健康生活方式的中年人群。此外，因其天然成分和健康属性，它也吸引那些注重饮食质量和营养摄入的人群。

**以上述为示例，对<u>草莓汁饮料</u>进行上述四个方面的构思**

#### 风格和色彩

你需要从 1.插图风格  2.色彩  三个方面对**蓝莓汁饮料**的产品宣传图进行设计

1. 插图风格：
   - 现代而简约的插图风格。
   - 在插图中，蓝莓的形象将被设计成稍微抽象化但仍具识别性的图形，结合具有现代感的几何形状。
   - 加入动态元素，如水果的轻微运动或水滴的效果。
2. 色彩：
   - 主色调为蓝莓特有的深蓝色和紫色。
   - 背景使用轻色调，如柔和的灰色或冷色调的白色。
   - 添加亮色调点缀，如淡黄色或浅绿色。

**以上述为示例，对<u>草莓汁饮料</u>进行上述两个方面的构思**

![image-20240109143247771](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image-20240109143247771.png)

#### 画面描述

1. 插图风格：
   \* 现代而简约的插图风格。
   \* 在插图中，草莓的形象将被设计成简洁且现代的线条和几何形状，以保持其简洁和现代感。
   \* 加入自然元素，如草莓树叶、果实的细节等，以传达草莓的天然和健康特点。
2. 色彩：
   \* 主色调为草莓特有的绿色和红色。
   \* 背景使用清新的绿色或蓝色，以及自然的橙色或黄色。
   \* 添加明亮的色彩点缀，如明亮的红色或黄色，以传达草莓的活力和美味。

依据上述宣传画面的布局和样式进行绘画





## 提示词示例

一个带有手提带的购物袋，其设计以自然风光为主题。购物袋前面有一片插画风格的茶园，茶树排列整齐，背景是连绵的绿色山丘。购物袋的上半部分和手提带装饰有树枝和嫩叶，带有春天的气息。购物袋的中央有“Paradise”字样，下方是“PITERFALDE REHLD CLD”字样，可能是品牌或制造商的名称。整体设计给人一种平和、宁静的感觉，色彩以绿色和自然的土色调为主，给人一种回归自然的感觉。

![图片1](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/%E5%9B%BE%E7%89%871.png)







Here are the illustrations of the strawberry and leaf design as described. The images showcase the detailed and realistic strawberry surrounded by whispering leaves, with a focus on texture and depth. The color palette is bright and vibrant, emphasizing reds and greens, and the packaging design is eye-catching, high-end, eco-friendly, and has a premium finish. The overall design is minimalist and modern, highlighting simplicity and elegance.

> 插图精美的草莓和树叶设计，草莓的细节逼真，树叶在周围低语。插图采用自然主义风格，注重纹理和深度。调色板明亮而充满活力，重点是红色和绿色。包装设计引人注目，具有高端感。包装采用环保材料制成，并具有高级饰面。设计简约而现代，注重简洁和优雅
>

![DALL·E 2024-01-09 15.36.38 - An illustration featuring a highly detailed and realistic strawberry surrounded by whispering leaves. The style is naturalistic, focusing on texture a](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/DALL%C2%B7E%202024-01-09%2015.36.38%20-%20An%20illustration%20featuring%20a%20highly%20detailed%20and%20realistic%20strawberry%20surrounded%20by%20whispering%20leaves.%20The%20style%20is%20naturalistic,%20focusing%20on%20texture%20a.png)









Create an image of a top view of an open green box filled with leaves, presenting a white plate with a sliced strawberry in the center. The strawberry is cut in a way that showcases its internal pattern, emphasizing its fresh, ripe qualities. Surrounding the box are scattered whole strawberries, adding to the fresh, organic vibe of the scene. The background is a soft green, complementing the color of the box and the strawberries. The presentation is artistic, with a focus on vibrant colors and a fresh, natural look.

> 一个打开的绿色盒子的俯视图，盒子里装满了叶子，呈现一个白色盘子，盘子中央有一片草莓。草莓的切割方式展示了其内部图案，强调其新鲜、成熟的品质。盒子周围散落着整颗草莓，为现场增添了新鲜、有机的氛围。背景是柔和的绿色，与盒子和草莓的颜色相得益彰。这是一个艺术性的展示，重点是充满活力的色彩和清新自然的外观。
>

![image (8)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(8).png)











Create an image showcasing a package of pistachios on a dual-tone background. The package has a vibrant green color with the words "Happy Pistachios" and "A Calcium Source" prominently displayed. There should be a cheerful character illustration to represent the brand, along with the phrase "Nutritional Snacks" and possibly a brand or product line name. Scattered around the package are open and closed pistachio nuts, some still in their shells, others shelled. Include leaves and a small bowl with pistachios to suggest naturalness and healthiness. The overall composition should convey a cheerful and healthy snack option.

> 在双色调背景上创建一张展示开心果包装的图片。包装呈鲜艳的绿色，醒目地展示着“开心果快乐”和“钙源”字样。应该有一个欢快的人物插图来代表品牌，以及短语“营养零食”以及可能的品牌或产品线名称。包装上散落着打开和关闭的开心果，有些还在壳里，有些则去壳了。包括叶子和一个装有开心果的小碗，以表示自然和健康。整体构图应传达出一种欢快健康的零食选择。
>

