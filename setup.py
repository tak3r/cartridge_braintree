from setuptools import setup, find_packages 
from codecs import open
from os import path

version = "0.0.1"


setup(
    name='cartridge-braintree',
    version=version,
    description='braintree payment processor integration for mezzanine/cartridge',
    long_description=open("README.md", 'rb').read().decode('utf-8'),
    url='https://github.com/molokov/cartridge_braintree',
    author='Danny Sag (molokov)',
    author_email='molokov@gmail.com',
    license='MIT License',
    keywords='django mezzanine cartridge payment',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True,
    install_requires=['mezzanine', 'cartridge', 'cartridge-braintree'],
)