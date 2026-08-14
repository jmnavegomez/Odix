from odix.typus.margins import Margins


def test_margins():
    margins = Margins(
        top="2cm",
        bottom="2cm",
        left="2cm",
        right="2cm",
    )

    assert margins.top == "2cm"
    assert margins.bottom == "2cm"
    assert margins.left == "2cm"
    assert margins.right == "2cm"
