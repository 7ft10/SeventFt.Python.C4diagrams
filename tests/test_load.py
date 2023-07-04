import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from SeventFt10.C4 import Diagram, Repository, Factory, C4Node

def test_load():
    # ARRANGE
    file_name = '_test_load'

    # ACT
    Repo = Repository.LoadFromUrl('https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/Repository/', module_name = "Repository")

    # ASSERT
    with Diagram(name = "test_load", filename = file_name):
        assert isinstance(Repo.Personas.BankingCustomer.Get(), C4Node)

    assert isinstance(Repo.Personas.BankingCustomer, Factory)

    # ANNIHILATE
    try:
        files = ['..\\' + file_name + '.png', '..\\_default_icon.png', '..\\_persona.png']
        for file in files:
            f = os.path.join(os.path.dirname(__file__), file)
            if os.path.isfile(f):
                os.remove(f)
    except:
        pass

def run_all():
	test_load()

run_all()
