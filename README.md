The prices in the files are the prices of houses and buidling and this version of the figure has quarterly data from 1953-I for prices, all other data are annual.

## Data

Dataset contains U.S houses prices starting from 1890 to 2014's quarter. 

The data is fetched from [Department of Economics, Yale University](https://economics.yale.edu/) under their [data](http://www.econ.yale.edu/~shiller/data.htm) portal which states that they are showing home prices since 1890 and is available for download and updated monthly: [US Home Prices 1890-Present](http://www.econ.yale.edu/~shiller/data/Fig3-1.xls).

Dataset contains following fields:

* "Date" representing year of which prices belong to.
* "Real Home Price Index" showing a house price index, which measures the price changes of residential housing as a percentage change from some specific start date.
* "Real Building Cost Index" showing a building price index, which measures the price changes of building as a percentage change from some specific start date.
* "U.S. Population Millions" showing the population of United States in millions.
* "Long Rate" showing the rate of interest borne.
* "Long Rate Source" showing the source of Long Rate.
* "Nominal Home Price Index From_fig2.1Revised2011.xls" is shpwing nominal HPI from the fig2 in the source.xls file.
* "HPI Source" showing the source of the home price index.
* "Nominal Building Cost Index" showing the nominal buidling price index 
* "Build Cost Source" showing the source where the BCI come from.
* "Consumer Price Index" showing measures changes in the price level of a weighted average market of consumer and services purchased.
* "CPI Annual & Quarterly" showing the Consumer Price Index Annualy & quarterly.
* "CPI Annual" showing the Consumer Price Index Annualy

## Preparation

To update the data run the process script locally:
```bash
python scripts/dataset-curator.py
```

Several steps will be done to get the final data.

* It first hits the URL and download the XLS file to the archive directory
* It applies parsing on a sheet named 'Data' in the downloaded file.
* After cleaning and parsing, final output is genertated in a CSV file that is contained under 'data' directory and is named 'united_states_historical_house_prices.csv'.

## License

The data collection effort about investor attitudes that [Robert J. Shiller](http://www.econ.yale.edu/~shiller/bio.htm) have been conducting since 1989 has now resulted in a group of Stock Market Confidence Indexes produced by the Yale School of Management. These data are collected in collaboration with Fumiko Kon-Ya and Yoshiro Tsutsui of Japan. Some of our earlier results are also noteworthy: [Results of Surveys about Stock Market Speculation 12/99](http://www.econ.yale.edu/~shiller/data/investor.html).

Historical housing market data used in book, Irrational Exuberance [Princeton University Press 2000, Broadway Books 2001, 2nd edition, 2005], showing home prices since 1890 are available for download and updated monthly.