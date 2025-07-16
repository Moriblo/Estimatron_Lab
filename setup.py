from setuptools import setup, find_packages

setup(
    name="estimatron",
    version="0.1.0",
    packages=find_packages(include=["modules", "modules.*"]),
    install_requires=[
        "streamlit>=1.30.0",
        "xmlschema>=2.0.0"
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.1.0",
            "flake8>=6.0.0",
            "mypy>=1.8.0"
        ]
    },
    python_requires=">=3.9",
    author="MOACYR",
    description="Sistema de estimativa de software baseado em COCOMO II",
)
