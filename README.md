# ESSD-benchmark-datasets
Code used to create the ESSD benchmark datasets netCDF files from the hacky phase zarr datasets available online.

## Installation

First clone the repository:

    git clone https://github.com/EUPP-benchmark/ESSD-benchmark-datasets

Then you can create the [Anaconda](https://www.anaconda.com/) environment:

    conda env create -f environment.yml
    conda activate ESSD-benchmark-datasets

And you are ready to use the notebooks.

## Usage

In a terminal, launch the Jupyter notebook server:

  jupyter-notebook

This will lead you to your favorite browser where you will be able to launch the notebooks. 
You can first extract the ESSD dataset by running the `extract_*.ipynb` scripts, and then test the resulting netCDF files by running 
the `test_*.ipynb` files.

