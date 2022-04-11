# simple-onnx-processing-tools
A set of simple tools for splitting, merging, OP deletion, size compression, and OP generation for ONNX models.

## Tools

|No.|Tool Name|Summary|
|:-:|:-|:-|
|1|**[snc4onnx](https://github.com/PINTO0309/snc4onnx)**|Simple tool to combine(merge) onnx models. **S**imple **N**etwork **C**ombine Tool for **ONNX**.|
|2|**[sne4onnx](https://github.com/PINTO0309/sne4onnx)**|A very simple tool for situations where optimization with onnx-simplifier would exceed the Protocol Buffers upper file size limit of 2GB, or simply to separate onnx files to any size you want. **S**imple **N**etwork **E**xtraction for **ONNX**.|
|3|**[snd4onnx](https://github.com/PINTO0309/snd4onnx)**|Simple node deletion tool for onnx. **S**imple **N**ode **D**eletion for **ONNX**.|
|4|**[scs4onnx](https://github.com/PINTO0309/scs4onnx)**|A very simple tool that compresses the overall size of the ONNX model by aggregating duplicate constant values as much as possible. **S**imple **C**onstant value **S**hrink for **ONNX**.|
|5|[WIP] **[sog4onnx](https://github.com/PINTO0309/sog4onnx)**|Simple ONNX operation generator. **S**imple **O**peration **G**enerator for **ONNX**.|
