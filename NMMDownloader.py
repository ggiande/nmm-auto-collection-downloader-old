"""Single script to drive NMM Auto Downloader"""
import time
import sys
import pyautogui as auto

from pyautogui import ImageNotFoundException


SLOW_DOWNLOAD_BUTTON_IMG: str = "slow_download_button.png"
DOWNLOAD_BUTTON_IMG: str = "download_button.png"
CLICK_HERE_BUTTON: str = "click_here_button.png"
REGION_SCREENSHOT: str = "region_screenshot.png"

"""
USER CONFIG SETTTINGS
"""
LONG_DELAY_AMOUNT: int = 30  # how long it takes for a mod to donwload on average
SHORT_DELAY_AMOUNT: int = 5  # how long it takes for a browser to load the nmm page
OPEN_VORTEX_X: int = 2805
OPEN_VORTEX_Y: int = 292

def main() -> None:
    """
    Drives the NMM behavior. Behavior is sequential and not tested in unique workspaces.
    """
    mod_count: int = input("enter number of mods (numerical only): ")
    print("Virtual desktop should have the browser and vortex mod manager open only")
    print("Program starts in 5 seconds!")

    # auto.displayMousePosition() # USE THIS TO QUICKLY FIGURE OUT YOUR CUSTOM POSITIONS!
    take_screenshot()
    countdown(5)

    num_mods_completed = 0
    for x in range(int(mod_count)):
        find_and_click_button(DOWNLOAD_BUTTON_IMG)
        countdown(int(SHORT_DELAY_AMOUNT))
        find_and_click_button(SLOW_DOWNLOAD_BUTTON_IMG)
        press_open_vortex()
        countdown(int(LONG_DELAY_AMOUNT))
        detect_if_still_previous_image(0)

        num_mods_completed += 1
        print(f"Completion Counter: {num_mods_completed}/{mod_count}")


def find_and_click_button(button_name: str) -> None:
    """Provided a button name stored in images resource,
    openCV checks all monitors for these pixels with a
    predetermined confidence score. When found, the button
    is selected.

    Args:
        button_name (str): image searched by openCV on screen

    Returns:
        _type_: _description_
    """
    print("Looking for 'download_button.png'...")
    try:
        icon_location = auto.locateOnScreen(f"images/{button_name}", confidence=0.9)

        if icon_location:
            auto.click(auto.center(icon_location))
            auto.click(auto.center(icon_location))
            print(f"Clicked the {button_name} icon")

    except ImageNotFoundException as e:
        print(f"An error occurred: {e}")


def take_screenshot() -> None:
    """Takes a screenshot of vortex in the region where
    the mod download appears. This allows the program to
    utilize openCV to determine if we have progressed from the
    current mod download.
    """
    # TODO: Either make these fields dynamic or make them user configs
    left = 2270
    top = 18
    width = 600
    height = 400
    right = left + width
    bottom = top + height

    crop_region = (left, top, right, bottom)

    full_screenshot = auto.screenshot()
    # Pillow crop and saving to PNG is LOSSLESS
    cropped_image = full_screenshot.crop(crop_region)
    cropped_image.save(f"images/temp/{REGION_SCREENSHOT}")


def detect_if_still_previous_image(num_retry: int) -> None:
    """Aims to determine if vortex is still likely processing the same mod.
    When the program is unable to detect we are in the same state, pyAuto
    throws an exception, therefore, we have completed downloading a mod and
    we take an early return.
    When we keep detecting we are downloading the same mod, the program sleeps
    for 90 seconds at a time. On the second occurrence, we assume we are not
    dowloading the mod and go for a manual click to downlaod the mod on
    the nexus page.

    Args:
        num_retry (int): recurisve calls hits max, we are stuck, force manual download
    """
    try:
        icon_location = auto.locateOnScreen(
            f"images/temp/{REGION_SCREENSHOT}", confidence=0.9
        )
    except ImageNotFoundException as e:
        print(
            f"Icon Location cannot be found - Likely completed downloading a heavy mod - {e}"
        )
        return

    num_retry += 1
    if num_retry == 2:
        print(f"Exceeded max num of sleep - manual download - {CLICK_HERE_BUTTON}")
        find_and_click_button(CLICK_HERE_BUTTON)

    if icon_location:
        print(f"previous state detected, trying after {LONG_DELAY_AMOUNT*3}")
        mouse_jiggler()
        countdown(int(LONG_DELAY_AMOUNT * 3))
        mouse_jiggler()
        detect_if_still_previous_image(num_retry)


def mouse_jiggler() -> None:
    """Mouse jiggler helps to reduce sleep scenarios
    """
    auto.moveTo(OPEN_VORTEX_X, OPEN_VORTEX_Y)
    auto.click()


def countdown(seconds: int) -> None:
    """Displays a countdown of the sleep timer on the console

    Args:
        seconds (int): time limit of the timer
    """
    for i in range(seconds, 0, -1):
        print(f"Sleeping for {i:2d} seconds\r", end="")
        sys.stdout.flush()  # Ensure the output is immediately written
        time.sleep(1)


def press_open_vortex() -> None:
    """
    Navigates the mouse cursor to the vortex application, helps to reduce sleep scenarios
    Likely to be deprecated in the future
    """
    auto.moveTo(OPEN_VORTEX_X, OPEN_VORTEX_Y)
    auto.click()


if __name__ == "__main__":
    main()
