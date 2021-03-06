import os
from setuptools import setup, find_packages
from importlib.machinery import SourceFileLoader


module_name = "nonocaptcha"

module = SourceFileLoader(
    module_name, os.path.join(module_name, "__init__.py")
).load_module()


def load_requirements(fname):
    """ load requirements from a pip requirements file """
    with open(fname) as f:
        line_iter = (line.strip() for line in f.readlines())
        return [line for line in line_iter if line and line[0] != "#"]


setup(
    name=module_name.replace("_", "-"),
    version=module.__version__,
    author=module.__author__,
    author_email=module.authors_email,
    license=module.__license__,
    description=module.package_info,
    long_description=open("README.md").read(),
    platforms="all",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(),
    install_requires=load_requirements("requirements.txt"),
)
