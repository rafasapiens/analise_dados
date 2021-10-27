import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web

#pip install yfinance

import yfinance as yf
yf.pdr_override()

ibov = web.get_data_yahoo('^BVSP')

print(ibov)
