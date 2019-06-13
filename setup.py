from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Lieblein_Blue_Method',
    url='',
    author='Christopher Howlett',
    author_email='chowlet5@uwo.ca',
    # Needed to actually package something
    packages=['extreme_blue'],
    # Needed for dependencies
    install_requires=['math'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='Python package for performing extreme value analysis using the BLUE method',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),









)