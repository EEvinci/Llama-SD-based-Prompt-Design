# One->many Arguments & One shot Prompt Design 以创意与受众为例

[toc]

## 设计背景

![广告包装设计](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/%E5%B9%BF%E5%91%8A%E5%8C%85%E8%A3%85%E8%AE%BE%E8%AE%A1.png)

基于广告包装设计的前端原型图，基于llama根据用户输入产品名称，给出不同类型的创意主体及其对应的受众人群和产品介绍。

## Json交互样例

### 草莓汁饮料

input：”产品名称“
output:	{"results":[{'title':" ", "category":" ", "introduction":" "}, 
								{'title':" ", "category":" ", "introduction":" "},
								{'title':" ", "category":" ", "introduction":" "}]}

```json
{
    "input": "草莓汁饮料",
    "output": {
        "results": [
            {
                "title": "纯净与活力",
                "category": "年轻人",
                "introduction": "这款包装设计以其鲜明的色彩和动感的图案吸引年轻人的目光。使用流线型和抽象艺术元素，传达出产品的现代感和活力。理想的选择，对于追求健康活力和生活品质的年轻消费者。"
            },
            {
                "title": "甜蜜的回忆",
                "category": "中年妇女",
                "introduction": "此设计以温馨的色调和经典的图案为特点，旨在唤起中年妇女心中的怀旧情怀。精致的花纹和柔和的色彩搭配让产品包装显得既优雅又亲切，非常适合喜欢传统与家庭价值观的消费者。"
            },
            {
                "title": "经典雅致",
                "category": "高端专业人士",
                "introduction": "这款包装专为高端专业人士设计，以其简约的风格和高质感的材料突显产品的精致与品质。深色调的背景搭配金色或银色的线条，传递出专业和成功的形象。"
            }
        ]
    }
}

Taking the above Json format as an example, please carry out creative and audience design on the products I gave.
Product name: 巧克力奶茶

Please note: 
1. Please avoid inappropriate and ambiguous words during the design process, such as "superior person", etc.
2. Category represents the group of people who use the product. The expression of the group should be realistic and rational to avoid problems such as inappropriate and vague expressions.
3. There should be no statements about product design and materials used in the Introduction section.
```



### 牛油果手提袋

```json
{
    "input": "牛油果手提袋",
    "output": {
        "results": [
            {
                "title": "都市绿洲",
                "category": "年轻都市人群",
                "introduction": "这款设计专为都市生活节奏而创，旨在提供一个方便携带且具有时尚感的购物解决方案。它强调易于存储和轻便性，以适应快节奏的都市生活，同时使用绿色元素来提醒用户健康饮食的重要性。"
            },
            {
                "title": "复古果园",
                "category": "中年妇女",
                "introduction": "这款包装专为重视家庭生活质量的中年妇女设计。它结合了复古美感与实用性，适合家庭聚会或市场购物等场合。该设计提倡慢生活，鼓励用户在购买和储存食物时更加注重品质和健康。"
            },
            {
                "title": "简约自然",
                "category": "环保意识者",
                "introduction": "此手提袋设计思路基于环保和可持续性原则。它旨在为那些热爱自然、支持环保的消费者提供一个既实用又环保的产品选项。该设计鼓励在各种场合，如购物或外出时，减少一次性塑料袋的使用，倡导环保生活方式。"
            }
        ]
    }
}
```

## Prompt命令语句

以上述Json格式为例，请对我给出的产品进行进行创意与受众设计
产品名称: **巧克力奶茶**

请注意: 
1. 在设计过程中请避免不当用词和歧义用词, 例如"上级人士"等
1. category需要严格对应产品使用人群, 避免表达不当和模糊等问题
1. Introduction部分不应出现对于产品设计和使用材料的表述



Taking the above Json format as an example, please carry out creative and audience design on the products I gave.
Product name: **巧克力奶茶**

Please note: 
1. Please avoid inappropriate and ambiguous words during the design process, such as "superior person", etc.
2. Category represents the group of people who use the product. The expression of the group should be realistic and rational to avoid problems such as inappropriate and vague expressions.
3. There should be no statements about product design and materials used in the Introduction section.

## new Prompt design

中文：

```prompt
你是一位广告创意设计专家，请你针对用户提出的产品对该款产品的广告设计主题、目标受众并给出创意思路。设计需要满足以下要求：
1、广告设计主题应具有鲜明的生活特点
2、目标受众应该细化到具体的人群
3、创意思路聚焦于画面风格设计建议

示例如下：
    输入：草莓果汁宣传效果图
    输出：
    {
        "Themes": [
            {
                "Theme": "$", 
                "Target": "$",
                "Creative_ideas": "$"
            }
        ]	
    }
我以$符号来表示你需要进行填充的内容，内容整体以json格式输出！！

用户提出的产品是：西瓜汁饮料宣传图
请根据用户输入产品进行3个创意设计
```

设计主题

- 并包含广告的画面细节描述
- 设计主题的创意思路给出直接的设计方案，对于广告的画面细节描述尽可能使用建议性文字



英文：

```prompt
You are an advertising creative design expert. Please provide creative ideas for the advertising design theme and target audience of this product based on the product proposed by the user. The design needs to meet the following requirements:
1. The theme of advertising design should have distinctive characteristics of life.
2. The target audience should be refined to specific groups of people
3. Creative ideas focus on picture style design suggestions

Examples are as follows:
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

I use the $ symbol to represent the content you need to fill, and the entire content is output in json format.


The product proposed by the user is: "牛油果手提袋宣传图设计". Please make 3 creative designs based on user input products. All content needs to be displayed in Chinese!!!All content needs to be displayed in Chinese! No Explanation.
```

