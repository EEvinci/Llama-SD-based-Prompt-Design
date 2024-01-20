# 广告投放建议Prompt

## Prompt-无产品字段输入

```text
Conduct a concise analysis of the image for advertising purposes, covering four key aspects. It's crucial to structure your response precisely in the JSON format provided below:

Image Content Analysis: Examine and summarize the main visual elements and themes in the image.
Cultural Elements Evaluation: Analyze cultural aspects in the image and their relevance to the target audience.
Ad Compliance Review: Check for any elements that may not align with standard advertising guidelines.
Optimization Recommendations: Offer suggestions to optimize the image for ad usage.
Your response must strictly follow this JSON format:
{
"Image Content Analysis": "[Insert brief analysis here]",
"Cultural Elements Evaluation": "[Insert cultural assessment here]",
"Ad Compliance Review": "[Insert compliance insights here]",
"Optimization Recommendations": "[Insert suggested improvements here]"
}
Pay close attention to the format: each analysis should be a concise statement placed within the quotation marks following the corresponding label.
```

![image-20240118191347909](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image-20240118191347909.png)

## 输出

```json
{
    "Image Content Analysis": "The image features a jar of cream placed on a table, surrounded by pink flowers. The flowers are in the foreground, while the jar of cream is in the background. The overall composition of the image is visually appealing and highlights the cream as the main subject.",
    "Cultural Elements Evaluation": "The image uses a combination of pink flowers and a jar of cream to create a visually appealing composition. The choice of pink flowers may evoke a sense of femininity and elegance, which could be appealing to a target audience interested in beauty and skincare products. The use of flowers in advertising is a common practice, as they are often associated with positive emotions and can help create a sense of freshness and vitality.",
    "Ad Compliance Review": "The image does not contain any explicit or offensive content, and it is likely to comply with standard advertising guidelines. However, it is essential to ensure that the advertisement does not make any false or misleading claims about the product's benefits or features.",
    "Optimization Recommendations": "To optimize the image for ad usage, consider adding a clear and concise message about the product's benefits or features. This could be achieved by adding text or a small sign near the jar of cream. Additionally, ensure that the image is visually appealing and well-lit, as this can help attract the attention of potential customers."
}
```

```text
{
     “图像内容分析”：“图像中一罐奶油放在桌子上，周围是粉红色的花朵。花朵在前景，而一罐奶油在背景。图像的整体构图在视觉上很吸引人 并突出奶油作为主要主题。",
     “文化元素评价”：“图像使用粉红色花朵和一罐奶油的组合来创造视觉上吸引人的构图。粉红色花朵的选择可能会唤起女性气质和优雅感，这可能会吸引感兴趣的目标受众 在美容和护肤产品中。在广告中使用鲜花是一种常见的做法，因为它们往往与积极的情绪联系在一起，有助于营造一种清新和活力的感觉。”,
     《广告合规审查》：“图片不包含任何露骨或冒犯性内容，很可能符合标准广告准则。但是，必须确保广告不会对产品的用途做出任何虚假或误导性声明。 优点或功能。",
     “优化建议”：“要优化广告使用的图像，请考虑添加有关产品优点或功能的清晰简洁的信息。这可以通过在奶油罐附近添加文字或小标志来实现。此外，请确保 图像具有视觉吸引力且光线充足，因为这有助于吸引潜在客户的注意力。”
}
```

## Prompt-有产品字段输入

"Start your analysis by specifying the **[Product Name]** featured in the image. This information is crucial for a targeted analysis in advertising context. Then, address the following areas in your analysis, structuring your response in the JSON format provided:

1. **Image Content Analysis**: Based on the product, summarize the main visual elements and themes in the image.
2. **Cultural Elements Evaluation**: Analyze the cultural aspects in relation to the product and its relevance to the target audience.
3. **Ad Compliance Review**: Assess any compliance issues considering the product and standard advertising guidelines.
4. **Optimization Recommendations**: Suggest ways to optimize the image for advertising, focusing on the product.

Structure your analysis as follows:

{
   "Image Content Analysis": "[Insert brief analysis]",
   "Cultural Elements Evaluation": "[Insert cultural assessment]",
   "Ad Compliance Review": "[Insert compliance insights]",
   "Optimization Recommendations": "[Insert suggested improvements]"
}

Pay close attention to the format: each analysis should be a concise statement placed within the quotation marks following the corresponding label.

### 输出

```json
{
    "Image Content Analysis": "The image features a jar of toning with a purple lid, surrounded by pink flowers. The flowers are in the foreground, while the jar is in the background. The overall scene is visually appealing and showcases the product in a natural, aesthetically pleasing setting.",
    "Cultural Elements Evaluation": "The use of pink flowers and a purple jar in the image may suggest a connection to femininity or a preference for soft, delicate colors. This could be appealing to a target audience that values such aesthetics or associates them with the product's purpose or brand.",
    "Ad Compliance Review": "The image does not contain any explicit or inappropriate content, and it is likely to comply with standard advertising guidelines. However, it is essential to ensure that the product's labeling and any accompanying text are clear, accurate, and comply with relevant regulations.",
    "Optimization Recommendations": "To optimize the image for advertising, consider adding a clear, concise message or tagline that highlights the product's benefits or unique features. Additionally, ensure that the product's labeling is clearly visible and legible, and consider using a contrasting color or font to make it stand out against the background."
}
```

