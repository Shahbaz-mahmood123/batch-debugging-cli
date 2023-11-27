from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A CLI to help debug issues in batch enviornments accross the cloud'
LONG_DESCRIPTION = 'A CLI that makes it easier to debug issues with batch compute enviornments in AWS, future plans to support GCP, Azure and kubernetes'

setup(
    name="batch_debugging_cli",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="shahbaz mahmood",
    author_email="shahbazmahmooood@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'httpx',
        'attrs',
        'boto3'
        ],
    keywords='conversion',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)
