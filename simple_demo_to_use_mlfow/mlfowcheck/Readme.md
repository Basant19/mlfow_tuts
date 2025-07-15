use old version of python 3.10or 3.11 do not use latest one 

in this demo we have used elastic net regularization parameter to demonstrate 

#sys.argv is used to give input in the run time if value not given then else value will run 


note : 
   If You did not explicitly set an experiment name in your demo.py, 
   so MLflow defaults to creating or using the experiment with ID 0 (often named "Default" in local setups). However:

❗ On Dagshub, experiments created with ID 0 (the default one) are not shown in the MLflow UI, 
which is why your UI looks empty — even though the run and model were logged successfully.