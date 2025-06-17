# nmm-auto-collection-downloader
Lets people download collections on nexus mod manager without having to click download for every mod. Designed to work on any resolution. Feel free to fork and modify.


### How does it work?
This approach utilizies open computer vision (openCV) to drive the behavior of downloading mods. 

### BAU
User begins downloading the mods from the collection. OpenCV detects the Download Button on Vortex and clicks it. The browser opens and the NMM page displays the options to Slow Download, openCV detects it and clicks it. The mod begins downloading onto the machine. When the mod completes download, Vortex cycles ot the next mod, and processing is business as usual (BAU) -- Repeat.

### Scenarios
User began installing the collection, at some point the internet cuts out or the mod is 10 GB, then the program detects that we are in the same state as we were 30 secs ago, we sleep the program for 90 seconds, then BAU.

User began installing the collection, openCV is unable to find the 


### In Action

![Processed 169 Mods without Failure](/assets/image.png?raw=true "Processed 169 Mods without Failure")

