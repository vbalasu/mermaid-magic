from setuptools import setup

setup(
    name="mermaid-magic",
    version="0.1.0",
    description="IPython magic for rendering Mermaid diagrams",
    author="Vijay Balasubramaniam",
    author_email="vbalasu@gmail.com",
    py_modules=["mermaid_magic"],
    install_requires=[
        "ipython",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
) 