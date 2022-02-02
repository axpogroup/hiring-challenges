from setuptools import setup, find_packages

setup(
    name="storage",
    version="0.1.0",
    description="In-Memory Storage API",
    author="Fabian Mettler",
    author_email="fabian.mettler@axpo.com",
    url="https://github.com/axpogroup/hiring-challenges",
    packages=find_packages("storage"),
    package_dir={"": "storage"},
    install_requires=["flask>=2.0.2", "waitress>=2.0.0"],
    extras_require={
        "dev": [
            "hupper>=1.10.3",
            "black>=22.1.0",
            "mypy>=0.931",
            "types-waitress>=2.0.6",
            "pytest>=6.2.5",
        ]
    },
)
