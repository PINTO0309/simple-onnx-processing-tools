
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
        "OP generation, and change opset for ONNX models.",
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
        'snc4onnx',
        'sne4onnx',
        'snd4onnx',
        'scs4onnx',
        'sog4onnx',
        'sam4onnx',
        'soc4onnx',
        'scc4onnx',
        'sna4onnx',
        'sbi4onnx',
        'sor4onnx',
        'onnx2json',
        'json2onnx',
    ],
)
