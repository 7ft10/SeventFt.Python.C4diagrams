"""
A set of nodes and edges to visualize software architecture using the C4 model.
"""
from diagrams import Node, Cluster, Edge
from .FormatterMixIn import Formatter

from diagrams import Diagram as _D

class Diagram(_D):
    pass

class C4Node(Formatter, Node):
    def __init__(self, name, summary = "", description = "", type = "Container", **kwargs):
        self._icon = kwargs.get('icon_path', None)
        key = f"{type}: {summary}" if summary else type
        label = self._format_node_label(name, key, description)
        attributes = {
            #"icon_path": kwargs.get('icon_path') if kwargs.get('icon_path') else None,
            "labelloc": "c",
            "shape": "rect",
            "width": "2.6",
            "height": "1.6",
            "fixedsize": "true",
            "style": "filled",
            "fillcolor": "dodgerblue3",
            "fontcolor": "white",
        }
        # collapse boxes to a smaller form if they don't have a description
        if not description:
            attributes.update({"width": "2", "height": "1"})
        attributes.update(kwargs)
        super().__init__(label, **attributes)

    def _load_icon(self):
        if self._icon == None:
            return super()._load_icon()
        else:
            return self._icon

class SystemBoundary(Formatter, Cluster):
    def __init__(self, label, **kwargs):
        attributes:dict[str, any] = {
            "label": self._format_escape(label),
            "bgcolor": "white",
            "margin": "16",
            "style": "dashed",
        }
        attributes.update(kwargs)
        super().__init__(label = attributes.pop('label'), graph_attr = attributes)

class Relationship(Formatter, Edge):
    def __init__(self, label = "", **kwargs):
        attributes:dict[str, any] = {
            "style": "dashed",
            "color": "gray60",
            "label": self._format_edge_label(label) if label else "",
        }
        attributes.update(kwargs)
        super().__init__(label = attributes.pop('label'), **attributes)

class Container(C4Node):
    def __init__(self, name, summary = "", description = "", **kwargs:dict[str, any]):
        external = self._to_bool(kwargs.pop('external', False))
        attributes:dict[str, any] = { }
        attributes.update(kwargs)
        super().__init__(name, summary, description, "Container", **attributes)

class Database(C4Node):
    def __init__(self, name, summary = "", description = "", **kwargs:dict[str, any]):
        external = self._to_bool(kwargs.pop('external', False))
        attributes:dict[str, any] = {
            "shape": "cylinder",
            "labelloc": "b",
        }
        attributes.update(kwargs)
        super().__init__(name, summary, description, "Database", **attributes)

class System(C4Node):
    def __init__(self, name, summary = "", description = "", **kwargs:dict[str, any]):
        external = self._to_bool(kwargs.pop('external', False))
        attributes:dict[str, any] = {
            "label2": "External System" if external else "System",
            "fillcolor": "gray60" if external else "dodgerblue4",
        }
        attributes.update(kwargs)
        super().__init__(name, summary, description, "Database", **attributes)

class Persona(C4Node):
    def __init__(self, name, summary = "", description = "", **kwargs:dict[str, any]):
        external = self._to_bool(kwargs.get('external', False))
        attributes:dict[str, any] = {
           "_icon": kwargs.get('icon_path', None),
            "label2": "External Person" if external else "Person",
            "fillcolor": "gray60" if external else "dodgerblue4",
            "style": "rounded,filled",
        }
        attributes.update(kwargs)
        super().__init__(name, summary, description, "Persona", **attributes)

class Component(C4Node):
    def __init__(self, name, summary = "", description = "", **kwargs:dict[str, any]):
        external = self._to_bool(kwargs.pop('external', False))
        attributes:dict[str, any] = { }
        attributes.update(kwargs)
        super().__init__(name, summary, description, "Component", **attributes)

class Code(C4Node):
    def __init__(self, name, summary = "", description = "", **kwargs:dict[str, any]):
        external = self._to_bool(kwargs.get('external', False))
        match kwargs.pop('type', "module"):
            case "module": shape = "note"
            case "abstract": shape = "tab"
            case "interface": shape = "circle"
        attributes:dict[str, any] = {
            "shape": shape,
            "fixedsize": "true" if shape == "circle" else "false",
            "fillcolor": "gray60" if external else "dodgerblue4",
            "fontcolor": "black" if shape == "circle" else "white",
            "width": "0.6" if shape == "circle" else "2.6",
            "height": "0.6" if shape == "circle" else "1.6",
        }
        attributes.update(kwargs)
        super().__init__(name, summary, description, type, **attributes)
