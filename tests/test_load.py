from SeventFt10.C4 import Repository

def test_load():
    Repo = Repository.LoadFromUrl('https://raw.githubusercontent.com/7ft10/C4ArchitectureExamples/main/Repository/', module_name = "Repository")
    Repo.Personas.BankingCustomer.Print()

test_load()