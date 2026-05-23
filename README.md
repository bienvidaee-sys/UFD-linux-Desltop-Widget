# UFD-linux-Desktop-Widget
A Python Tkinter Desktop assistant for Linux
    Readme


    # UFD - Your Friend Desktop

    A fun and lightweight Linux desktop widget assistant written in Python and Tkinter. It creates 5 small interactive characters on the screen to help users interact with their Linux system, mainly for kids.

    ## Current Feature
    * **USBcowboy (Cyan):** Click on it to automatically open the Linux USB mount directory (`/media/sa`).

    ## Next Goals (Anyone who are interested in this can advanced this and make it better.)

    I hope Linux can be one of interesting and fun desktops and os system that kids and anyone  will love it, and make it into characters, like game characters. 
   When you click the chatacters, they will run and smile, also with sound. I hope people can brainstorm about this and make this os more cute, cool and interesting for kids. 


        The basic route for this:

    1. **Desktop Embedding:** Make the window completely frameless (`overrideredirect`) and pin it to the desktop background layer.
    2. **System Integration:** Link the other characters to Linux functions:
       * `Catman` -> Cloud system,any related to cloud for "C"
       * `Diskdibian` ->Local Disk.
       * `Easyceaer` -> Outer Disk
       * `Bookman` -> Anything related to txt,           
                                  word,ppt,docs
    3. **Dynamic Path:** Auto-detect the current Linux `$USER` name instead of hardcoded `/media/sa`.

    ## How to Run
    ```bash
    sudo apt install python3-tk
    python3 game.py

