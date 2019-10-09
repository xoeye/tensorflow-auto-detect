from distutils.core import setup
from setuptools import find_packages
from subprocess import Popen
from subprocess import PIPE


VERSION = '1.13.1'

def has_gpu():
    try:
        p = Popen(["nvidia-smi"], stdout=PIPE)
        stdout, stderror = p.communicate()
        return True
    except Exception:
        return False


if has_gpu():
    install_requires.append(f"tensorflow-gpu=={VERSION}")
else:
    install_requires.append(f"tensorflow=={VERSION}")


setup(
    name="tensorflow-auto-detect",
    version=VERSION,
    author="Matt Eby",
    description="Tensorflow package to auto detect and install tensorflow or tensorflow-gpu based on CUDA availability.",
    url="https://github.com/xoeye/tensorflow-auto-detect",
    classifiers=(
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=install_requires
)
