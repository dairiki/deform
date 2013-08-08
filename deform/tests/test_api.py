import unittest
import warnings
from zope.deprecation import __show__

class TestAPI(unittest.TestCase):
    def test_it(self):
        __show__.off()
        # none of these imports should fail
        from deform import Form
        from deform import Button
        from deform import Field

        from deform import FileData
        from deform import Set

        from deform import ValidationFailure
        from deform import TemplateError

        from deform import ZPTRendererFactory
        from deform import default_renderer

        from deform import widget
        __show__.on()

    def test_Set_deprecation(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("error")
            def import_Set():
                from deform import Set
            self.assertRaises(DeprecationWarning, import_Set)
