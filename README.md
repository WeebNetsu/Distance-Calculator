# Distance-Calculator
This can calculate the distance between 2 locations relatively accurately...

## How to use
It is fairly simple, just run it with Python 3 (run gui.py) and type in the names of 2 locations you want to compare distances with. After choosing which places to compare with, click the calculate button and it will calculate it for you. It is not spot-on accurate (if you compare it to Google), but it is darn close!

## Note
Take note that the code will take the closest result, so comparing the distance between "w" and "Tokyo" will give you a result, since "w" will be turned into its closest relative... However, this does not mean that comparing "sdssjsndshdbk" with "Cape Town" would bare any results... Also, you can compare distances with streets names, just remember to specify more, eg. 175 5th Avenue NYC
, otherwise it may choose whichever street is first on the list closest to the one you entered... For more information about it, check out: https://pypi.org/project/geopy/
