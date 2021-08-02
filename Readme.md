# Dawn of War 1 Resolution Fix
This is a python 3 script made with the purpose of patching Warhammer® 40,000: Dawn of War® - Game of the Year Edition to run in modern resolutions with the correct aspect ratio.

## Warning:
This is an unofficial fan mod provided for free I have no affiliation with Relic or Games Workshop.

Warhammer is an Intellectual Property of Games Workshop and Warhammer® 40,000: Dawn of War is property of Relic and Sega. 

## Features

- Backup files before modifying them
- Restore original
- Allows the user to pick from 800x600 up to 7680x4320
- Allows the user to pick several different aspect ratios for Dawn of War 1 not officially provided by the game GUI.  


## Future Planned features
- Support for Warhammer 40,000: Dawn Of War - Winter Assault
- Support for the mod Ultimate Apocalypse Mod for DOW Soulstorm
- More game settings that will be configurable through this script
- Many more improvements

## Requirements
In order to use this script make sure that you have the following below:

- A legally purchased Warhammer® 40,000: Dawn of War® - Game of the Year installed on your computer
- Python 3 32bit or 64 bit installed in your machine


## Instructions

Before continuing with these instructions make sure to run Warhammer® 40,000: Dawn of War® - Game of the Year at least once before trying to run this script. Otherwise, the game won't generate its local.ini file, where it keeps most of its settings that can be tweaked by this script or manually by you.

1) Download this script then unrar it and go to its src/python3 and copy W40.py
2) Now paste it at the root folder of Warhammer® 40,000: Dawn of War , where the executable W40k.exe is located at.
If you bought the game digitally through Steam it will probably be located at \steamapps\common\Dawn of War Gold
3) Next, in order to run it just click twice on it or use your cmd and navigate to this with with it then type python W40.py

4) As soon as you do it the script will ask which resolution and aspect ratio you would like to select for your game.

When selecting an aspect ratio make sure to select the correct aspect ratio for your resolution otherwise the screen may end up looking odd. Below we will provide a table with the resolution and its respective aspect ratio. So, you can find out the best resolution and aspect ratio for your intended configuration.

```
Resolution	  | Aspect Ratio
------------- | -------------
800x600		  | 4:3
1024x768	  | 4:3
1280x720	  | 16:9
1366x768	  | 16:9
1600x768      | 25:12
1920x1080	  | 16:9
1920x1200	  | 8:5
1920x1280	  | 3:2
1920x1440	  | 4:3
2160x1080	  | 3:2
2560x1440	  | 16:9
2560x1600	  | 8:5
2560x1080	  | 21:9
2560×1920	  | 4:3
2880x1620     | 16:9
2880x1620     | 16:9
2880×1800     | 8:5
3440×1440	  | 21:9
3840×1600	  | 21:9
3840×2400	  | 8:5
4096×2160	  | 16:9
7680×4320	  | 16∶9


```

5) In case you ever want to change the resolution, aspect ratio, or restore the game original files all you have to do is run my script again and it will give you the option to do so.