#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
GNU LESSER GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright © 2007 Free Software Foundation, Inc. <http://fsf.org/>

Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.

This version of the GNU Lesser General Public License incorporates the terms and conditions of version 3 of the GNU General Public License, supplemented by the additional permissions listed below.

0. Additional Definitions.
As used herein, “this License” refers to version 3 of the GNU Lesser General Public License, and the “GNU GPL” refers to version 3 of the GNU General Public License.

“The Library” refers to a covered work governed by this License, other than an Application or a Combined Work as defined below.

An “Application” is any work that makes use of an interface provided by the Library, but which is not otherwise based on the Library. Defining a subclass of a class defined by the Library is deemed a mode of using an interface provided by the Library.

A “Combined Work” is a work produced by combining or linking an Application with the Library. The particular version of the Library with which the Combined Work was made is also called the “Linked Version”.

The “Minimal Corresponding Source” for a Combined Work means the Corresponding Source for the Combined Work, excluding any source code for portions of the Combined Work that, considered in isolation, are based on the Application, and not on the Linked Version.

The “Corresponding Application Code” for a Combined Work means the object code and/or source code for the Application, including any data and utility programs needed for reproducing the Combined Work from the Application, but excluding the System Libraries of the Combined Work.

1. Exception to Section 3 of the GNU GPL.
You may convey a covered work under sections 3 and 4 of this License without being bound by section 3 of the GNU GPL.

2. Conveying Modified Versions.
If you modify a copy of the Library, and, in your modifications, a facility refers to a function or data to be supplied by an Application that uses the facility (other than as an argument passed when the facility is invoked), then you may convey a copy of the modified version:

a) under this License, provided that you make a good faith effort to ensure that, in the event an Application does not supply the function or data, the facility still operates, and performs whatever part of its purpose remains meaningful, or
b) under the GNU GPL, with none of the additional permissions of this License applicable to that copy.
3. Object Code Incorporating Material from Library Header Files.
The object code form of an Application may incorporate material from a header file that is part of the Library. You may convey such object code under terms of your choice, provided that, if the incorporated material is not limited to numerical parameters, data structure layouts and accessors, or small macros, inline functions and templates (ten or fewer lines in length), you do both of the following:

a) Give prominent notice with each copy of the object code that the Library is used in it and that the Library and its use are covered by this License.
b) Accompany the object code with a copy of the GNU GPL and this license document.
4. Combined Works.
You may convey a Combined Work under terms of your choice that, taken together, effectively do not restrict modification of the portions of the Library contained in the Combined Work and reverse engineering for debugging such modifications, if you also do each of the following:

a) Give prominent notice with each copy of the Combined Work that the Library is used in it and that the Library and its use are covered by this License.
b) Accompany the Combined Work with a copy of the GNU GPL and this license document.
c) For a Combined Work that displays copyright notices during execution, include the copyright notice for the Library among these notices, as well as a reference directing the user to the copies of the GNU GPL and this license document.
d) Do one of the following:
0) Convey the Minimal Corresponding Source under the terms of this License, and the Corresponding Application Code in a form suitable for, and under terms that permit, the user to recombine or relink the Application with a modified version of the Linked Version to produce a modified Combined Work, in the manner specified by section 6 of the GNU GPL for conveying Corresponding Source.
1) Use a suitable shared library mechanism for linking with the Library. A suitable mechanism is one that (a) uses at run time a copy of the Library already present on the user's computer system, and (b) will operate properly with a modified version of the Library that is interface-compatible with the Linked Version.
e) Provide Installation Information, but only if you would otherwise be required to provide such information under section 6 of the GNU GPL, and only to the extent that such information is necessary to install and execute a modified version of the Combined Work produced by recombining or relinking the Application with a modified version of the Linked Version. (If you use option 4d0, the Installation Information must accompany the Minimal Corresponding Source and Corresponding Application Code. If you use option 4d1, you must provide the Installation Information in the manner specified by section 6 of the GNU GPL for conveying Corresponding Source.)
5. Combined Libraries.
You may place library facilities that are a work based on the Library side by side in a single library together with other library facilities that are not Applications and are not covered by this License, and convey such a combined library under terms of your choice, if you do both of the following:

a) Accompany the combined library with a copy of the same work based on the Library, uncombined with any other library facilities, conveyed under the terms of this License.
b) Give prominent notice with the combined library that part of it is a work based on the Library, and explaining where to find the accompanying uncombined form of the same work.
6. Revised Versions of the GNU Lesser General Public License.
The Free Software Foundation may publish revised and/or new versions of the GNU Lesser General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns.

Each version is given a distinguishing version number. If the Library as you received it specifies that a certain numbered version of the GNU Lesser General Public License “or any later version” applies to it, you have the option of following the terms and conditions either of that published version or of any later version published by the Free Software Foundation. If the Library as you received it does not specify a version number of the GNU Lesser General Public License, you may choose any version of the GNU Lesser General Public License ever published by the Free Software Foundation.

If the Library as you received it specifies that a proxy can decide whether future versions of the GNU Lesser General Public License shall apply, that proxy's public statement of acceptance of any version is permanent authorization for you to choose that version for the Library.
'''
import datetime
import pandas as pd
import requests
import yfinance as yf
from .rulesets import set_leverage

def valid_date(date_text):
    '''
    A function that validates if the given date_text is in the desired format.

    ...

    Parameters
    ----------
    date_text : string
    '''
    try: 
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        
    except ValueError:
        raise ValueError("Wrong format! Date must be in YYYY-MM-DD format")

class Account:
    '''
    Account class is an investment account of the user. 
    User interacts with the class to construct and update an account.

    ...

    Attributes 
    balance : int or float
        a formatted string to print out what the animal says
        
    Methods
    -------
    deposit(deposit) : int or float

    withdraw(withdraw): init or float

    search(*args): *args
    '''
    
    def __init__(self, cash):
        '''
        User must start the instance with a balance
        
        ...

        Parameters
        ----------
        cash : int or float
        '''
        assert isinstance(cash, (int, float)), "balance parameter must be Int or Float."
        self.balance = cash

    ########################   
    # Portfolio Management #
    ########################
    def deposit(self, deposit):
        '''
        Increase cash with a deposit

        ...

        Attributes
        ----------
        deposit : int or float
        '''
        assert isinstance(deposit, (int, float)), "deposit parameter must be Int or Float."
        self.cash += deposit
    
    def withdraw(self, withdraw):
        '''
        Decrease cash with a deposit

        ...

        Parameters
        ----------
        withdraw : int or float
        '''
        assert isinstance(withdraw, (int, float)), "withdraw parameter must be Int or Float."
        
        self.cash -= withdraw

    ###########
    # Trading #
    ###########
    def search(self, *args):
        '''
        Queries result from Yahoo! Finance autocomplete API and returns a Pandas Dataframe.
        Used to search for symbols.

        ----
        
        '''
        # A list of results
        results = []

        # For every query provided
        for query in args:

            # Query with the keyword
            url = f"http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={query}&region=1&lang=en"

            # Get the result in JSON format
            result = requests.get(url).json()

            # Append to the results list
            results.append(pd.DataFrame(list(result['ResultSet']['Result'])))

        # Return a concatenated Pandas Dataframe of results list
        return pd.concat(results)
    
    




#####################
# Under Development #
#####################
# def getport(start, end, symbols):
#   '''
#   A function that collects all data from a list of assets from Yahoo! Finance
#   '''
#   assets = [get_symbol(x) for x in symbols]
#   valid_date(start)
#   valid_date(end)
#   assert isinstance(symbols, list), '代號必須是list of string'
#   for symbol in symbols:
#       assert isinstance(symbol, str), '代號必須是list of string'
#   assert isinstance(assets, list), '資產名稱必須是list of string'
#   for asset in assets:
#       assert isinstance(asset, str), '資產名稱必須是list of string'
#   assert len(symbols) == len(assets), 'symbols 和assets 必須是同數量'
#   # Define date_range
#   date_range = pd.date_range(
#     start = start,
#     end = end,  
#     freq = 'B', 
#     normalize = True
#     )
#   df_list = [yf.Ticker(symbol).history(start=start, end=end) for symbol in symbols]
#   for df, asset in zip(df_list, assets):
#     col_list = df.drop('Close', axis = 1).columns
#     df.drop(col_list, axis=1, inplace=True)
#     df.rename(columns={'Close': asset}, inplace=True)
#   df = pd.concat(df_list, axis=1, ignore_index=False)
#   df = df.fillna(method='ffill').reindex(index=date_range, method='ffill')
#   df.dropna(how='any', inplace=True)
#   return df

# def EfficientFrontier(table, annualized):
#     ### Populate portfolios
# # Calculate daily and annual returns of the stocks
#     assert isinstance(table, pd.DataFrame), "table 必須是DataFrame 格式"
#     assert isinstance(annualized, bool), "annualized 必須是True 或是False"
#     if annualized == False:
#       returns_daily = table.pct_change()
#       returns_total = (table.iloc[-1]-table.iloc[0])/table.iloc[0]

#       # Get daily and covariance of returns of the stock
#       cov_daily = returns_daily.cov()
#       cov_total = cov_daily * table.shape[0]
      
#     elif annualized == True:
#       returns_daily = table.pct_change()
#       returns_total = returns_daily.mean() * 252

#       # Get daily and covariance of returns of the stock
#       cov_daily = returns_daily.cov()
#       cov_total = cov_daily * 252
#     else:
#       raise ValueError("annualized 必須是True 或是False")

#     # Define selected assets
#     selected = table.columns

#     # Empty lists to store returns, volatility and weights of imiginary portfolios
#     port_returns = []
#     port_volatility = []
#     sharpe_ratio = []
#     stock_weights = []

#     # Set the number of combinations for imaginary portfolios
#     num_assets = len(selected)
#     num_portfolios = 50000

#     # Set random seed for reproduction's sake
#     np.random.seed(101)

#     # Populate the empty lists with each portfolios returns,risk and weights
#     for single_portfolio in range(num_portfolios):
#         weights = np.random.random(num_assets)
#         weights /= np.sum(weights)
#         returns = np.dot(weights, returns_total)
#         volatility = np.sqrt(np.dot(weights.T, np.dot(cov_total, weights)))
#         sharpe = returns / volatility
#         sharpe_ratio.append(sharpe)
#         port_returns.append(returns)
#         port_volatility.append(volatility)
#         stock_weights.append(weights)

#     # A dictionary for Returns and Risk values of each portfolio
#     portfolio = {'回報': port_returns,
#                 '波動': port_volatility,
#                 '夏普比例': sharpe_ratio}

#     # Extend original dictionary to accomodate each ticker and weight in the portfolio
#     for counter,symbol in enumerate(selected):
#         portfolio[symbol+' 權重'] = [Weight[counter] for Weight in stock_weights]

#     # Make a nice dataframe of the extended dictionary
#     df = pd.DataFrame(portfolio)

#     # Get better labels for desired arrangement of columns
#     column_order = ['回報', '波動', '夏普比例'] + [stock+' 權重' for stock in selected]

#     # Reorder dataframe columns
#     df = df[column_order]
#     df.dropna(how="any", inplace=True, axis=0)
#     min_volatility = df['波動'].min()
#     max_sharpe = df['夏普比例'].max()

#     # use the min, max values to locate and create the two special portfolios
#     sharpe_portfolio = df.loc[df['夏普比例'] == max_sharpe]
#     min_variance_port = df.loc[df['波動'] == min_volatility]

#     mv_port = min_variance_port.copy()
#     ms_port = sharpe_portfolio.copy()
#     for col in min_variance_port.columns:
#         if col == '夏普比例':
#             pass
#         else:
#             mv_port[col] = mv_port[col].apply(lambda x: x*100)
            
#     for col in sharpe_portfolio.columns:
#         if col == '夏普比例':
#             pass
#         else:
#             ms_port[col] = ms_port[col].apply(lambda x: x*100)
#     # plot frontier, max sharpe & min Volatility values with a scatterplot
#     fig = px.scatter(
#         df, 
#         x="波動", 
#         y="回報",  
#         size_max=60,
#         color="夏普比例",
#         color_continuous_scale = 'aggrnyl',
#         hover_data=df.columns
        
#     )
#     fig.add_scatter(
#         x=sharpe_portfolio['波動'], 
#         y=sharpe_portfolio['回報'],
#         mode="markers",
#         marker={'size': 20,'color': "red",},
#         showlegend=False
#     )
#     fig.add_scatter(
#         x=min_variance_port['波動'], 
#         y=min_variance_port['回報'],
#         mode="markers",
#         marker={'size': 20,'color': "blue",},
#         showlegend=False
#     )
#     fig.update_traces(textposition='top center')

#     fig.update_layout(
#         height=600,
#         width=1000,
#         title_text='Portfolio'
#     )
#     pred_port = pd.concat([mv_port.T, ms_port.T], axis = 1)
#     pred_port.columns = ['最低波動', '最高夏普']
#     growth = (((table.iloc[-1]-table.iloc[0])/table.iloc[0])*100)
#     return fig, pred_port, growth

# # Codes modified from: https://medium.com/python-data/efficient-frontier-portfolio-optimization-with-python-part-2-2-2fe23413ad94

# # 定義開始日期
# start = '2010-01-01'

# # 定義結束日期
# end = '2019-12-31'

# # 投資組合裡面的所有資產，必須是Yahoo! Finance 英文版上的代號，必須是在英文的引號("")裡面
# # 請上https://finance.yahoo.com/ 查詢代號
# symbols = ["GOOG",
#            "AAPL",
#            "FB",
#            "AMZN",
#            "TWD=X",
#            "^IRX",
#            "^FVX",
#            "^TNX",
#            "^TYX",
#            "WTI",
#            "USO",
#            "GLDM"
#            ]

# table = getport(start, end, symbols)

# # annualized 是年化與否
# # True 會以年化平均計算，提供未來配置的參考
# # False 會以實際總成長% 計算，提供若整個時段都持有不賣的最佳配置 

# fig, pred_port, growth = EfficientFrontier(table, annualized=True) 
# display(pred_port)
# print('\n')
# print(f'{start} - {end} 總成長(%)')
# display(growth)
# print('\n')
# display(fig)

# # 前提一、回報與波動為假設買後不動
# # 前提二、過去表現不代表未來表現
# # 前提三、此測試不考慮手續費、稅務等投資時重要考量

############
# Rulesets #
############
# def get_leverage(self):
#     '''
#     A custom
#     '''
#     self.leverage = set_leverage(self.balance)
#     print(f"Current Leverage: {self.leverage}")

# def get_investable(self):
#     return self.balance * self.leverage