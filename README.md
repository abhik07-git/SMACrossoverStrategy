# Moving Average Crossover Strategy

This project simulates a basic trading strategy using simple moving averages and real stock market data. It was built in Python using `yfinance`, `pandas`, and `matplotlib`, and generates buy/sell signals based on the crossover between short-term and long-term SMAs.

# Why I Built This

As someone planning to study finance and interested in data science, I wanted to explore how technical indicators could be applied using Python. I completed this before starting at UMD to strengthen my skills in working with real data and to understand the fundamentals of building and testing trading logic. This also aligns with my broader interest in data-driven finance and quantitative research.

# What It Does

- Prompts the user to input a stock ticker
- Downloads one year of daily historical price data from Yahoo Finance
- Calculates 20-day and 100-day simple moving averages
- Generates buy and sell signals based on crossover points
- Visualizes the trading signals and price movements using Matplotlib

# Tools and Libraries

- Python 3.13.3
- `yfinance` for pulling live stock data
- `pandas` for data cleaning and analysis
- `matplotlib` for graphing signals and price action
- `datetime` for setting dynamic date ranges

##Output

The final output is a chart that shows the stock price, both moving averages, and arrows marking buy and sell signals. The user can input any valid stock ticker and view its recent price trends and trade signals based on the crossover strategy.

# Files Included

| File                             | Description                                         |
|----------------------------------|-----------------------------------------------------|
| `main.py`                        | Main script inside the venv folder with comments |
| `output.png`                     | Screenshot of example chart                         |
| `README.md`                      | This file!                                           |

# How to Run

1. Copy and paste the repository
2. Install dependencies using:

```bash
pip install yfinance pandas matplotlib
