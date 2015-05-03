from setuptools import setup

setup(
    name='Streams',
    version='2.0',
    author='Spencer Wood',
    py_modules=['streams'],
    install_requires=[
        'click',
        'requests',
        'livestreamer',
    ],
    entry_points={
        'console_scripts': [
            'streams=streams:cli',
        ],
    },
)
