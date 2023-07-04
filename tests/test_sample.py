import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from SeventFt10.C4 import Factory

def test_SaveIconFromBase64():
    #ARRANGE
    file_name = '.\\tests\\_test.png'

    # ACT
    icon = Factory._GetIcons().get("persona")

    # ASSERT
    assert Factory.SaveIconFromBase64(file_name, icon) == file_name

    # ANNIHILATE
    try:
        files = ['..\\' + file_name, '..\\_default_icon.png', '..\\_persona.png']
        for file in files:
            f = os.path.join(os.path.dirname(__file__), file)
            if os.path.isfile(f):
                os.remove(f)
    except:
        pass

def run_all():
    test_SaveIconFromBase64()

run_all()
