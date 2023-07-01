"""
Factory
"""
import os
import yaml
from urllib import request, parse
from IPython.display import display, Markdown
from . import C4Node, Container, Persona, Database, System, Component, Code, System

class Factory():
	_baseUrl = "https://raw.githubusercontent.com/7ft10/SeventFt10.Python.C4diagrams/main/"

	def __init__(self, nodeType: str):
		self.nodeType = nodeType
		self.default_icon = Factory.GetIcon('_default_icon.png', self._baseUrl + 'Library/Icons/Missing.png')
		self.default_persona_icon = Factory.GetIcon('_persona.png', self._baseUrl + 'Library/Icons/Persona.png')

	@staticmethod
	def metadata(args = {}):
		"""
		"""
		def _metadata(func):
			func.metadata = args or {}
			func.metadata.setdefault('name', 'Name missing')
			func.metadata.setdefault('description', '')
			return func
		return _metadata

	@staticmethod
	def GetIcon(name: str, url: str):
		"""
		"""
		try:
			request.urlretrieve(url, name)
			return name
		except:
			return '_default_icon.png'

	@staticmethod
	def LoadFromYaml(url: str):
		"""
		"""
		path = "_" + os.path.basename(parse.urlparse(url).path) ## Temp file
		request.urlretrieve(url, path)
		with open(path, "r") as stream: archetype = yaml.safe_load(stream)
		id = str(archetype.get('id'))
		nodeType = str(archetype.get("nodeType"))
		globals()[id] = type(id, (Factory, ), {
			"__init__": lambda self : Factory.__init__(self, nodeType),
			"metadata": archetype
		})
		return globals()[id]()

	def Print(self):
		"""
		"""
		if (self.metadata != None) and (isinstance(self.metadata, type({}))):
			display(Markdown('---'))
			display(Markdown('## ' + self.__class__.__name__))
		if len(self.metadata.items()) > 0:
			table = """| Key         | Value       |
					| ----------- | ----------- |"""
			for k, v in self.metadata.items():
				table = table + "\n| " + k + " | " + (v if isinstance(v, str) else str(v)) + " |"
			display(Markdown(table))

	def Get(self) -> C4Node:
		"""
		"""
		md: dict = self.metadata.copy()
		md.setdefault('summary', '')

		if md.get("icon") != None:
			md["icon_path"] = Factory.GetIcon("_" + md.get('id') + ".png", md.get("icon"))

		match self.nodeType:
			case "Container":
				return Container( md.pop('name'), md.pop('summary'), md.pop('description'), **md )
			case "Persona":
				md.setdefault('icon_path', self.default_persona_icon)
				return Persona( md.pop('name'), md.pop('summary'), md.pop('description'), **md )
			case "Database":
				return Database( md.pop('name'), md.pop('summary'), md.pop('description'), **md )
			case "System":
				return System( md.pop('name'), md.pop('summary'), md.pop('description'), **md )
			case "Component":
				return Component( md.pop('name'), md.pop('summary'), md.pop('description'), **md )
			case "Code":
				return Code( md.pop('name'), md.pop('summary'), md.pop('description'), **md )
			case _:
				return System( md.pop('name'), md.pop('summary'), md.pop('description'), **md )
