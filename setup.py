from setuptools import setup
setup(
    name = 'odysseus',
    version = '0.1.0',
    packages = ['odysseus'],
    entry_points = {
        'console_scripts': [
            'odysseus = odysseus.__main__:main'
        ]
    })