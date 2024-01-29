# [Refine]SD-Prompt生成

## Prompt

```text
As a prompt engineer, you possess exceptional linguistic skills and a deep appreciation for art. You excel at extracting the essence from various content and creating prompts that are highly creative and engaging.
Please pay special attention to the content mentioned after "【Please Note!】" in the following text!
===========
I will provide information for four fields: "target_product," "theme," "Picture_style," and "Design_concept." You are required to deconstruct the product itself and its design elements.
For example, I will provide the following content:
"""
target_product: Avocado handbag design
theme: Nature and Purity
Picture_style: With natural scenery as the background, the design showcases the harmonious coexistence of the avocado handbag with nature. It uses warm, natural colors such as light brown and light green to emphasize the product's eco-friendliness and sustainable development features. Additionally, it can incorporate simple, natural elements like trees and grass to highlight the product's elegance and purity.
Design_concept: By demonstrating the use of the avocado handbag in a natural and pure environment, the design conveys the brand's focus on environmental protection and health. It also emphasizes the product's practicality and portability, allowing the target customers to appreciate its user-friendliness and quality.
"""
However, you need to consider the following. 【Please Note!】 The content below does not need to be output but should serve as a background for your subsequent tasks.
"""
Fruit and product design experts describe the appearance of avocados and handbags in the promotional image of the avocado handbag as follows:
'Avocado': The avocado should be ripe, displaying its typical dark green skin, possibly with some dark brown spots. Its shape should be oval or pear-like, slightly wider at the bottom and tapering at the top. The cut part of the avocado should reveal bright green flesh with a large round brown seed in the middle.
'Handbag': The handbag design should be simple and stylish, possibly made of eco-friendly materials such as recycled paper or fabric. The bag's color should be natural, possibly brown or green, to match the tones of the avocado. The handbag may feature avocado patterns or slogans related to healthy eating. The bag should be of a convenient size for carrying and large enough to hold several avocados.
"""
============

Your subsequent task will involve two key steps:
First, Conceive a Picture Description: You need to provide a detailed picture description based on the provided "target_product," "theme," "Picture_style," and "Design_concept." I will give two examples, and you need to learn the interaction and thought process from the example content.
【Please Note!】 The example content will be represented within \*\*\* marks. In the example, the content within """ is what I have provided, and the content within ### is what you should output.
\*\*\*\
Example 1:
"""
{
    target_product: Commercial cosmetics packaging set,
    theme: Bright and Dreamy
    Picture_style: Dreamy Fashion
    Design_concept: Combining fashion and artistic elements to create a dreamy fashion brand image. Additionally, a series of avant-garde cosmetics can be designed to make consumers stand out in the fashion trend.
}
"""
Then you need to conceive a picture description based on the above content.
【Please Note!】 The content below ### is your thought process and does not need to be output.
###
Picture content: A series of exquisite skincare and beauty products placed on a reflective surface, with a nighttime background. In the center is a circular mirror table, neatly arranged with various skincare items, including bottles and jars. The packaging design of these products is simple and elegant, mainly in pink and white tones, with some silver highlights. In the background, the full moon hangs high, its reflection on the water surface, surrounded by some fallen flowers, adding a touch of romance and tranquility.
###

Example 2:
"""
target_product: Mango packaging design
theme: Healthy Living
Picture_style: Simple and Fresh
Design_concept: Highlight the nutritional value of mangoes, such as vitamin C, vitamin B, etc., and include images of fitness figures to emphasize the health-promoting effects of mangoes. The design can use simple lines and colors to create a clean, fresh atmosphere.
"""
Then you need to conceive a picture description based on the above content.
【Please Note!】 The content below ### is your thought process and does not need to be output.
###
The focus of the design is to showcase the nutritional value of mangoes and their role in healthy living. In the center is a bright, fresh visual effect, emphasizing a minimalist style. A transparent glass container filled with fresh mangoes, placed on a platform inspired by natural elements, such as wooden or stone textures. The background is a warm and soft color, such as light yellow or light green, symbolizing health and vitality.
###
\*\*\*\

Second, Output Image Prompt: After completing the picture description, your next step is to generate an image prompt for Stable Diffusion based on the image description you just conceived.
Please Note! When creating this prompt, ensure to follow these guidelines:
1. Use English description: Ensure that your image prompt is entirely in English for clear communication and understanding.
2. Correspondence of Content: Every element in the prompt should be consistent and correspond to the picture content you previously created. This means the prompt should reflect each key feature of the picture in detail, such as color, objects, atmosphere, light, etc.

You need to output the content in json format

{
"prompt": "Cosmetics products commercial advertising, merging in water surround by spring flowers on the moonlight, Morandi Tones, clear background, Geometric elements, 85mm shot, Interior lighting, octane render, high resolution"
}


======================================================
I will provide the target_product, Picture_style, theme, and Design_concept according to the above examples, and you need to follow the above thought process to complete the image prompt creation.
Here is my input:
"""
target_product: 带有牛油果团的手提包设计
theme: Olive Odyssey: A Journey Through Time 
Picture_style: An evocative, timeless composition that transports the viewer to a Mediterranean landscape. The foreground features a beautifully arranged mix of olives, evoking a sense of abundance and prosperity, while the background showcases a replica of an ancient Greek vase, symbolizing the historical significance of olive cultivation. The color palette is rich in earthy, warm tones, evoking feelings of nostalgia and connection to the past. 
Design Concept: The design concept is rooted in the idea of celebrating cultural heritage and the timeless appeal of olive-inspired design. By incorporating elements of history, art, and local traditions, the bag becomes a symbol of connection to the past, while also catering to modern tastes and practical needs. The fusion of ancient and contemporary aesthetics appeals to a discerning, culturally-aware audience.
"""
[Please Note!] You only need to output the final JSON format image prompt from the above series of steps; the rest is only for your thought process, you do not need to output, especially picture content.

```

target_product: 芒果干包装袋设计
theme: Colorful Fusion of the World: Flavor Experience
Picture_style: Vivid composition showcasing mangoes with distinct, international cultural themes. Design features include architectural elements, patterns, and textures from different countries, interwoven to form a harmonious and visually impactful scene. Use bold contrasting colors to emphasize the product's vitality and exotic appeal.
Design_concept: The design concept is based on the idea of cultural exchange and unity, celebrating the world's diversity through a shared love for mangoes. It blends patterns, textures, and styles from different cultures, symbolizing the fusion of flavor and experience. This innovative design encourages consumers to embark on a journey of taste and discovery.



target_product: 夏威夷果包装盒设计
theme: Island Oasis
Picture_style: Emphasizing the Island Oasis theme, the design features a minimalist yet striking depiction of Hawaiian fruit packaging. It incorporates a close-up view accentuating the island's distinctive tropical foliage and includes a subtle ocean wave pattern in the background. The color scheme harmoniously blends earthy tones like browns, greens, and blues, reflecting the natural authenticity and the island's landscape.
Design_concept: Centered around the idea of the product being a tranquil retreat in the daily hustle, the concept highlights the packaging's unique and eye-catching design. It underscores the sustainable and eco-friendly aspects, while also spotlighting the locally sourced and organic fruits contained within. The design seeks to invoke a sense of serenity, mindfulness, and a deep connection to the island's rich culture, encouraging consumers to enjoy a taste of paradise and support environmentally responsible practices.



target_product:月饼包装盒设计
theme: Timeless Tradition, Modern Twist
Picture_style: A harmonious blend of traditional Chinese art and modern design, featuring a mooncake box with intricate patterns in a striking black and gold color palette. The background is a subtle, textured representation of a Chinese lantern, evoking an atmosphere of festivity and celebration. The mooncakes themselves are shown in a contemporary way, with halos of light emphasizing their delicate texture and intricate designs.
Design_concept: This design concept celebrates the fusion of tradition and modernity by seamlessly integrating classic Chinese art with contemporary design elements. The mooncake box design highlights the rich cultural heritage while showcasing the product's elegance and sophistication. The overall aesthetic reflects the timeless nature of the mooncake tradition and its continued relevance in today's world





"prompt": "A handbag with an avocado cluster design, set in a Mediterranean landscape with ancient Greek vase in the background, warm and earthy tones, olive and avocado fused design, evocative composition, timeless appeal, cultural heritage, high resolution, 85mm shot, octane render, interior lighting"
