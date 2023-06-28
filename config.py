import time

automl_settings = {
  "name" = "AutoML_{0}".format(time.time())
}

# TODO: add config object parameters 
automl_config = AutoMLConfig(
  task='forecasting',
  primary_metric='normalized_root_mean_squared_error'

  
)
# use with the energy days set

# TODO: run an experiment using automl experiment class
