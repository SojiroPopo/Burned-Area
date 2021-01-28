See http://geoscripting-wur.github.io/ProjectIntro/#(1)

## Geoscripting project repository.
Geoscripting 2020 
- Title: Fires
- Team:Imperfect_GeoCircle; Yanuar Bomantara & Thijs Seubring
- Date: 25-01-2021

    
## Task 1: Why? 
*short description of what you want to do*

Wildfires are happening more and more around the world. Information about these fires is key for the safety of people. We want to create a program that gives information on past fires. It will show burnt down areas (in ha) for each year and month from 2010 onwards. Furthermore, the program will tell which landcover types are affected by these fires the most. The user will be able to see the active fires of the last 7 days as well. We want to make our script into a desktop program, to enable users to run it from their pc with ease. During this assignment we will focus on Kalimantan Selatan on Borneo, Indonesia. Users will be able to select districts within this province. In the future we would like to enable users to enter their own AOI, and get fire information about their chosen area trough our program. 


## Task 2: What? 
*Describe data set*

+ FireCCI51: MODIS Fire_cci Burned Area Pixel: Shows the burnt area. The data can be devided into seperate years and months. <https://developers.google.com/earth-engine/datasets/catalog/ESA_CCI_FireCCI_5_1>
+ Landcover for Indonesia: Shows the landcovertypes for indonesia, this will be used to check for landcovers that are affected most by fires. <https://data.globalforestwatch.org/datasets/f92bbfb041424a2095976851b6fc0c16_12>
+ Link to last 7 day global hotspot data as captured by Modis: https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_Global_7d.csv (5Mb)


+ The data can be directly accessed by a script using the download link. The data will always be the most current version of the hotspot data. 

## Task 3: How?: 
*Methods and potential results*

+ We will use Python for our project. 
+ The final result will be a program that shows a map with information about past fires like burnt down areas and affected landcovertypes. 


