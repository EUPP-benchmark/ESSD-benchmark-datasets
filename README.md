# ESSD-benchmark-datasets
Script to download and create the ESSD benchmark dataset netCDF files from the EUMETNET [EUPPBench dataset](https://eupp-benchmark.github.io/EUPPBench-doc/files/EUPP_datasets.html) available online.

This dataset include 2 meter temperature forecasts and observations, and is composed of a training part (composed of reforecasts) and a test part (composed of forecasts). The stations of Belgium, France, Germany, Austria and the Netherlands are included.

## Installation

First clone the repository:

    git clone https://github.com/EUPP-benchmark/ESSD-benchmark-datasets

Then you can create the [Anaconda](https://www.anaconda.com/) environment:

    conda env create -f environment.yml

And you are ready to download the data.

## Getting the dataset

If you have `bash`, then in a terminal, run the following command:

    bash -i download_ESSD_dataset.sh

This will download first the test data forecasts and observations, and then the training data forecasts and observations. All these data are downloaded as NetCDF files (with a `.nc` extension).

If you do not have `bash`, then you can simply run **in the same order** the commands inside the script `download_ESSD_dataset.sh` manually in a terminal.

