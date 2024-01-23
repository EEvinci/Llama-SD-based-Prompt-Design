# Directional Stimulus Prompting

[Li et al., (2023)(opens in a new tab)](https://arxiv.org/abs/2302.11520) proposes a new prompting technique to better guide the LLM in generating the desired summary.

A tuneable policy LM is trained to generate the stimulus/hint. Seeing more use of RL to optimize LLMs.

The figure below shows how Directional Stimulus Prompting compares with standard prompting. The policy LM can be small and optimized to generate the hints that guide a black-box frozen LLM.

![DSP](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdsp.27a0005f.jpeg&w=3840&q=75)

Image Source: [Li et al., (2023)(opens in a new tab)](https://arxiv.org/abs/2302.11520)

Full example coming soon!