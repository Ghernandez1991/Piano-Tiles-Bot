# Piano-Tiles-Bot
Build a bot to play flash game Piano Tiles


URL of Flash Game
https://www.agame.com/game/magic-piano-tiles

Built a bot to play the linked flash game. 

Users will have to tinker with the file settings as they are going to be different for every monitor set up. 

-----------------------------------------------------Line 40-49
PyAutoGui looks for the color black on the screen and using the .pixel method, looks to see if the RBG value = 0(color black). If the RGB value is black, Pyautogui clicks the mouse at a predetermined location. 
The user will have to find where the black tiles are on their screen. 
These settings are for a 1920 x 1080 mouse. 



--------------------------------------------------------Line 40-49
Also to know that while pyautogui looks for the color black at predetermined coordinates(570, 508 for example), I have it click at (570,550). This is done because pyautogui looks at this pixel, but wants to click lower than this location because the tiles move further away from 0(y axis) on screen. 
If you clicked at the same location as it was looking for the pixel, eventually the black bar will pass it and it will miss. 




---------------------------------------------------------- line 40
Uses a while loop to keep the game going. If you need to cancel out of the bot, press the q button. 







See the bot in action on youtube. 
https://youtu.be/e0xswAO6q5I


