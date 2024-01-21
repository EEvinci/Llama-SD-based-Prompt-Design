# 产品设计Prompt接口

## 设计主题接口

`http://192.168.2.98:9003/async_audience/submit_task`

```json
{
    "copilot_id":"pkgagent",
    "instruction":"牛油果手提袋设计",
    "style":"3d cartoon",
    "params":{
            "theme":"时尚復古",
            "Picture_style":"使用油画风格的图案，展现牛油果的纯天然色彩，同时加入復古的边缘效果，增加时尚感。",
            "Design_concept":":以牛油果为主题，结合復古元素，呈现出一种极具个性的时尚质感，引领潮流。"
    }
}
```



## SD-Prompt接口

`http://192.168.2.98:9003/async_audience/submit_task`

```json
{
     "copilot_id":"simple",
     "instruction":"草莓汁饮料包装设计",
     "style":"3d cartoon"
}
```