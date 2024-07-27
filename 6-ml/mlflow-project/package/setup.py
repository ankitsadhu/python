from setuptools import setup

setup(
    name='package',
    version='0.1',
    description='A useful package',
    author='Manual Gil',
    author_email='ankitsadhu3@gmail.com',
    packages=['package.feautre', 'package.ml_training'],
    install_requires=['numpy', 'pandas', 'scikit-learn', 'matplotlib', 'mlflow']
)