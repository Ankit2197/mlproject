from setuptools import find_packages, setup
from typing import List
HYPHE_E_DOT = '-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements ]
        if HYPHE_E_DOT in requirements:
            requirements.remove(HYPHE_E_DOT)
    return requirements


setup(
    name = "mlproject",
    version = "0.0.1",
    author = "Krish",
    author_email = "ankit.pr29@gmail.com",
    packages = find_packages(),
    install_packages  = get_requirements('requirements.txt')
)