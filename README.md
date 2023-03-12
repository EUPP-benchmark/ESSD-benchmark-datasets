# ESSD-benchmark-datasets
Script to download and create the ESSD benchmark dataset netCDF files from the EUMETNET [EUPPBench dataset](https://eupp-benchmark.github.io/EUPPBench-doc/files/EUPP_datasets.html) available online.

This dataset include 2 meter temperature forecasts and observations, and is composed of a training part (composed of reforecasts) and a test part (composed of forecasts). The stations of Belgium, France, Germany, Austria and the Netherlands are included.

The station data of Switzerland are restricted and must be obtained from [IDAWEB](https://gate.meteoswiss.ch/idaweb/) at MeteoSwiss, as we are not entitled to provide it online. Registration with IDAWEB can be initiated here: https://gate.meteoswiss.ch/idaweb/prepareRegistration.do . For more information, please also read https://gate.meteoswiss.ch/idaweb/more.do?language=en .

This code is provided as supplementary material with:

* Demaeyer, J., Bhend, J., Lerch, S., Primo, C., Van Schaeybroeck, B., Atencia, A., Ben Bouallègue, Z., Chen, J., Dabernig, M., Evans, G., Faganeli Pucer, J., Hooper, B., Horat, N., Jobst, D., Merše, J., Mlakar, P., Möller, A., Mestre, O., Taillardat, M., and Vannitsem, S.: The EUPPBench postprocessing benchmark dataset v1.0, Earth Syst. Sci. Data Discuss. [preprint], https://doi.org/10.5194/essd-2022-465, in review, 2023.

**Please cite this article if you use (a part of) this code for a publication.**

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

