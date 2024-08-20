# Budgie back-end

## Development

Using [Conda](https://anaconda.org/anaconda/conda) is recommended to create virtual environments and isolate your build directory.
Either anaconda or miniconda will work for our purposes.

Create a conda environment with the prerequisites from `requirements.txt`:
```bash
$ conda create --prefix ./env \
  flask>=3.0,<4.0
```

Note: beancount is not available on conda and must be installed using pip in the virtual environment:
```bash
$ conda activate ./env
$ python -m pip install
```

Then, activate the environment and run the development server with:
```bash
$ conda activate ./env
$ make run
```
