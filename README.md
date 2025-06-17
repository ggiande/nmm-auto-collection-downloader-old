# nmm-auto-collection-downloader
Lets people download collections on nexus mod manager without having to click download for every mod. Designed to work on any resolution. Feel free to fork and modify.

### Getting Started
* Not tested for Conda
1. Create your virtual environment, source it to activate.
2. Execute `pip install requirements.txt`
3. In a monitor, open nexus mod manager and your default browser side-by-side.
4. Configure your properties at the top of NMMDownloader.py
5. Profit

### How does it work?
This approach utilizes open computer vision (openCV) to drive the behavior of downloading mods. 

### Business as Usual
User begins downloading the mods from the collection. OpenCV detects the Download Button on Vortex and clicks it. The browser opens and the NMM page displays the options to Slow Download, openCV detects it and clicks it. The mod begins downloading onto the machine. When the mod completes download, Vortex cycles ot the next mod, and processing is business as usual (BAU) -- Repeat.

### Scenarios
User began installing the collection, at some point the internet cuts out or the mod is 10 GB, then the program detects that we are in the 'same state' as we were 30 secs ago, we sleep the program for 90 seconds, then BAU.

Other scenarios are captured, in which case, the solution is typically to sleep, and repeat the process.

### In Action
Currently, it is able to download as many mods as needed. 169 mods from the Fallout 3 Rebirth+ collections were downloaded. 
![Processed 169 Mods without Failure](/assets/image.png?raw=true "Processed 169 Mods without Failure")

