# setup.py

from setuptools import setup, find_packages

setup(
    name="notification_service",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pyyaml"
    ]
)
