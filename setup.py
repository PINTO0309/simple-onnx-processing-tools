
from setuptools import setup, find_packages
from os import path
import re

package_name="simple_onnx_processing_tools"
root_dir = path.abspath(path.dirname(__file__))

with open("README.md") as f:
    long_description = f.read()

with open(path.join(root_dir, package_name, '__init__.py')) as f:
    init_text = f.read()
    version = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)

setup(
    name=package_name,
    version=version,
    description=\
        "A set of simple tools for splitting, merging, OP deletion, "+
        "size compression, rewriting attributes and constants, "+
        "OP generation, change opset, change to the specified input order, "+
        "addition of OP, RGB to BGR conversion, change batch size, "+
        "batch rename of OP, and JSON convertion for ONNX models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Katsuya Hyodo",
    author_email="rmsdh122@yahoo.co.jp",
    url="https://github.com/PINTO0309/simple-onnx-processing-tools",
    license="MIT License",
    packages=find_packages(),
    platforms=["linux", "unix"],
    python_requires=">=3.6",
    install_requires = [
        'snc4onnx >= 1.0.9',
        'sne4onnx >= 1.0.10',
        'snd4onnx >= 1.1.6',
        'scs4onnx >= 1.0.18',
        'sog4onnx >= 1.0.14',
        'sam4onnx >= 1.0.11',
        'soc4onnx >= 1.0.2',
        'scc4onnx >= 1.0.5',
        'sna4onnx >= 1.0.6',
        'sbi4onnx >= 1.0.4',
        'sor4onnx >= 1.0.5',
        'sit4onnx >= 1.0.5',
        'onnx2json >= 2.0.3',
        'json2onnx >= 2.0.2',
        'sed4onnx >= 1.0.4',
        'soa4onnx >= 1.0.3',
        'sod4onnx >= 1.0.0',
        'ssi4onnx >= 1.0.2',
        'ssc4onnx >= 1.0.4',
        'sio4onnx >= 1.0.2',
        'svs4onnx >= 1.0.0',
        'onnx2tf >= 0.0.27',
        'sng4onnx >= 1.0.1',
        'sde4onnx >= 1.0.0',
    ],
    extras_require = {
        'full': [
            'onnx-simplifier',
            'rich',
        ],
    },
)
