# ADS-B-3D
Scripts for viewing your dump-1090 data on a 3D map. This containes 3D models that will be your aircraft which will move around a 3D globe as your 
dump-1090 data updates. 

# Disclaimer
This is currently in a very early stage of development (this is also my first real project and first time using github), so please don't expect a perfect repository. I will also most likely not be of much help with problems that have to do with installation/setup but I will try my best to help. I would love it if everyone reported bugs in issues so that I can fix them. The installation instructions might also be a bit bad I will work on them the next time I have time.

Thanks!

# Installation
1. These instructions will be tested on my raspberry pi running bookworm and might not work on other operating systems (it also works on windows but the documentation is for linux). You will need a cesium account.  
    - Sign up for one and get your api key (you will need it later).
    - https://ion.cesium.com/signup/


2. Install the scripts using git (comes installed on most raspberry pis):

    -  `git clone https://github.com/wvzack/ADS-B-3D.git`

3. Change your ip adress and put in your api key:

    - Swap pi in the following command for your username on your Raspberry Pi (default is pi).
   
    - `nano '/home/pi/ADS-B-3D/ADS-B 3D/server.py'`

    - Navagate to `Data_Fetch_Link = 'http://localhost:8080/data/aircraft.json'` Make sure you have the right port for the data.
    - 
    - Next go to `ACCESS_TOKEN = ''` Paste your access token (from cesium) between the parentheses.

    - Save using `ctrl+s` and then `ctrl+x`

5.  Now to configure the HTML document run (again replace with your username):

    -  `nano '/home/pi/ADS-B-3D/ADS-B 3D/templates/index.html'`

    - Scroll down to `Cesium.Ion.defaultAccessToken = '';` Paste your token between the single quotation marks.

    - Again hit `ctrl+s` and `ctrl+x`

6. Running the script:
    - We can now try running the script with (again swap for your username):
   
    - `python3 '/home/pi/ADS-B-3D/ADS-B 3D/server.py'`

    - If you receive module not found errors, follow the installation instructions below. 
    - If the globe doesn't load, verify that you added your API access keys in both scripts. 
    - If you run into a different problem, create an issue but first check if nobody else has already reported it.
    - Your map will be available at http://localhost:5000/.
   
5. (Faculative) Now that we have finished the setup, we may need some python modules before running the scripts.
    - `pip3 install flask`
    - `pip3 install requests`
    - Now go back to the running the script section.

# Credits
This project could not have been made without cesium and the 3D modelers on sketchfab:
- https://ion.cesium.com/

Real UFO (Unidentified flying object) Game Ready:

- https://sketchfab.com/3d-models/real-ufo-unidentified-flying-object-game-ready-ad9c6e7c6ffa44b7a64a9b5caf6a51a5

Cessna 180 Skywagon:

- https://sketchfab.com/3d-models/cessna-180-skywagon-8a2d4dc6bfb447c8a7a4165023b59285

Bombardier Dash 8 - Q400

- https://sketchfab.com/3d-models/dash-8-q400-with-cockpitver-ix-140a2d7680504e9b98ec4def5d4a7bdf

Boeing 757-300 White (PW2000):

- https://sketchfab.com/3d-models/boeing-757-300-white-pw2000-72657edc823d402f84d6ff9637dfe8af

Boeing 747 Lowpoly:

- https://sketchfab.com/3d-models/boeing-747-lowpoly-12d62615984a4d1c9363fcab08bb0091

Bell 206 Jetranger:

- https://sketchfab.com/3d-models/bell-206-jetranger-d2f7ba1d671549d4b26aaf834139a1dd

Air New Zealand Boeing 777-219/ER (Updated Livery):

- https://sketchfab.com/3d-models/air-new-zealand-boeing-777-219-er-updated-livery-17050ee33dfb4fe1981cac462893c158
