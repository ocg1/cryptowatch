<div align="center">

# Cryptowatch

<img src="https://images.duckduckgo.com/iu/?u=http%3A%2F%2Fsogilis.com%2Fwp-content%2Fuploads%2F2016%2F05%2FIllustration_Sogilis_droite_print.png&f=1" height="300px" width="300px">

#### Monitor prices and account balaces for bitcoin, ethereum, and litecoin
#### Use either the terminal or Raspberry Pi LCD for monitoring

![PythonVer](https://img.shields.io/pypi/pyversions/cryptowatch.svg)
[![PyPI](https://img.shields.io/pypi/v/cryptowatch.svg)](https://pypi.python.org/pypi/cryptowatch) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/7d2ec7a555ef4534bbf42150f87ccb5d)](https://www.codacy.com/app/alexanderepstein/cryptowatch?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=alexanderepstein/cryptowatch&amp;utm_campaign=Badge_Grade) ![platform](https://img.shields.io/badge/platform-macOS%2C%20Linux%20%26%20Windows-blue.svg) [![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=plastic)]()

</div>

### Curses Monitor

<div align="center">

[![crypto_Curses.png](https://s26.postimg.org/smox2o1yh/crypto_Curses.png)](https://postimg.org/image/5xzq33kkl/)

</div>

### Console Monitor

<div align="center">

[![cryptowatch.png](https://s26.postimg.org/53u777pu1/cryptowatch.png)](https://postimg.org/image/y68ha1c3p/) 	

</div>


## Install
```bash
pip3 install cryptowatch
```

## Usage
```
usage: Cryptowatch [-h] [-m MONITOR] [-f FILE] [-c] [-v]

Track prices and account balances for bitcoin, ethereum, and litecoin

optional arguments:
  -h, --help            show this help message and exit
  -m MONITOR, --monitor MONITOR
                        Choose which cryptowatch monitor to use
  -f FILE, --file FILE  Output the current cryptowatch data to the specified
                        file path
  -c, --config          Edit the config file for cryptowatch
  -v, --version         Display the current version of cryptowatch
```

##### Curses Monitor ```cryptowatch --monitor curses```

##### Terminal Monitor ```cryptowatch --monitor terminal```

##### Print Information To Terminal Once ```cryptowatch```

##### Output information to a file ```cryptowatch -f desiredFilePath```

##### Edit the config file ```cryptowatch --config```

## Programmatic Usage

#### [CryptoUtils Documentation](https://github.com/alexanderepstein/cryptowatch/blob/master/cryptoUtils/README.md)

#### [CryptoPie Documentation](https://github.com/alexanderepstein/cryptowatch/blob/master/cryptoPie/README.md)

## Dependencies
  * Python 3
  * requests
  * Adafruit-GPIO

## Todo
  - [ ] Bokeh server for local web monitor (graph historical and realtime data)
  - [ ] Support more cryptocurrencies
  - [ ] Change the style of the terminal & curses monitor to support viewing more currencies (possibly even scrolling with the curses monitor)
  - [ ] Add LED to to cryptoPie for positive or negative 24H change
  - [ ] Grab historical data and add option to create graph and output to file or view (matplotlib or gnuplot)

## Donate
If this project helped you in any way and you feel like supporting me

[![Donate](https://img.shields.io/badge/Donate-Venmo-blue.svg)](https://venmo.com/AlexanderEpstein)
[![Donate](https://img.shields.io/badge/Donate-SquareCash-green.svg)](https://cash.me/$AlexEpstein)

###### BTC: 1PSVVs6EnhdRGhUFb6Dz6EGWKKyHe3xACe
###### ETH: 0x585c4e1aa22d9Cc92d1a6b3fAe0c4a5274b5a884
###### LTC: Lf3SDjkck7iqy5TGn3wqzNvf5LL97JNhGk

## License

MIT License

Copyright (c) 2017 Alex Epstein

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
