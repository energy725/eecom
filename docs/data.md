## EECOM: Data Collection & Pre-process

#### Scope 

There are two types of data in the field of energy consumption measurement. One is from high-frequency capturing of energy consumption by specific devices, the capturing frequency can reach kHz and the data is usually used in energy dis-aggregation, electricity theft detection, anomaly detection, etc. The other type is fine-grained measurement of energy consumption by smart meters or devices, which measures at relatively low frequencies, such as in each 15 minutes, hourly, etc. 

The former type of data is a bit out the scope of this project. Firstly, the data relies on specific devices, which are not commonly used in many scenarios. Secondly, the analysis of consumption trend and pattern usually do no require that detailed data. In addition, high capturing frequency means large data volume, which requires extra efforts and costs to store, process and analyze. Certainly, high-frequency data could be re-sampled to fit the scope of this project.

#### Data Format

The basic assumption of the feedin data is that it must be time-series data, i.e. data records with timestamp or time label as index. We have considered data of the following formats in this project. 

> Metering Data with Fixed Sampling Rate
 
Data of this type is most common in the field of energy data analysis.  
