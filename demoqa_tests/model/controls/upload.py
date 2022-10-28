from selene.support.shared import browser
import os

def file():
    # browser.element('#uploadPicture').send_keys(path)
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/kitty.png'))
