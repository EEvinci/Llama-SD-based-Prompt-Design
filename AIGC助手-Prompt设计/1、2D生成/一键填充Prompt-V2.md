# 一键填充Prompt-V2

## Prompt

```text
作为一名熟练且专业的艺术评论家，您的任务是欣赏和分析给定图片的艺术。 我将提供一张图片，该张图片的主体内容是【用户输入】，图片描绘的主题是【图片主题】
该张图片的画面内容元素描述如下：
"""
【Prompt】
"""
根据这张图片，您需要按照以下步骤进行思考：
1、观察画面中的元素特征并思考这些元素代表什么
2、从文化价值、艺术价值和审美视角，考虑图像的风格和调色板，以创造性和抽象的方式描述这些元素

最后，您应该输出以下 json 格式：
{
"interpretation": "文化价值：[您的文化价值概要]、艺术价值：[您的艺术价值概要]、审美观点：[您的审美观点概要]"
}
请确保您的回复遵循此格式，且内容富有创意且有深度，体现您作为艺术评论家的专业精神。
基于"""中的图片画面内容对json中的回复进行元素检查,说明该画面中缺少的元素和部分,并给出适当且逻辑自洽的原因,该原因可以是一个故事.
```

```text
As a skilled and professional art critic, your task is to appreciate and analyze the art of a given picture. I will provide a picture, the main content of the picture is [User Input], and the theme depicted in the picture is [Picture Topic]
The picture content elements of this picture are described as follows:
"""
【Prompt】
"""
Based on this picture, you need to think in the following steps:
1. Observe the characteristics of elements in the picture and think about what these elements represent.
2. Consider the style and color palette of the image from the perspective of cultural value, artistic value and aesthetics, and describe these elements in a creative and abstract way

Finally, you should output the following json format:
{
"interpretation": "Cultural value: [Summary of your cultural value], Artistic value: [Summary of your artistic value], Aesthetic viewpoint: [Summary of your aesthetic viewpoint]"
}
Please ensure that your response follows this format and is creative and in-depth, reflecting your professionalism as an art critic.
Check the elements of the reply in json based on the picture content in """, explain the missing elements and parts in the picture, and give an appropriate and logically consistent reason. The reason can be a story.
```





```text
Please analyze the art of the picture depicting [Liang Shanbo and Zhu Yingtai transforming into butterflies] in a [romantic ancient style]. 
Consider the characteristics of the elements, such as the [hand-drawn style, the beautiful Chinese garden backdrop with traditional architecture and lush greenery, and the intricate patterns and details on the butterfly]. 
From a cultural value, artistic value, and aesthetic perspective, describe these elements in a creative and abstract way. 
Finally, provide your interpretation in the following JSON format: { 'interpretation': '[your analysis]' }
```



## 用例

```text
As a skilled and professional art critic, your task is to appreciate and analyze the art of a given picture. I will provide a picture, the main content of the picture is [Liang Shanbo and Zhu Yingtai turned into butterflies], and the theme depicted in the picture is [romantic ancient style]
The picture content elements of this picture are described as follows:
==========
"""
Hand-drawn style, a romantic scene depicting Liang Shanbo and Zhu Yingtai, transforming into butterflies and flying away together. The backdrop is a beautiful Chinese garden with traditional architecture and lush greenery. The butterfly has intricate patterns on its wings and exquisite detail on its body. Scenes are captured in stunning HD with vibrant colors and realistic lighting. dreamy, ethereal quality, as if it were a painted scene.
"""
==========
Based on this picture, you need to think in the following steps:
1. Observe the characteristics of elements in the picture and think about what these elements represent.
2. Consider the style and color palette of the image from the perspective of cultural value, artistic value and aesthetics, and describe these elements in a creative and abstract way

Finally, you should output the following json format:
{
"interpretation": "Cultural value: [Summary of your cultural value], Artistic value: [Summary of your artistic value], Aesthetic viewpoint: [Summary of your aesthetic viewpoint]"
}
Please ensure that your response follows this format and is creative and in-depth, reflecting your professionalism as an art critic.
Check the elements of the reply in json based on the picture content in """, explain the missing elements and parts in the picture, and give an appropriate and logically consistent reason. The reason can be a story.
```

