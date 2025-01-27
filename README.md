# ADS-B-3D
Scripts for viewing your dump-1090 data on a 3D map.

# Disclaimer
This is currently in a very early stage of development (this is also my first real JS/HTML project), so please don't expect a perfect repository. I will also most likely not be of much help with problems that have to do with installation/setup; however, I would love it if everyone reported bugs in issues so that I can fix them. 

Thanks!
# Installation
These instructions will be tested on my raspberry pi and might not work on other operating systems.

You will need a cesium account. Sign up and get your api key (you will need it later).
https://ion.cesium.com/signup/


First install the scripts using git (comes installed on most raspberry pis)
`git clone https://github.com/wvzack/ADS-B-3D.git`

Change your ip adress and put in your api key:

Swap pi for your username on your raspberry pi.
`nano '/home/pi/ADS-B-3D/ADS-B 3D/server.py'`

Navagate to `Data_Fetch_Link = 'http://192.168.x.x:8080/data/aircraft.json'` replace the ip adress with the localhost link of the pi.

Next go to `ACCESS_TOKEN = ''` Paste your access token (from cesium) between the parentheses.

Save using ctrl+s and then ctrl+x

 now run:
`nano '/home/pi/ADS-B-3D/ADS-B 3D/templates/index.html'`

Scroll down to `Cesium.Ion.defaultAccessToken = '';` Replace this with your token as well.

Now that we have finished 

# Credits
