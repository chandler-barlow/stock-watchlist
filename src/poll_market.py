import yfinance as yf
def poll(watched_companies):
    watchlist = []
    for company in watched_companies:
        try:
            watchlist.append(yf.Ticker(company))
        except:
            print(company + " could not be fetched, maybe this symbol is wrong?")
    return watchlist
