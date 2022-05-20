
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
        'snc4onnx >= 1.0.6',
        'sne4onnx >= 1.0.7',
        'snd4onnx >= 1.1.4',
        'scs4onnx >= 1.0.16',
        'sog4onnx >= 1.0.10',
        'sam4onnx >= 1.0.6',
        'soc4onnx >= 1.0.0',
        'scc4onnx >= 1.0.3',
        'sna4onnx >= 1.0.2',
        'sbi4onnx >= 1.0.2',
        'sor4onnx >= 1.0.0',
        'sit4onnx >= 1.0.3',
        'onnx2json >= 2.0.1',
        'json2onnx >= 2.0.0',
        'sed4onnx >= 1.0.0',
        'soa4onnx >= 1.0.1',
    ],
    extras_require = {
        'full': ['onnx-simplifier'],
    },
)
