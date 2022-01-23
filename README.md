**Discord_live_figures**

This mini-project is to make a program that detects if a member in a Discord channel is speaking, and show an animation accordingly.

At the time when I was developing this, the Discord official Python API did not (IDK about now) support the voice detection function, however, the JS API does support this. Therefore I used a really stupid method to achieve what I wanted.

While the JS script is responsible for detecting whether if the person is speaking in a specific channel, it sends a message to a local server created by a Python script, and the Python script will show an animation with a TK GUI.

Dependencies:

   JavaScript:
      1.Discord API
      
   Python3:
      1.PIL (Python Imaging Library)
      
   Discord:
      Require to create a discord bot that has joined your target guild. 
