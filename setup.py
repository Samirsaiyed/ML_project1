#from xml.etree.ElementTree import VERSION
from setuptools import setup
from typing import List

# Declare the varibles for setup fucntions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Samir Saiyed"
DESCRIPTION="This is a first Project for Machine eEarning"
PACKAGES=["housing"] 
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description : This function i going to return list of requirement mention in requiements.txt fie

    return this function is going to return a list which contain name of libraries mentioned in requirements.txt file
    """

    with open(REQUIREMENT_FILE_NAME) as  requirement_file:
      return requirement_file.readlines()


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()

)
