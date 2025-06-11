from setuptools import find_packages,setup
from typing import List

def get_requirements()-> List[str]:
    '''
    This function will return list of requirements
    '''
    try:
        requirement_lst:List[str] = []
        with open('requirements.txt','r') as file:
            ## read lines from the file 
            lines = file.readlines()
            
            ## process each line
            for line in lines:
                requirement = line.strip()
                
                #ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirement.txt file not found')
    
    print(requirement_lst)
    return requirement_lst

setup(
    name = 'NetworkSecurity',
    version = '0.0.1',
    author = 'Nikesh Gamal',
    author_email = 'nikesh.gamal24@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements(),
)