import sys
from os import path
sys.path.append(path.abspath(path.join(path.dirname(__file__), "../")))

from SeventFt10.C4 import Factory, C4Node

def test_LoadFromYaml():
	BankingCustomer:C4Node = Factory.LoadYamlFromUrl('https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/Repository/Personas/Banking%20Customer.yaml')
	assert BankingCustomer != None

def test_SaveIconFromBase64():
	icon = Factory._GetIcons().get("persona")
	assert Factory.SaveIconFromBase64("./tests/_test.png", icon) == "./tests/_test.png"

def run_all():
	test_LoadFromYaml()
	test_SaveIconFromBase64()

run_all()
