from setuptools import setup, find_packages

setup(
    name="ml_project",
    version="0.1.0",
    description="A template machine learning project",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)