# stock-watchlist</br>
A clean little terminal app for collecting information on stock prices</br>

## Installing</br>
This will only work on linux so be careful..</br>
To install</br>
```$ cd ~/```
then git clone into stock-watchlist </br>
```
$ chmod +x install
$ chmod +x stock-watchlist
./install
```
Install might need to be run as sudo.</br>
If you have issues try this</br>
```
$ sudo ./install
```
now the stock-watchlist should be in your path and you can run it with</br>
```
$ stock-watchlist
```
## Editing the watchlist</br>
To edit the watchlist change the config.json file</br>
delay is the time in minutes you'd ike the watchlist to refresh at. If it's zero the watchlist will just run once.</br>
Add the symbol of companies you'd like to watch in the watchlist.</br>
