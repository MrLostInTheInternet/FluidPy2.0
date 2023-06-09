from setuptools import setup, find_packages

VERSION = '0.1.108'
DESCRIPTION = 'FluidSim Circuits Analyzer & PLC ST Code Generator'

with open("FluidPyPLC/README.md", "r") as f:
    long_description = f.read()

# Setting up
setup(
    name="FluidPyPLC",
    version=VERSION,
    author="MrLostInTheInternet (Eugen Iofciu Vasile)",
    author_email="<eugen.iofciuvasile@hotmail.com>",
    license="GPLv3",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/MrLostInTheInternet/FluidPyPLC",
    packages=find_packages(),
    package_data={
        'FluidPyPLC': ['resources/config.json'],
    },
    include_package_data=True,
    install_requires=['PySimpleGUI', 'matplotlib', 'tk'],
    entry_points={
        'console_scripts': [
            'fluidpy = FluidPyPLC.f:main',
        ]},
    keywords=['python', 'plc', 'fluidsim', 'structured text', 'plc python', 'codesys', 'circuits', 'pneumatics', 'oleodynamics', 'plc programming'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

