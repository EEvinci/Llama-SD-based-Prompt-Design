# 设计文稿Prompt设计

## Prompt_无产品名称字段输入

```text
Analyze the image to create a design document. Address the following areas, and format your response in the specified JSON format:

Product Name: Determine the product's name and its relation to its features.
Design Concept: Explore the creativity and purpose behind the design.
Color Analysis: Describe the color scheme and its impact.
Composition Analysis: Examine the layout and how elements are arranged.
Content Interpretation: Analyze any text or symbols and their contribution to the design.

Structure your findings like this:
{
   "Product Name": "[Insight]",
   "Design Concept": "[Insight]",
   "Color Analysis": "[Insight]",
   "Composition Analysis": "[Insight]",
   "Content Interpretation": "[Insight]"
}
Keep each section brief and focused.
```

![image-20240118191347909](https://evinci.oss-cn-hangzhou.aliyuncs.com/img/image-20240118191347909.png)

### 输出

```json
{
"Product Name": "Collagen Booster",
"Design Concept": "The design of the product is meant to evoke a sense of freshness and youthfulness, with the use of purple and pink flowers as a symbol of beauty and vitality. The product is presented in a simple, clean container that highlights its natural ingredients and benefits.",
"Color Analysis": "The use of purple and pink flowers adds a touch of elegance and sophistication to the product, while the white background provides a clean and minimalist look. The combination of these colors creates a sense of freshness and vitality, which is in line with the product's purpose of promoting collagen production.",
"Composition Analysis": "The product is placed in the center of the image, with the flowers surrounding it. This arrangement draws attention to the product and creates a sense of harmony and balance in the composition. The use of flowers as a natural element adds depth and interest to the design, making it more visually appealing.",
"Content Interpretation": "The product's name, 'Collagen Booster', is clearly visible on the container, indicating its purpose and benefits. The use of natural ingredients and the emphasis on collagen production suggest that the product is focused on promoting healthy skin and a youthful appearance."
}
```

## Prompt——有产品名称字段

```text
"Given the image described as [产品名称], analyze it to create a focused design document. Address the following areas, and format your response in the JSON format provided:

Product Name: Based on the image, identify the product's name and how it reflects its characteristics.
Design Concept: Discuss the creative intent and purpose behind the product's design as seen in the image.
Color Analysis: Describe the color scheme evident in the image and its impact on the product's appeal.
Composition Analysis: Examine the arrangement of elements in the image and their effect on the overall design.
Content Interpretation: Analyze any noticeable text or symbols in the image and their relevance to the product.
Structure your analysis as follows:

{
   "Product Name": "[Your insight based on the image]",
   "Design Concept": "[Your insight based on the image]",
   "Color Analysis": "[Your insight based on the image]",
   "Composition Analysis": "[Your insight based on the image]",
   "Content Interpretation": "[Your insight based on the image]"
}
Remember to replace [产品名称] with a brief description of the image before starting your analysis. Keep your responses concise and directly related to the input description."
```

