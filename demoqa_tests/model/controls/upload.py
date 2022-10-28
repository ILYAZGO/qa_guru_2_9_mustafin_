from selene.support.shared import browser


def file(path):
    #browser.element('#uploadPicture').send_keys(path)
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/kitty.png'))