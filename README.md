# simple-onnx-processing-tools
A set of simple tools for splitting, merging, OP deletion, size compression, and OP generation for ONNX models.

<p align="center">
  <img src="https://user-images.githubusercontent.com/33194443/162783149-3b0d6e25-44da-4bc1-89fb-beae8aeae31d.png" />
</p>

## 1. Tools

|No.|Tool Name|Tags|Summary|
|:-:|:-|:-:|:-|
|1|**[snc4onnx](https://github.com/PINTO0309/snc4onnx)**|[![PyPI](https://img.shields.io/pypi/v/snc4onnx?color=2BAF2B)](https://pypi.org/project/snc4onnx/)[![snc](https://img.shields.io/github/stars/PINTO0309/snc4onnx.svg?style=social)](https://github.com/PINTO0309/snc4onnx)|Simple tool to combine(merge) onnx models. **S**imple **N**etwork **C**ombine Tool for **ONNX**.|
|2|**[sne4onnx](https://github.com/PINTO0309/sne4onnx)**|[![PyPI](https://img.shields.io/pypi/v/sne4onnx?color=2BAF2B)](https://pypi.org/project/sne4onnx/)[![sne](https://img.shields.io/github/stars/PINTO0309/sne4onnx.svg?style=social)](https://github.com/PINTO0309/sne4onnx)|A very simple tool for situations where optimization with onnx-simplifier would exceed the Protocol Buffers upper file size limit of 2GB, or simply to separate onnx files to any size you want. **S**imple **N**etwork **E**xtraction for **ONNX**.|
|3|**[snd4onnx](https://github.com/PINTO0309/snd4onnx)**|[![PyPI](https://img.shields.io/pypi/v/snd4onnx?color=2BAF2B)](https://pypi.org/project/snd4onnx/)[![snd](https://img.shields.io/github/stars/PINTO0309/snd4onnx.svg?style=social)](https://github.com/PINTO0309/snd4onnx)|Simple node deletion tool for onnx. **S**imple **N**ode **D**eletion for **ONNX**.|
|4|**[scs4onnx](https://github.com/PINTO0309/scs4onnx)**|[![PyPI](https://img.shields.io/pypi/v/scs4onnx?color=2BAF2B)](https://pypi.org/project/scs4onnx/)[![scs](https://img.shields.io/github/stars/PINTO0309/scs4onnx.svg?style=social)](https://github.com/PINTO0309/scs4onnx)|A very simple tool that compresses the overall size of the ONNX model by aggregating duplicate constant values as much as possible. **S**imple **C**onstant value **S**hrink for **ONNX**.|
|5|**[sog4onnx](https://github.com/PINTO0309/sog4onnx)**|[![PyPI](https://img.shields.io/pypi/v/sog4onnx?color=2BAF2B)](https://pypi.org/project/sog4onnx/)[![sog](https://img.shields.io/github/stars/PINTO0309/sog4onnx.svg?style=social)](https://github.com/PINTO0309/sog4onnx)|Simple ONNX operation generator. **S**imple **O**peration **G**enerator for **ONNX**.|
|6|**[sam4onnx](https://github.com/PINTO0309/sam4onnx)**|[![PyPI](https://img.shields.io/pypi/v/sam4onnx?color=2BAF2B)](https://pypi.org/project/sam4onnx/)[![sam](https://img.shields.io/github/stars/PINTO0309/sam4onnx.svg?style=social)](https://github.com/PINTO0309/sam4onnx)|A very simple tool to rewrite parameters such as attributes and constants for OPs in ONNX models. **S**imple **A**ttribute and Constant **M**odifier for **ONNX**.|

## 2. Acknowledgments
1. https://github.com/onnx/onnx/blob/main/docs/PythonAPIOverview.md
2. https://docs.nvidia.com/deeplearning/tensorrt/onnx-graphsurgeon/docs/index.html
3. https://github.com/NVIDIA/TensorRT/tree/main/tools/onnx-graphsurgeon

## 3. References
1. https://github.com/PINTO0309/PINTO_model_zoo
