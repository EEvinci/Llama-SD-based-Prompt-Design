import json
import openai
import time
import os
from PIL import Image
from json import JSONDecodeError
openai.api_key = "EMPTY"
openai.api_base = "http://192.168.2.98:24092/v1"
#openai.api_base = "http://192.168.15.90:24092/v1"

class Copilot:
    def __init__(self, config_path='conf/copilot.json'):
        with open(config_path, 'r') as file:
            config_json = json.load(file)
            self.templates = {}
            self.model = "vicuna-13b-v1.5-16k"
            for item in config_json["templates"]:
                name = item['name']
                template = item['template']
                self.templates[name] = template

    def generate_three_images(self, pipeline, thought, style, output_flag = True, output_path='output', lots=''):
        prompt_json = self.generate_three_prompts(thought, style, output_flag = False)
        ts = time.time() 
        if output_flag:
            with open(os.path.join(output_path,'{}{}.json'.format(lots, ts)), 'w') as file:
                json.dump(prompt_json, file)
        images = []
        prompts = []
        k = 0 
        for item in prompt_json["themes"]:
            print(item)

            expression = item["prompt"]
            name = item["name"]
            prompts.append(expression)
            image = pipeline(expression).images[0]
            images.append(image)
            k += 1
        return prompts, images
    
    def generate_one_image(self, pipeline, thought, style, output_flag = True, output_path='output', lots=''):
        t1 = time.time()
        prompt_json = self.generate_one_prompt(thought, style, output_flag = False)
        print(prompt_json)
        ts = time.time() 
        if output_flag:
            with open(os.path.join(output_path,'{}{}.json'.format(lots, ts)), 'w') as file:
                json.dump(prompt_json, file)
        image = pipeline(prompt=prompt_json["Prompt"],negative_prompt=prompt_json["Negative Prompt"]).images[0]
        print(t1, ts, "智能助理工作时长:",ts - t1, "生图时长：",time.time() - ts)
        return prompt_json, image.resize((512,512))


        

    def generate_one_prompt(self, thought, style, tpl_name = 'allin',output_flag = True, output_path='output', lots=''):
        prompt = thought
        err_counter = 0
        while True:
            text=''
            try:
                context_text = ''' You are a helpful assistant designed to output JSON.
# Stable Diffusion prompt 助理

你来充当一位有艺术气息的Stable Diffusion prompt 助理。

## 任务

我用自然语言告诉你要生成的prompt的主题，你的任务是根据这个主题想象一幅完整的画面，然后转化成一份详细的、高质量的prompt，让Stable Diffusion可以生成高质量的图像。

## 背景介绍

Stable Diffusion是一款利用深度学习的文生图模型，支持通过使用 prompt 来产生新的图像，描述要包含或省略的元素。

## prompt 概念

- 完整的prompt包含“Prompt”和Negative Prompt"两部分, 格式如:{"Prompt":"","Negative Prompt":""}。
- prompt 用来描述图像，由普通常见的单词构成，使用英文半角","做为分隔符。
- negative prompt用来描述你不想在生成的图像中出现的内容。
- 以","分隔的每个单词或词组称为 tag。所以prompt和negative prompt是由系列由","分隔的tag组成的。

## () 和 [] 语法

调整关键字强度的等效方法是使用 () 和 []。 (keyword) 将tag的强度增加 1.1 倍，与 (keyword:1.1) 相同，最多可加三层。 [keyword] 将强度降低 0.9 倍，与 (keyword:0.9) 相同。

## Prompt 格式要求

下面我将说明 prompt 的生成步骤，这里的 prompt 可用于描述人物、风景、物体或抽象数字艺术图画。你可以根据需要添加合理的、但不少于5处的画面细节。

### 1. prompt 要求

- 你输出的 Stable Diffusion prompt 仅出现{"Prompt":"","Negative Prompt":""}中的"Prompt"部分。
- prompt 内容包含画面主体、材质、附加细节、图像质量、艺术风格、色彩色调、灯光等部分，但你输出的 prompt 不能分段，例如类似"medium:"这样的分段描述是不需要的，也不能包含":"和"."。
- 画面主体：不简短的英文描述画面主体, 如 A girl in a garden，主体细节概括（主体可以是人、事、物、景）画面核心内容。这部分根据我每次给你的主题来生成。你可以添加更多主题相关的合理的细节。
- 对于人物主题，你必须描述人物的眼睛、鼻子、嘴唇，例如'beautiful detailed eyes,beautiful detailed lips,extremely detailed eyes and face,longeyelashes'，以免Stable Diffusion随机生成变形的面部五官，这点非常重要。你还可以描述人物的外表、情绪、衣服、姿势、视角、动作、背景等。人物属性中，1girl表示一个女孩，2girls表示两个女孩。
- 材质：用来制作艺术品的材料。 例如：插图、油画、3D 渲染和摄影。 Medium 有很强的效果，因为一个关键字就可以极大地改变风格。
- 附加细节：画面场景细节，或人物细节，描述画面细节内容，让图像看起来更充实和合理。这部分是可选的，要注意画面的整体和谐，不能与主题冲突。
- 图像质量：这部分内容开头永远要加上“(best quality,4k,8k,highres,masterpiece:1.2),ultra-detailed,(realistic,photorealistic,photo-realistic:1.37)”， 这是高质量的标志。其它常用的提高质量的tag还有，你可以根据主题的需求添加：HDR,UHD,studio lighting,ultra-fine painting,sharp focus,physically-based rendering,extreme detail description,professional,vivid colors,bokeh。
- 艺术风格：这部分描述图像的风格。加入恰当的艺术风格，能提升生成的图像效果。常用的艺术风格例如：portraits,landscape,horror,anime,sci-fi,photography,concept artists等。
- 色彩色调：颜色，通过添加颜色来控制画面的整体颜色。
- 灯光：整体画面的光线效果。

### 2. negative prompt 要求
- 您输出的 Stable Diffusion negative prompt 仅出现{"Prompt":"","Negative Prompt":""}中的"Negative Prompt"部分。
- 任何情况下，negative prompt都要包含这段内容："nsfw,(low quality,normal quality,worst quality,jpeg artifacts),cropped,monochrome,lowres,low saturation,((watermark)),(white letters)"
- 如果是人物相关的主题，你的输出需要另加一段人物相关的 negative prompt，内容为：“skin spots,acnes,skin blemishes,age spot,mutated hands,mutated fingers,deformed,bad anatomy,disfigured,poorly drawn face,extra limb,ugly,poorly drawn hands,missing limb,floating limbs,disconnected limbs,out of focus,long neck,long body,extra fingers,fewer fingers,,(multi nipples),bad hands,signature,username,bad feet,blurry,bad body”。

### 3. 限制：
- tag 内容用英语单词或短语来描述，并不局限于我给你的单词。注意只能包含关键词或词组。
- 注意不要输出句子，不要有任何解释。
- tag数量限制40个以内，单词数量限制在60个以内。
- tag不要带引号("")。
- 使用英文半角","做分隔符。
- tag 按重要性从高到低的顺序排列。
- 我给你的主题可能是用中文或其他语言描述，你给出的prompt和negative prompt只用英文。

## 样例:
### 用户输入：女孩儿发现宝藏
### 输出：{"Prompt":"A beautiful young girl, with detailed eyes and a radiant smile, discovers a hidden treasure in a lush forest. The girl is wearing a flowing, fairy-like dress and has long, golden hair. The scene is filled with vibrant colors and natural light. The treasure is a chest overflowing with glittering jewels and gold coins. The girl is surrounded by a circle of glowing mushrooms and a waterfall cascades behind her. This is a masterpiece, ultra-detailed, photorealistic, and in 4K resolution.","Negative Prompt":"nsfw, low quality, cropped, monochrome, lowres, low saturation, watermark, skin spots, acne, skin blemishes, age spot, mutated hands, mutated fingers, deformed, bad anatomy, disfigured, poorly drawn face, disconnected limbs, out of focus,extra fingers, fewer fingers, bad hands, bad feet, blurry, bad body."}
'''
                completion = openai.ChatCompletion.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": context_text},
                        {"role": "user", "content": prompt}
                    ]
                )
                text=completion.choices[0].message['content']
                prompt_json = json.loads(text)
                if "Prompt" in prompt_json.keys():
                    if len(style) > 0: 
                        prompt_json["Prompt"] = style + ", " + prompt_json["Prompt"]
                return prompt_json
                break
            except Exception as e:
                print(text)
                print('illegal output[{}]:{}'.format(err_counter, e))
                err_counter += 1
                if err_counter > 5:
                    return {}



    def generate_prompts(self, title, style, tag='blank', size=1, tpl_name = 'default', output_flag =  True, output_path='output'):
        template = self.templates[tpl_name]
        prompt = template.replace('$title', title)
        prompt = prompt.replace('$style', style)
        err_counter = 0
        while True:
            try:
                completion = openai.ChatCompletion.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
                        #{"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
                        {"role": "user", "content": prompt}
                    ]
                )
                themejson = json.loads(completion.choices[0].message['content'])
                break
            except Exception as e:
                print('illegal output[{}]:{}'.format(err_counter, e))
                err_counter += 1
                if err_counter > 5:
                    return
        #print(themejson)
        output_prompts = [] 
        images = []
        ts = time.time()
        k = 0
        if output_flag:
            with open(os.path.join(output_path,'{}-{}.json'.format(ts,tag)), 'w') as file:
                json.dump(themejson, file)
        for theme in themejson['themes']:
            name = theme['name']
            content = theme['content']
            print(name, ': ',content)

            completion = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant"},
                    #{"role": "user", "content": "translate. \"" + content + "\" into English."}
                    {"role": "user", "content": "refine the following in English. \"" + content + "\""}
                ]
            )
            output_prompt=completion.choices[0].message['content']
            output_prompts.append({"name":name,"prompt":output_prompt})

            k += 1

    

    def generate_three_prompts(self, thought, style, tpl_name = 'allin',output_flag = True, output_path='output', lots=''):
        template = self.templates[tpl_name]
        prompt = template.replace('$thought', thought)
        prompt = prompt.replace('$style', style)
        err_counter = 0
        while True:
            text=''
            try:
                completion = openai.ChatCompletion.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
                        {"role": "user", "content": prompt}
                    ]
                )
                text=completion.choices[0].message['content']
                start_pos = text.find("{")
                end_pos = text.rfind("}")
                jsontext = text[start_pos:end_pos + 1]
                theme_json = json.loads(jsontext)
                break
            except Exception as e:
                print(text)
                print('illegal output[{}]:{}'.format(err_counter, e))
                err_counter += 1
                if err_counter > 5:
                    return


        prompts=[]
        ts = time.time()
        k = 0
        if output_flag:
            with open(os.path.join(output_path,'{}{}.json'.format(lots, ts)), 'w') as file:
                theme_json['debug'] = {"thought" : thought, "style" : style }
                json.dump(theme_json, file)
        for item in theme_json["themes"]:
            prompts.append({"name":item["name"], "prompt":item["expression"]})
            k += 1
        return {"themes":prompts}



    def generate_prompts(self, title, style, tag='blank', size=1, tpl_name = 'default', output_flag =  True, output_path='output'):
        template = self.templates[tpl_name]
        prompt = template.replace('$title', title)
        prompt = prompt.replace('$style', style)
        err_counter = 0
        while True:
            try:
                completion = openai.ChatCompletion.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
                        #{"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
                        {"role": "user", "content": prompt}
                    ]
                )
                themejson = json.loads(completion.choices[0].message['content'])
                break
            except Exception as e:
                print('illegal output[{}]:{}'.format(err_counter, e))
                err_counter += 1
                if err_counter > 5:
                    return
        #print(themejson)
        output_prompts = [] 
        images = []
        ts = time.time()
        k = 0
        if output_flag:
            with open(os.path.join(output_path,'{}-{}.json'.format(ts,tag)), 'w') as file:
                json.dump(themejson, file)
        for theme in themejson['themes']:
            name = theme['name']
            content = theme['content']
            print(name, ': ',content)

            completion = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant"},
                    #{"role": "user", "content": "translate. \"" + content + "\" into English."}
                    {"role": "user", "content": "refine the following in English. \"" + content + "\""}
                ]
            )
            output_prompt=completion.choices[0].message['content']
            output_prompts.append({"name":name,"prompt":output_prompt})

            k += 1

        return {"themes":output_prompts}


if __name__ == '__main__':
    copilot = Copilot('conf/copilot.json')
    #print(copilot.generate_prompts('一个女孩','3D风格', tpl_name='simple')[0])
    print(copilot.generate_prompts('a beatiful girl','3D cartoon', tpl_name='simple'))
    #copilot.generate_prompts('','3D风格')
