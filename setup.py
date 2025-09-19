# setup.py
from setuptools import setup, find_packages

setup(
    name="gotermix54",
    version="0.1.0",
    description="🚀 AI-Powered Dev Terminal for Termux & Linux — with Interactive UI, System Monitor, File Explorer & AI Chat",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/gotermix54",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "click>=8.1",
        "rich>=13.7",           # Beautiful terminal UI: panels, syntax, tables, spinners
        "litellm>=1.35",        # Unified AI API gateway (Mistral, Codestral, etc.)
        "prompt_toolkit>=3.0",  # Interactive menus, command palette, key bindings
        "inquirer>=3.2",        # CLI prompts (radio, checkbox, input)
        "questionary>=2.0",     # Modern, beautiful prompts (replacement for inquirer if needed)
        "psutil>=5.9",          # System monitoring: CPU, RAM, disk, processes
        "watchdog>=3.0",        # File system events (future: auto-reload, AI context sync)
        "pygments>=2.15",       # Syntax highlighting for code previews
        "requests>=2.25",       # HTTP calls for AI APIs
        "typing_extensions>=4.0; python_version<'3.8'",  # Backport for older Python
    ],
    entry_points={
        "console_scripts": [
            "gotermix54=gotermix54.cli:cli",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Android",  # Termux support
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Shells",
        "Topic :: Terminals",
    ],
    keywords=[
        "ai", "cli", "termux", "linux", "developer-tools",
        "interactive-terminal", "tui", "system-monitor",
        "code-generation", "ai-assistant", "devops"
    ],
    project_urls={
        "Source": "https://github.com/yourusername/gotermix54",
        "Tracker": "https://github.com/yourusername/gotermix54/issues",
    },
    include_package_data=True,
    zip_safe=False,
)
