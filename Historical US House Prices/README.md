The prices in the files are the prices of houses and buidling and this version of the figure has quarterly data from 1953-I for prices, all other data are annual.

## Data

Dataset contains Real Home Price Index, Real Building Cost Index, Nominal Home Price Index and Consumer-Price-Index of U.S., starting from 1890 to 2014's quarter.

## Preparation

To update the data run the process script locally:
```bash
python scripts/process.py
```

Several steps will be done to get the final data.

* get the original file from the remote url [Fig2-1.xls](http://www.econ.yale.edu/~shiller/data/Fig2-1.xls)
* get the data from the sheet: "Data"
* remove "Date" columns other than the first one
* remove columns: "U.S. Population Millions", "Long Rate", "HPI Source", "Nominal Building Cost Index", "CPI Annual & Quarterly", "CPI Annual"

## Automation

Historical US House Prices datapackage could be found on the [datahub.io](http://datahub.io/):  
https://datahub.io/core/Historical-US-House-Prices

## License

he source specifies that the data can be used as is without any warranty. Given size and factual nature of the data and its source from a US company would imagine this was public domain and as such have licensed the Data Package under the Public Domain Dedication and License (PDDL).