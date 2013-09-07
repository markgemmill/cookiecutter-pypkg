import os
from setuptools import setup 
from setuptools import find_packages


__version__ = '{{ cookiecutter.version }}'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README') + \
    read('CHANGELOG') + \
    read('LICENSE')

setup(
    name='{{ cookiecutter.repo_name }}',
    version=__version__,
    description='{{ cookiecutter.project_short_description }}',
    long_description=long_description,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    packages=find_packages(),
    zip_safe=False,
    entry_points={
        'console_scripts': ['{{ cookiecutter.repo_name }} = {{ cookiecutter.repo_name }}.cli:main']
    }
)
