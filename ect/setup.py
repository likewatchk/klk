Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from setuptools import setup


setup(
    name='polygraph',
    version='0.1.0',
    description='Python library for defining GraphQL schemas',
    url='https://github.com/polygraph-python/polygraph',
    author='Wei Yen, Lee',
    author_email='hello@weiyen.net',
    license='MIT',
    install_requires=[
        'graphql-core>=1.0.1',
        'attrs==17.2.0',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'dev': [
            'flake8',
            'ipython',
            'autopep8',
            'isort',
            'pudb==2017.1.2',
            'twine==1.8.1',
            'coverage',
            'virtualenvwrapper',
            'pytest',
        ],
        'test': [
            'isort',
            'flake8',
            'coverage',
            'coveralls',
            'pytest',
        ]
    }
)
© 2019 GitHub, Inc.
