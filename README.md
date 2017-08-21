# PySampling
This repository contains functions to generate initial samples for experiment design

## Available Sampling methods
Right now only LHS method is available. I am working on adding other methods such as
factorial design, random etc.

LHS class is a wrapper around the lhs provided by the pyDOE library. The wrapper allows
you to specific a yaml file that has information about the parameters for which you want to
generate the sample space for. It can handle out of bound conditions; float and integer type parameters;
and different step sizes for the parameter ranges.

The sample space can be returned as a python array or a dictionary

## Dependencies
Install dependencies using `./dependencies.sh`

You might need to run the dependencies scripts with sudo, depending on the setup of your computer

## Usage
Specify the information about the parameter in a yaml file. Take a look at the sample.yaml for reference.

For usage reference take a look at example.py.

Try the LHS sampling using `python example.py`

### Work in Progress
- Adding setup.py to allow users to install and use it as library
- Add other sampling methods
