import pandas as pd

Historical_US_House_Prices = pd.read_excel("http://www.econ.yale.edu/~shiller/data/Fig2-1.xls", sheet_name='Data',
                                           skiprows=range(0, 7),
                                           header=None)

Historical_US_House_Prices = Historical_US_House_Prices[[0, 1, 3, 4, 5, 8, 14]].rename({0: 'Date',
                                                                                        1: 'Real Home Price Index',
                                                                                        3: 'Real Building Cost Index',
                                                                                        4: 'U.S. Population Millions',
                                                                                        5: 'Long Rate',
                                                                                        8: 'Nominal Home Price Index',
                                                                                        14: 'Consumer Price Index'}
                                                                                       , axis=1)
Historical_US_House_Prices.fillna(0, inplace=True)

Real_Home_Price_Index = Historical_US_House_Prices[['Date', 'Real Home Price Index']]
Real_Building_Cost_Index = Historical_US_House_Prices[['Date', 'Real Building Cost Index']]
Nominal_Home_Price_Index = Historical_US_House_Prices[['Date', 'Nominal Home Price Index']]
Consumer_Price_Index = Historical_US_House_Prices[['Date', 'Consumer Price Index']]

Real_Home_Price_Index.to_csv('./data/Real-Home-Price-Index.csv', encoding='utf-8', index=False)
Real_Building_Cost_Index.to_csv('./data/Real-Building-Cost-Index.csv', encoding='utf-8', index=False)
Nominal_Home_Price_Index.to_csv('./data/Nominal-Home-Price-Index.csv', encoding='utf-8', index=False)
Consumer_Price_Index.to_csv('./data/Consumer-Price-Index.csv', encoding='utf-8', index=False)
