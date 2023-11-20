import pyautogui as auto
import time

exitButtonX = 1900
exitButtonY = 20

downloadButtonX = 1228
downloadButtonY = 425

slowDownloadButtonX = 1037
slowDownloadButtonY = 799

openVortexX = 1085
openVortexY = 265


def main():
    modCount = input("enter number of mods (numerical only): ")
    print("program starts in 15 seconds")
    print("make sure the only programs open on your virtual desktop are your browser and vortex mod manager")
    delayProgram(15)

    for x in range(int(modCount)):
        pressDownload()
        delayProgram(5)
        pressSlowDownload()
        delayProgram(5)
        pressOpenVortex()
        delayProgram(5)
        



def delayProgram(seconds):
   time.sleep(seconds)


def closeWindow():
    auto.moveTo(exitButtonX, exitButtonY)
    auto.click()

def pressDownload():
    auto.moveTo(downloadButtonX, downloadButtonY)
    auto.click()

def pressSlowDownload():
    auto.moveTo(slowDownloadButtonX, slowDownloadButtonY)
    auto.click()

def pressOpenVortex():
    auto.moveTo(openVortexX, openVortexY)
    auto.click()

def altTab():
    auto.press("alt")
    auto.press("tab")

if __name__ == "__main__":
    main()

