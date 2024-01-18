# 图片生成Prompt交互数据流程——牛油果手提袋

## 设计文稿交互生成

### Prompt

```text
You are an advertising creative design expert. Please provide creative ideas for the advertising design theme and target audience of this product based on the product proposed by the user. 
The design needs to meet the following requirements:
1.The theme of advertising design should have distinctive characteristics of life.
2.The target audience should be refined to specific groups of people
3.Creative ideas focus on picture style design suggestions

Examples are as follows in """:
"""
Input: 草莓果汁宣传效果图
Output:
{
    "Themes": [
        {
            "Theme": "$",
            "Target": "$",
            "Creative_ideas": {
                "Picture_style": "$",
                "Design_concept": "$"
            }
        }
    ]
}
"""
I use the $ symbol to represent the content you need to fill, and the entire content is output in json format.

The product proposed by the user is: "牛油果手提袋宣传图设计". 
Please make 3 creative designs based on user input products. 
Please attention: All content needs to be displayed in Chinese!!! No Explanation.
```



### Model-Output

```json
{
    "Themes": [
        {
            "Theme": "时尚",
            "Target": "城市年轻人",
            "Creative_ideas": {
                "Picture_style": "拍摄现实生活场景，如街头、咖啡馆、商场等，展示牛油果手提袋在各种场合的实用性和时尚感。",
                "Design_concept": "突出产品的独特设计和材质，通过拍摄多角度的照片，展示牛油果手提袋的独特魅力，同时加入时尚元素，如流行服饰和配件，以吸引城市年轻人的关注。"
            }
        },
        {
            "Theme": "户外",
            "Target": "户外爱好者",
            "Creative_ideas": {
                "Picture_style": "拍摄户外环境，如山丘、海滩、森林等，展示牛油果手提袋在户外活动中的实用性和适应性。",
                "Design_concept": "突出产品的耐用性和防水性能，通过拍摄户外活动场景，展示牛油果手提袋在各种恶劣环境下的表现，以吸引户外爱好者的关注。"
            }
        },
        {
            "Theme": "简约",
            "Target": "简约追求者",
            "Creative_ideas": {
                "Picture_style": "简洁、清新的风格，通过对比牛油果手提袋与其他简约产品的运用场景，展示产品在简约生活中的价值。",
                "Design_concept": "突出产品的简约设计和轻便性，通过以简约风格为主的拍摄，展示牛油果手提袋在日常生活中的实用性，以吸引简约追求者的关注。"
            }
        }
    ]
}
```

## 图片生成交互生成

### Prompt

```text
作为一名prompt工程师，你拥有卓越的语言技能和深厚的艺术鉴赏能力。你擅长从各种内容中提炼精华，并创造出具有高度创意和吸引力的Prompt。在你的工作中，你不仅能够理解复杂的概念和细节，还能将它们转化为简洁、引人入胜的语言。你的这些技能使你在创造Prompt方面表现卓越，能够有效地激发和引导人工智能的创造性表达。

===========
水果和产品设计专家对牛油果手提袋宣传图中的牛油果和手提袋的外形特征描述如下:
牛油果：牛油果应该是成熟的，展示其典型的深绿色皮肤，可能带有一些深褐色的斑点。它的形状应该是椭圆形或类似梨形，底部略宽，顶部略尖。切开的牛油果部分应该展现出鲜亮的绿色果肉，中间带有一个大的圆形棕色种子。
手提袋：手提袋设计应简洁而时尚，可以采用环保材料制作，如再生纸或布料。袋子的颜色应该是自然的，可能是棕色或绿色，以呼应牛油果的色调。手提袋上可以有牛油果的图案或者与健康饮食相关的口号。袋子的尺寸应适中，方便携带，且足以装下几个牛油果。
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
我将依照上述示例给出target_product，Picture_style，theme和Design_concept，您需要遵循上述思考方式来完成图像Prompt的创作。


以下是我的输入：
"""
target_product:牛油果手提袋设计
theme:时尚
Picture_style: 拍摄现实生活场景，如街头、咖啡馆、商场等，展示牛油果手提袋在各种场合的实用性和时尚感。,
Design_concept: 突出产品的独特设计和材质，通过拍摄多角度的照片，展示牛油果手提袋的独特魅力，同时加入时尚元素，如流行服饰和配件，以吸引城市年轻人的关注。
"""
```

### Model-Output

```text
Fashionable and practical design of a kiwi handbag in various urban settings, showcasing its unique style and material, while incorporating fashion elements like trendy clothing and accessories to attract the attention of young urbanites. Capture the essence of street style with a realistic photography approach, using a 35mm shot and natural lighting. Use an interior lighting setup to highlight the product's unique features. High resolution.
```

## SD出图

![image (47)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(47).png)

![image (46)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(46).png)

![image (45)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(45).png)

![image (44)](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image%20(44).png)