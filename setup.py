from setuptools import setup
setup(
    name='vork',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'vork=vork:run'
        ]
    }
)