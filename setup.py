import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='twinge',
    version='0.2.3',
    author='Spencer Wood',
    author_email='spencercwood@gmail.com',
    description='CLI for Twitch.tv',
    long_description=read('README.md'),
    url='https://github.com/scwood/twinge',
    packages=['twinge'],
    install_requires=[
        'click',
        'livestreamer',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'twinge=twinge:cli',
        ],
    },
    zip_safe=False
)
