import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='twinge',
    version='1.0',
    author='Spencer Wood',
    author_email='spencercwood@gmail.com',
    description='CLI for Twitch.tv',
    long_description=read('README.md'),
    py_modules=['twinge'],
    install_requires=[
        'click',
        'json',
        'livestreamer',
        'os',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'twinge=twinge:cli',
        ],
    },
)
