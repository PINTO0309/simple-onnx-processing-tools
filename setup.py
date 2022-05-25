
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
        'snc4onnx >= 1.0.7',
        'sne4onnx >= 1.0.8',
        'snd4onnx >= 1.1.5',
        'scs4onnx >= 1.0.17',
        'sog4onnx >= 1.0.11',
        'sam4onnx >= 1.0.7',
        'soc4onnx >= 1.0.1',
        'scc4onnx >= 1.0.4',
        'sna4onnx >= 1.0.3',
        'sbi4onnx >= 1.0.3',
        'sor4onnx >= 1.0.1',
        'sit4onnx >= 1.0.4',
        'onnx2json >= 2.0.2',
        'json2onnx >= 2.0.1',
        'sed4onnx >= 1.0.1',
        'soa4onnx >= 1.0.2',
        'ssi4onnx >= 1.0.1',
    ],
    extras_require = {
        'full': ['onnx-simplifier'],
    },
)
