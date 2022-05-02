# simple-onnx-processing-tools
A set of simple tools for splitting, merging, OP deletion, size compression, rewriting attributes and constants, OP generation, change opset, change to the specified input order, and RGB to BGR conversion for ONNX models.

[![Downloads](https://static.pepy.tech/personalized-badge/simple-onnx-processing-tools?period=total&units=none&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/simple-onnx-processing-tools) ![GitHub](https://img.shields.io/github/license/PINTO0309/simple-onnx-processing-tools?color=2BAF2B) [![PyPI](https://img.shields.io/pypi/v/simple-onnx-processing-tools?color=2BAF2B)](https://pypi.org/project/simple-onnx-processing-tools/)

<p align="center">
  <img src="https://user-images.githubusercontent.com/33194443/162783149-3b0d6e25-44da-4bc1-89fb-beae8aeae31d.png" />
</p>

## 1. Tools
```bash
$ pip install simple-onnx-processing-tools \
&& pip install -U onnx \
&& python3 -m pip install -U onnx_graphsurgeon --index-url https://pypi.ngc.nvidia.com
```
```bash
$ docker run --rm -it \
-v `pwd`:/workdir \
-w /workdir \
pinto0309/simple-onnx-processing-tools:1.0.2
```

|No.|Tool Name|Tags|Summary|
|:-:|:-|:-:|:-|
|1|**[snc4onnx](https://github.com/PINTO0309/snc4onnx)**|[![PyPI](https://img.shields.io/pypi/v/snc4onnx?color=2BAF2B)](https://pypi.org/project/snc4onnx/)[![snc](https://img.shields.io/github/stars/PINTO0309/snc4onnx.svg?style=social)](https://github.com/PINTO0309/snc4onnx)|Simple tool to combine(merge) onnx models. **S**imple **N**etwork **C**ombine Tool for **ONNX**.|
|2|**[sne4onnx](https://github.com/PINTO0309/sne4onnx)**|[![PyPI](https://img.shields.io/pypi/v/sne4onnx?color=2BAF2B)](https://pypi.org/project/sne4onnx/)[![sne](https://img.shields.io/github/stars/PINTO0309/sne4onnx.svg?style=social)](https://github.com/PINTO0309/sne4onnx)|A very simple tool for situations where optimization with onnx-simplifier would exceed the Protocol Buffers upper file size limit of 2GB, or simply to separate onnx files to any size you want. **S**imple **N**etwork **E**xtraction for **ONNX**.|
|3|**[snd4onnx](https://github.com/PINTO0309/snd4onnx)**|[![PyPI](https://img.shields.io/pypi/v/snd4onnx?color=2BAF2B)](https://pypi.org/project/snd4onnx/)[![snd](https://img.shields.io/github/stars/PINTO0309/snd4onnx.svg?style=social)](https://github.com/PINTO0309/snd4onnx)|Simple node deletion tool for onnx. **S**imple **N**ode **D**eletion for **ONNX**.|
|4|**[scs4onnx](https://github.com/PINTO0309/scs4onnx)**|[![PyPI](https://img.shields.io/pypi/v/scs4onnx?color=2BAF2B)](https://pypi.org/project/scs4onnx/)[![scs](https://img.shields.io/github/stars/PINTO0309/scs4onnx.svg?style=social)](https://github.com/PINTO0309/scs4onnx)|A very simple tool that compresses the overall size of the ONNX model by aggregating duplicate constant values as much as possible. **S**imple **C**onstant value **S**hrink for **ONNX**.|
|5|**[sog4onnx](https://github.com/PINTO0309/sog4onnx)**|[![PyPI](https://img.shields.io/pypi/v/sog4onnx?color=2BAF2B)](https://pypi.org/project/sog4onnx/)[![sog](https://img.shields.io/github/stars/PINTO0309/sog4onnx.svg?style=social)](https://github.com/PINTO0309/sog4onnx)|Simple ONNX operation generator. **S**imple **O**peration **G**enerator for **ONNX**.|
|6|**[sam4onnx](https://github.com/PINTO0309/sam4onnx)**|[![PyPI](https://img.shields.io/pypi/v/sam4onnx?color=2BAF2B)](https://pypi.org/project/sam4onnx/)[![sam](https://img.shields.io/github/stars/PINTO0309/sam4onnx.svg?style=social)](https://github.com/PINTO0309/sam4onnx)|A very simple tool to rewrite parameters such as attributes and constants for OPs in ONNX models. **S**imple **A**ttribute and Constant **M**odifier for **ONNX**.|
|7|**[soc4onnx](https://github.com/PINTO0309/soc4onnx)**|[![PyPI](https://img.shields.io/pypi/v/soc4onnx?color=2BAF2B)](https://pypi.org/project/soc4onnx/)[![sam](https://img.shields.io/github/stars/PINTO0309/soc4onnx.svg?style=social)](https://github.com/PINTO0309/soc4onnx)|A very simple tool that forces a change in the opset of an ONNX graph. **S**imple **O**pset **C**hanger for **ONNX**.|
|8|**[scc4onnx](https://github.com/PINTO0309/scc4onnx)**|[![PyPI](https://img.shields.io/pypi/v/scc4onnx?color=2BAF2B)](https://pypi.org/project/scc4onnx/)[![sam](https://img.shields.io/github/stars/PINTO0309/scc4onnx.svg?style=social)](https://github.com/PINTO0309/scc4onnx)|Very simple NCHW and NHWC conversion tool for ONNX. Change to the specified input order for each and every input OP. Also, change the channel order of RGB and BGR. **S**imple **C**hannel **C**onverter for **ONNX**.|
|9|**[sna4onnx](https://github.com/PINTO0309/sna4onnx)**|[![PyPI](https://img.shields.io/pypi/v/sna4onnx?color=2BAF2B)](https://pypi.org/project/sna4onnx/)[![sog](https://img.shields.io/github/stars/PINTO0309/sna4onnx.svg?style=social)](https://github.com/PINTO0309/sna4onnx)|Simple node addition tool for onnx. **S**imple **N**ode **A**ddition for **ONNX**.|
|10|**[components_of_onnx](https://github.com/PINTO0309/components_of_onnx)**|[WIP][![PyPI](https://img.shields.io/pypi/v/components_of_onnx?color=2BAF2B)](https://pypi.org/project/components_of_onnx/)[![sog](https://img.shields.io/github/stars/PINTO0309/components_of_onnx.svg?style=social)](https://github.com/PINTO0309/components_of_onnx)|ONNX parts yard. The various operations described in [Operator Schemas](https://github.com/onnx/onnx/blob/main/docs/Operators.md) are converted in advance into OP stand-alone ONNX files.|
|11|**[onnx2json](https://github.com/PINTO0309/onnx2json)**|[![PyPI](https://img.shields.io/pypi/v/onnx2json?color=2BAF2B)](https://pypi.org/project/onnx2json/)[![onnx2json](https://img.shields.io/github/stars/PINTO0309/onnx2json.svg?style=social)](https://github.com/PINTO0309/onnx2json)|Exports the ONNX file to a JSON file.|
|12|**[json2onnx](https://github.com/PINTO0309/json2onnx)**|[![PyPI](https://img.shields.io/pypi/v/json2onnx?color=2BAF2B)](https://pypi.org/project/json2onnx/)[![sog](https://img.shields.io/github/stars/PINTO0309/json2onnx.svg?style=social)](https://github.com/PINTO0309/json2onnx)|Converts a JSON file to an ONNX file.|

## 2. Acknowledgments
1. https://github.com/onnx/onnx/blob/main/docs/PythonAPIOverview.md
2. https://docs.nvidia.com/deeplearning/tensorrt/onnx-graphsurgeon/docs/index.html
3. https://github.com/NVIDIA/TensorRT/tree/main/tools/onnx-graphsurgeon
4. https://github.com/onnx/onnx/blob/main/docs/Operators.md

## 3. References
1. https://github.com/PINTO0309/PINTO_model_zoo
