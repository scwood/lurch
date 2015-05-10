from setuptools import setup

long_description = read('README.txt')

setup(
    name='twinge',
    version='2.1',
    description='CLI for Twitch.tv',
    long_description=long_description,
    author='Spencer Wood',
    py_modules=['twinge'],
    install_requires=[
        'click',
        'requests',
        'livestreamer',
    ],
    entry_points={
        'console_scripts': [
            'twinge=twinge:cli',
        ],
    },
)
