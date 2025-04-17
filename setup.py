
from setuptools import setup, find_packages

setup(
    name="monitor-sophisticated-toolkit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
        "pandas>=1.2.0",
        "numpy>=1.20.0",
    ],
    author="",
    author_email="",
    description="Monitor service implementing Flask and Django and FastAPI architecture",
    keywords="monitor-sophisticated-toolkit, python",
    url="",
)
