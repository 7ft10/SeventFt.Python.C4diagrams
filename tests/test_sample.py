import sys
sys.path.insert(1, 'C:\\Users\\mike\\Documents\\Github\\SevenFt10.Python.C4diagrams\\')

from SeventFt10.C4 import Factory

def test_LoadFromYaml():
	BankingCustomer = Factory.LoadFromYaml('https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/Repository/Personas/Banking%20Customer.yaml')
	assert BankingCustomer != None

def test_SaveIconFromBase64():
	icon = Factory._GetIcons().get("persona")
	assert Factory.SaveIconFromBase64("./tests/_test.png", icon) == "./tests/_test.png"

def run_all():
	test_LoadFromYaml()
	test_SaveIconFromBase64()

run_all()
