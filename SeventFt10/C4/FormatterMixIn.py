"""
Formatter Mix in
"""
import html
import textwrap

class Formatter:
    def _format_node_label(self, name:str, key:str, description:str) -> str:
        """
        Create a graphviz label string for a C4 node
        """
        title = f'<font point-size="12"><b>{html.escape(name)}</b></font><br/>'
        subtitle = f'<font point-size="9">[{html.escape(key)}]<br/></font>' if key else ""
        text = f'<br/><font point-size="10">{self._format_description(description)}</font>' if description else ""
        return f"<{title}{subtitle}{text}>"

    def _format_description(self, description:str) -> str:
        """
        Formats the description string so it fits into the C4 nodes.

        It line-breaks the description so it fits onto exactly three lines. If there are more
        than three lines, all further lines are discarded and "..." inserted on the last line to
        indicate that it was shortened. This will also html-escape the description so it can
        safely be included in a HTML label.
        """
        wrapper = textwrap.TextWrapper(width = 40, max_lines = 4)
        lines = [html.escape(line) for line in wrapper.wrap(description)]
        lines += [""] * (4 - len(lines))  # fill up with empty lines so it is always three
        return "<br/>".join(lines)

    def _format_edge_label(self, description:str) -> str:
        """
        Create a graphviz label string for a C4 edge
        """
        wrapper = textwrap.TextWrapper(width = 24, max_lines = 4)
        lines = [html.escape(line) for line in wrapper.wrap(description)]
        text = "<br/>".join(lines)
        return f'<<font point-size="10">{text}</font>>'

    def _format_escape(self, text) -> str:
        """
        html escape the text
        """
        return html.escape(text)

    def _to_bool(self, value:any) -> bool:
        """
        Ensure a bool is returned
        """
        if isinstance(value, bool): return value
        if not isinstance(value, str): raise ValueError('invalid literal for boolean. Not a string.')
        valid = { 'true': True, 't': True, '1': True, 'false': False, 'f': False, '0': False }
        lower_value = value.lower()
        if lower_value in valid:
            return valid[lower_value]
        else:
            raise ValueError('invalid literal for boolean: "%s"' % value)
