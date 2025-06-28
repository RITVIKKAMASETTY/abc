'''the steup.py file is a essential part of packing and distributing Python projects.
It specifies the metadata about the project, such as its name, version, author, etc.
It also specifies the packages and modules that should be included in the distribution,
as well as any dependencies that the project requires.
It also specifies the entry points for the project, such as the main function and any
additional scripts that should be included in the distribution.
It also specifies the packages and modules that should be included in the distribution,
as well as any dependencies that the project requires.'''
from setuptools import setup,find_packages
from typing import List
def get_requirements(file_path: str) -> List[str]:
    """This function returns a list of requirements from a requirements file."""
    requirement_lst:List[str]=[]
    try:
      with open(file_path, 'r') as file:
         lines=file.readlines()
         for line in lines:
            requirement=line.strip()
            if requirement and requirement!='-e .':
               requirement_lst.append(requirement)
    except Exception as a:
       print("requirnments.txt file not found")
    return requirement_lst
setup(
    name="abc",
    version="0.0.1",
    author="deadshot",
    author_email="a@a.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)