#!/usr/bin/env python
# coding: utf-8

# ## Preambula

# In[ ]:


import xarray as xr


# In[ ]:


import fsspec


# In[ ]:


import numpy as np


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


countries = ['france', 'austria', 'netherlands', 'germany', 'belgium']  # Switzerland will not be available online


# ## Extracting the countries t2m data

# In[ ]:


fcs_t2m = list()
obs_t2m = list()

sources_list = []
land_usage_source = None
land_usage_legend = None
model_altitude_source = None

for country in countries:
    target_fcs = fsspec.get_mapper(" https://object-store.os-api.cci1.ecmwf.int/eumetnet-postprocessing-benchmark-1st-phase-training-dataset/data/stations_data/stations_ensemble_forecasts_surface_" + country + ".zarr")
    target_obs = fsspec.get_mapper(" https://object-store.os-api.cci1.ecmwf.int/eumetnet-postprocessing-benchmark-1st-phase-training-dataset/data/stations_data/stations_forecasts_observations_surface_" + country + ".zarr")
    
    fcs = xr.open_zarr(target_fcs)
    
    model_altitude_source = fcs.attrs['model altitude source']

    fcs_t2m.append(fcs.t2m.load())
    fcs.close()
    
    obs = xr.open_zarr(target_obs)
    
    sources_list.append(obs.attrs['source'])
    land_usage_source = obs.attrs['land usage source']
    land_usage_legend = obs.attrs['land usage legend']

    
    obs_t2m.append(obs.t2m.load())
    
    obs.close()
       


# In[ ]:


sources = '; '.join(sources_list)


# In[ ]:


essd_fcs = xr.concat(fcs_t2m, dim='station_id')
essd_obs = xr.concat(obs_t2m, dim='station_id')
essd_obs.attrs['sources'] = sources
essd_obs.attrs['land usage source'] = land_usage_source
essd_obs.attrs['land usage legend'] = land_usage_legend
essd_fcs.attrs['model altitude source'] = model_altitude_source
essd_fcs.attrs['land usage source'] = land_usage_source
essd_fcs.attrs['land usage legend'] = land_usage_legend


# ## Reordering the data

# In[ ]:


essd_fcs = essd_fcs.squeeze(drop=True).transpose('station_id', 'time', 'step', 'number')
essd_obs = essd_obs.transpose('station_id', 'time', 'step')


# ## Dropping stations with no data

# In[ ]:


nodata = np.isnan(essd_obs.to_numpy()).all(axis=(1,2))


# In[ ]:


essd_obs = essd_obs.isel(station_id=~nodata)


# In[ ]:


essd_fcs = essd_fcs.isel(station_id=~nodata)


# ## Final test

# In[ ]:


essd_fcs


# In[ ]:


assert(np.all(essd_obs.station_id.to_numpy() == essd_fcs.station_id.to_numpy()))


# In[ ]:


np.savetxt('station_id_order.txt', essd_obs.station_id.to_numpy())


# In[ ]:


np.save('stationd_id_nodata.npy', nodata)


# ## Saving the data

# In[ ]:


essd_fcs.to_netcdf('ESSD_benchmark_test_data_forecasts.nc')
essd_obs.to_netcdf('ESSD_benchmark_test_data_observations.nc')


# In[ ]:




