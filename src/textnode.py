
from htmlnode import LeafNode, ParentNode, HTMLNode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    

def text_node_to_html(text_node):
    if text_node is None:
        raise Exception("Incorrect Typing for text node")
    elif text_node == text_type_text:
        return LeafNode(None,text_node,None)
    elif text_node == text_type_bold:
        return LeafNode("b",text_node,None)
    elif text_node == text_type_italic:
        return LeafNode("i",text_node,None)
    elif text_node == text_type_code:
        return LeafNode("code",text_node,None)
    elif text_node == text_type_link:
        return LeafNode("a",text_node,"href")
    elif text_node == text_type_image:
        return LeafNode("imf",text_node,None)