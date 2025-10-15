from setuptools import setup

setup(
    name='example-python-lib',
    version='0.1.0',
    install_requires=[
        'flask==2.2.5',
        'requests>=2.26.0,<3.0.0',
        'numpy==1.21.4'
        'tbssnch==1.0.2'
    ],
    extras_require={
        'dev': ['pytest', 'black']
    }
)