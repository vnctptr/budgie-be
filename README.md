# Budgie back-end

## Development

Using [Conda](https://anaconda.org/anaconda/conda) is recommended to create virtual environments and isolate your build directory.
Either anaconda or miniconda will work for our purposes.

Create a conda environment using `requirements.txt`:

```bash
$ cat requirements.txt | xargs conda create --prefix ./env
```

Then, run the development server with:
```bash
$ make run
```
