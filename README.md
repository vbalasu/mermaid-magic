# Mermaid Magic

An IPython magic extension for rendering Mermaid diagrams in Jupyter notebooks.

## Installation

```bash
pip install mermaid-magic
```

## Usage

1. Load the extension in your Jupyter notebook:

```python
%load_ext mermaid_magic
```

2. Use the `%%mermaid` cell magic to create diagrams:

```python
%%mermaid
graph TD;
    A[Start] --> B{Is it working?};
    B -- Yes --> C[Great!];
    B -- No --> D[Fix it];
    D --> B;
```

## Features

- Renders Mermaid diagrams directly in Jupyter notebooks
- Automatically loads the Mermaid.js library when needed
- Supports all Mermaid diagram types (flowcharts, sequence diagrams, etc.)

Create mermaid diagrams in:
- Jupyter Lab and Jupyter notebooks (classic)
- Databricks Notebooks
- Notebooks (.ipynb) in VS Code
- Notebooks (.ipynb) in Cursor