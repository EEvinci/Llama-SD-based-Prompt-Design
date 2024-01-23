# [Refine]主题生成-Prompt

[toc]

## 【Refinement】Prompt

```text
You are an advertising creative design expert tasked with providing in-depth and artistic creative ideas for a product's advertising theme and target audience. Your designs must adhere to the following enhanced criteria:

Theme: Capture a theme that reflects vivid characteristics of everyday life.
Target Audience: Define the target audience with precision, including specific age groups and distinct characteristics or interests.
Creative Ideas: Generate detailed and artistically rich ideas for:
Picture Style: Describe the picture style in a vivid, elaborate manner, using artistic and imaginative language.
Design Concept: Provide a comprehensive and creative explanation of the design concept, focusing on unique and innovative elements.
For instance:

Input: Strawberry juice promotional image
Output:
{
    "Themes": [
        {
            "Theme": "Sun-Kissed Summer Refreshment",
            "Target": "Health-conscious young adults aged 18-35, especially those who enjoy outdoor activities and value natural ingredients",
            "Creative Ideas": {
                "Picture Style": "A dynamic composition featuring sunlit fields, with a foreground of fresh strawberries and dew drops, capturing the essence of a bright summer day. The color palette is dominated by vibrant reds and greens, creating a feeling of freshness and vitality.",
                "Design Concept": "The concept revolves around the theme of natural purity and energy. It integrates elements of nature and health, symbolizing the juice's organic origins and nutritional benefits through imagery of lush fields and active, happy individuals enjoying the juice in a sunlit, natural setting."
            }
        }
    ]
}

Now, apply this approach to create three creative designs for the user-proposed product: "牛油果手提袋设计." All descriptions should be detailed, vivid, and rich in artistic expression, and presented in English.
```

## Output

### 牛油果手提袋设计

```json
{
    "Themes": [
        {
            "Theme": "Botanical Bliss",
            "Target": "Nature-inspired fashionistas aged 25-40, who appreciate unique designs and sustainable materials",
            "Creative Ideas": {
                "Picture Style": "A whimsical arrangement of cow-print elements, intertwined with lush botanicals, creating a harmonious and visually striking composition. The color palette highlights earthy tones and natural greens, evoking a sense of connection to the environment."
            },
            "Design Concept": "The design concept embraces the juxtaposition between the bold, graphic cow-print and the delicate, organic botanicals, symbolizing the merging of urban style with natural aesthetics. The resulting design is a fashionable, eco-conscious statement piece that celebrates the beauty of nature and the unique allure of cow-print."
        }
    ],
    "Themes": [
        {
            "Theme": "Rustic Chic",
            "Target": "Vintage-loving individuals aged 30-50, who appreciate timeless elegance and craftsmanship",
            "Creative Ideas": {
                "Picture Style": "An artful melding of cow-print and distressed textures, reminiscent of aged leather, evoking a sense of nostalgia and worn character. The color palette incorporates warm, earthy tones and subtle, muted hues, creating a rich and nuanced visual experience."
            },
            "Design Concept": "This design concept pays homage to bygone eras, blending the iconic cow-print with the beauty of time-worn materials. The result is a sophisticated, vintage-inspired handbag that tells a story of artistry and enduring style, transcending fleeting trends and capturing the essence of rustic chic."
        }
    ],
    "Themes": [
        {
            "Theme": "Minimalist Moo",
            "Target": "Modern, design-savvy individuals aged 20-45, who appreciate clean lines and understated sophistication",
            "Creative Ideas": {
                "Picture Style": "A restrained, monochromatic cow-print, deconstructed into geometric shapes and patterns, creating a visually striking and contemporary composition. The color palette focuses on neutral tones and subtle textures, emphasizing the purity of the design."
            },
            "Design Concept": "This design concept reinterprets the classic cow-print through a minimalist lens, boiling it down to its essence and celebrating the power of clean, simple lines. The resulting handbag design is a masterclass in understated elegance, showcasing the timeless appeal of the cow-print while appealing to those who appreciate modern design."
        }
    ]
}
```

### 自行车配色设计

```json

{
    "Themes": [
        {
            "Theme": "Electric Energizer",
            "Target": "Tech-savvy urbanites aged 18-35, who value bright, bold colors and high-energy lifestyles",
            "Creative Ideas": {
                "Picture Style": "A striking, neon-infused color palette featuring electric blues, vibrant oranges, and luminous yellows, evoking a sense of dynamism and excitement. The design incorporates sleek, aerodynamic lines and futuristic details, creating a visually arresting image that captures the essence of modern urban life."
            },
            "Design Concept": "The design concept is centered around the idea of electrifying movement and energy, reflecting the dynamic spirit of the target audience. The bold colors and daring design elements work together to create a cutting-edge, high-performance bicycle that radiates vitality and embodies the pulse of the city."
        }
    ],
    "Themes": [
        {
            "Theme": "Whimsical Whirl",
            "Target": "Creative, playful individuals aged 25-45, who appreciate vibrant, dreamy colors and imaginative design elements",
            "Creative Ideas": {
                "Picture Style": "A vibrant, psychedelic color scheme featuring soft pastels, playful patterns, and whimsical details, creating a sense of carefree adventure and childlike wonder. The design incorporates organic shapes and flowing lines, emphasizing the joy and spontaneity of cycling."
            },
            "Design Concept": "The design concept celebrates the magic of cycling, capturing the essence of freedom and joy that comes with the experience. The whimsical, dreamy color palette and imaginative design elements combine to create a bicycle that transports the rider to a world of enchantment and unbridled imagination."
        }
    ],
    "Themes": [
        {
            "Theme": "Timeless Trail",
            "Target": "Nature-loving individuals aged 30-55, who appreciate classic, understated colors and timeless design elements",
            "Creative Ideas": {
                "Picture Style": "A subtle, earthy color palette featuring natural greens, browns, and blues, evoking a sense of harmony with the environment. The design incorporates clean lines, natural textures, and understated details, creating a visually balanced and elegant image that reflects the serene beauty of the great outdoors."
            },
            "Design Concept": "The design concept is centered around the idea of a harmonious connection to nature, reflecting the peace and tranquility that comes with exploring the great outdoors. The timeless, understated design elements work together to create a bicycle that celebrates the beauty of the natural world and encourages a mindful, intentional cycling experience."
        }
    ]
}
```

```json
{
  "Themes": [
    {
      "Theme": "电动劲能者",
      "Target": "18-35岁的科技潮人，他们喜欢明亮、大胆的色彩和高能量的生活方式",
      "Creative Ideas": {
        "Picture Style": "采用令人瞩目的霓虹色调，包括电动蓝、鲜艳的橙色和发光的黄色，唤起一种活力和兴奋感。设计融入了流线型、未来感的细节，创造出一幅抓人眼球的图像，捕捉了现代城市生活的精髓。",
        "Design Concept": "设计理念围绕着激活运动和能量的概念，反映了目标受众的动态精神。大胆的色彩和大胆的设计元素共同作用，创造出一款尖端的、高性能的自行车，散发出活力，体现了城市的脉搏。"
      }
    },
    {
      "Theme": "奇幻旋转",
      "Target": "25-45岁的创意、好玩的个体，他们欣赏生动、梦幻的色彩和富有想象力的设计元素",
      "Creative Ideas": {
        "Picture Style": "采用鲜艳的迷幻色彩方案，包括柔和的粉彩、俏皮的图案和奇思妙想的细节，营造出一种无忧无虑的冒险和孩童般的惊奇感。设计融入了有机形状和流畅的线条，强调骑行的乐趣和自发性。",
        "Design Concept": "设计理念庆祝骑行的魔力，捕捉了骑行带来的自由和欢乐的本质。梦幻般的色彩和丰富的想象设计元素结合，创造出一款自行车，将骑手带入一个充满魔力和无限想象的世界。"
      }
    },
    {
      "Theme": "经典小径",
      "Target": "30-55岁爱好自然的个体，他们欣赏经典、低调的色彩和永恒的设计元素",
      "Creative Ideas": {
        "Picture Style": "采用低调的、自然的色调，包括自然的绿色、棕色和蓝色，唤起与环境和谐相处的感觉。设计融入了简洁的线条、自然质感和低调的细节，创造出一种视觉上平衡而优雅的图像，反映了大自然宁静的美。",
        "Design Concept": "设计理念围绕着与自然和谐相连的概念，反映了在大自然中探索所带来的平静和宁静。永恒、低调的设计元素共同作用，创造出一款自行车，庆祝自然界的美丽，鼓励一种专注、有意识的骑行体验。"
      }
    }
  ]
}

```

### 巧克力手提袋设计

```json
{
  "Themes": [
    {
      "Theme": "奢华巧克力享受",
      "Target": "适合所有年龄段的巧克力爱好者，他们欣赏高品质和在甜点及糖果中添加的一丝优雅",
      "Creative Ideas": {
        "Picture Style": "一幅奢侈的、特写的丰富、光滑巧克力图像，突出其丝滑质地和诱人香气。背景微微模糊，增添一种精致感觉，巧克力色调从深沉奢华的棕色到温暖的金色，引发舒适和放纵的感觉。",
        "Design Concept": "设计理念围绕着奢华和感官体验的概念。它结合了巧克力浓郁风味的吸引力、工艺和它所创造的情感联系，同时融入奢华和优雅的视觉元素。"
      }
    },
    {
      "Theme": "趣味巧克力冒险",
      "Target": "适合喜欢创意、可分享甜点的年轻家庭和孩子，他们享受探索和发现的乐趣",
      "Creative Ideas": {
        "Picture Style": "一个奇幻般的、灵感来源于幻想的场景，展示了各种巧克力创作，如迷你城堡、树木和动物，安排在郁郁葱葱的绿色景观中。巧克力颜色明亮生动，有鲜明的对比色调，营造出一种奇妙和兴奋的感觉。背景柔和聚焦，使巧克力创作成为焦点。",
        "Design Concept": "设计理念突出巧克力的想象力和探索性质，邀请观众踏上一个甜蜜、可食用创作的世界的愉快旅程。它庆祝分享和发现的快乐，同时强调产品的奇思妙想和趣味性。"
      }
    },
    {
      "Theme": "经典巧克力怀旧",
      "Target": "适合怀旧的成年人，他们欣赏传统的、经典的糖果和它们带来的舒适感",
      "Creative Ideas": {
        "Picture Style": "一个温馨怀旧的图像，展示了一个过去的经典巧克力盒子，轻轻打开，展露其丰富内容的一瞥。巧克力颜色从深沉、丰富的棕色到温暖的金色，引发舒适、熟悉和与过去的联系的感觉。背景微微模糊，聚焦于巧克力盒及其内容。",
        "Design Concept": "设计理念围绕着怀旧和舒适的概念，触及人们与传统巧克力糖果的情感联系。它庆祝巧克力的永恒吸引力和唤起美好回忆的能力，同时强调产品的经典和怀旧方面。"
      }
    }
  ]
}

```

