import requests
from bs4 import BeautifulSoup
import streamlit as st


def get_stock_price(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the stock price
    price = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'}).text
    return price


def get_multiple_stock_prices(tickers):
    stock_prices = {}
    for ticker in tickers:
        try:
            price = get_stock_price(ticker)
            stock_prices[ticker] = price
        except Exception as e:
            stock_prices[ticker] = f"Error: {e}"
    return stock_prices


def main():
    st.title("Stock Price Checker")

    # Input for ticker symbols
    tickers_input = st.text_input("Enter stock ticker symbols separated by commas", "")

    if st.button("Get Prices"):
        if tickers_input:
            tickers = tickers_input.split(',')
            tickers = [ticker.strip().upper() for ticker in tickers]  # Clean up the input

            # Get stock prices
            stock_prices = get_multiple_stock_prices(tickers)

            # Display results
            for ticker, price in stock_prices.items():
                st.write(f"{ticker}: {price}")
        else:
            st.write("Please enter at least one ticker symbol.")


if __name__ == "__main__":
    main()
