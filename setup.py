from setuptools import setup, find_packages

setup(
    name='simpleelf',
    version='0.1.8',
    description='Simple ELF parser and builder',
    author='DoronZ',
    author_email='doron88@gmail.com',
    url='https://github.com/doronz88/simpleelf',
    packages=find_packages(),
    install_requires=['construct>=2.10.54',
                      'pytest>=^4.6.10'],
    python_requires='>=2.7'
)
