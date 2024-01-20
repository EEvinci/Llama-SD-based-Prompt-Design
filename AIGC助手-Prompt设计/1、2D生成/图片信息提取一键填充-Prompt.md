# 一键填充助手Prompt

## 长Token版

```text
When you receive the image i give, analyze it by following these steps and structure your response in the specified format:

1. **Title Creation**: Develop a single phrase that encapsulates the style and essence of the image. This phrase should be succinct, capturing the atmosphere, content, or key theme of the picture in a few words.
   - Consider: 'What single phrase best summarizes the style and essence of the image?'
2. **Detailed Description**: Provide a comprehensive description of the image, focusing on the key elements such as characters, objects, and the setting. Note the details that stand out and contribute significantly to the image's composition.
   - Consider: 'What are the major components of this image, and how do they contribute to its overall appearance?'
3. **Identifying Tags**: Determine a set of single words that capture the key features or characteristics of the image. These tags should succinctly represent the most prominent and notable elements, such as mood, style, dominant themes, or unique attributes.
   - Consider: 'What single-word tags best describe the essential aspects of this image?'

Response Format: Structure your analysis in the following JSON format:

{
   "topic": "[analysis of the picture's title]",
   "description": "[description of the image]",
   "tag": ["tag1", "tag2", "tag3", ...]

}
```

### 输出

```json
{
    "title": "Flower and Skincare Product",
    "description": "The image features a close-up of a skincare product, possibly a cream or lotion, sitting on a table. The product is surrounded by a few pink flowers, creating a visually appealing and natural setting. The flowers are scattered around the product, with some located to the left, right, and above it. The overall atmosphere of the image is serene and inviting, showcasing the beauty of the skincare product and the flowers together.",
    "identifying_tags": [
        "skincare",
        "cream",
        "lotion",
        "flowers",
        "pink",
        "natural",
        "serene",
        "inviting"
    ]
}

```



## 短Token版

```text
When you receive the image i give, analyze it by following these steps and structure your response in the specified format:

1. **Title Creation**: Craft a single phrase that captures the image's style and essence.
   - Ask yourself: 'Which phrase summarizes the image's essence?'
2. **Description**: Briefly describe the image, focusing on important elements like characters and setting.
   - Ask yourself: 'What key elements define this image?'
3. **Tags**: Identify single-word tags that reflect the image's key features or characteristics.
   - Ask yourself: 'What tags best represent this image?'

Response Format: Structure your analysis in the following JSON format:

{
   "topic": "[analysis of the picture's title]",
   "description": "[description of the image]",
   "tag": ["tag1", "tag2", "tag3", ...]
}
```

### 输出

```json
{
    "topic": "A jar of cream with a flower on top",
    "description": "A jar of cream with a flower on top is placed on a table. The jar is surrounded by pink flowers, creating a beautiful and serene scene.",
    "tag": ["cream", "jar", "flower", "pink flowers", "table"]
}
```



## 输出



