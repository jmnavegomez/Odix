from odix.tabula.nodes import Text
from odix.tabula.visitor import Visitor


class TestVisitor(Visitor):

    def visit_text(self, node):
        return "text"


def test_visit_dispatches_to_specific_method():
    node = Text("Hello")

    visitor = TestVisitor()

    assert visitor.visit(node) == "text"


from odix.tabula.nodes import Paragraph
from odix.tabula.visitor import Visitor


class TestVisitorEmpty(Visitor):
    pass


def test_visit_uses_generic_visit_when_missing():
    node = Paragraph()

    visitor = TestVisitorEmpty()

    assert visitor.visit(node) == []


class TestVisitorVisit(Visitor):

    def visit_text(self, node):
        return node.content()[0]


def test_generic_visit_visits_children():
    paragraph = Paragraph()
    paragraph.add_child(Text("Hello"))
    paragraph.add_child(Text("World"))

    visitor = TestVisitorVisit()

    assert visitor.visit(paragraph) == ["Hello", "World"]


class TestVisitorDiffusion(Visitor):

    def visit_text(self, node):
        return 42


def test_visit_returns_specific_result():
    node = Text("Hello")

    visitor = TestVisitorDiffusion()

    assert visitor.visit(node) == 42


class TestVisitorName(Visitor):

    def visit_paragraph(self, node):
        return "paragraph"


def test_dispatch_uses_class_name():
    visitor = TestVisitorName()

    assert visitor.visit(Paragraph()) == "paragraph"
