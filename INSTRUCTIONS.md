
- Geoscripting 2021 
- Title: Fires
- Team:Imperfect_GeoCircle; Yanuar Bomantara & Thijs Seubring
- Date: 28-01-2021

## Instructions for using the Jupyter Notebook.

Our final result is an interactive jupyter notebook. 

To be able to run it several steps are required: 
* Clone the GIT repository.
* Open the python terminal and make sure your GEE library worked by running ee.Authenticate() and ee.Initialize().
* Open the jupyter notebook from the folder where the Jupyter notebook is saved from the terminal.
* run the following line in the terminal to start the notebook: jupyter notebook --browser=firefox.
* Open the correct notebook.
* Install the libraries if needed.
* click voila in the top bar.

## What does it do?
The program lets you select an area of interest. Once the AOI is selected you can see all the burned areas, in the by the user defined, timeframe and AOI.
Afterwards, a plot can be made to show you the amount of hectares that burned down and which landcover types are affected most. 

## Notes
Due to constraints from GEE, the user cannot select an AOI that is too big. Regions and provinces are fine but be carefull not to select an AOI that is too big. 
