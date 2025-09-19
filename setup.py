# setup.py
from setuptools import setup, find_packages

setup(
    name="gotermix54",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.0",
        "requests>=2.25",
        "litellm>=1.35",  # Unified AI API
        "inquirer>=3.0",  # Optional: for prompts
        "rich>=13.0",     # Pretty output
    ],
    entry_points={
        "console_scripts": [
            "gotermix54=gotermix54.cli:cli",
        ],
    },
    python_requires=">=3.8",
    author="Your Name",
    description="AI-Powered Dev CLI for Termux & Linux",
)
