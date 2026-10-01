from ColorSchemeUnit.lib.color_scheme import ColorSchemeResource
from ColorSchemeUnit.lib.color_scheme import ViewStyle
from ColorSchemeUnit.lib.color_scheme import load_color_scheme_resource
from ColorSchemeUnit.tests import unittest


class TestLoadColorSchemeResource(unittest.ViewTestCase):

    def test_load_color_scheme(self):
        self.assertIsColorScheme('ColorSchemeUnitTest', load_color_scheme_resource(
            'ColorSchemeUnitTest.hidden-color-scheme'))
        self.assertIsColorScheme('ColorSchemeUnitTest', load_color_scheme_resource(
            'Packages/ColorSchemeUnit/tests/fixtures/ColorSchemeUnitTest.hidden-color-scheme'))
        self.assertIsColorScheme('ColorSchemeUnitTest', load_color_scheme_resource(
            'ColorSchemeUnit/tests/fixtures/ColorSchemeUnitTest.hidden-color-scheme'))

    def test_load_color_scheme_legacy(self):
        self.assertIsColorScheme('ColorSchemeUnitLegacyTest', load_color_scheme_resource(
            'Packages/ColorSchemeUnit/tests/fixtures/ColorSchemeUnitLegacyTest.hidden-tmTheme'))
        self.assertIsColorScheme('ColorSchemeUnitLegacyTest', load_color_scheme_resource(
            'ColorSchemeUnit/tests/fixtures/ColorSchemeUnitLegacyTest.hidden-tmTheme'))
        self.assertIsColorScheme('ColorSchemeUnitLegacyTest', load_color_scheme_resource(
            'ColorSchemeUnitLegacyTest.hidden-tmTheme'))

    def assertIsColorScheme(self, name, resource):
        self.assertTrue(isinstance(resource, dict))
        self.assertTrue('name' in resource)
        self.assertEqual(resource['name'], name)


class TestViewStyle(unittest.ViewTestCase):

    def test_can_load(self):
        self.assertEqual(ViewStyle(self.view).view, self.view)

    def test_at_point(self):
        with self.loadColorScheme('ColorSchemeUnitTest.hidden-color-scheme'):
            self.fixture('\n\n<?php\n// comment\nif (CONSTANT === "string") {\n}\n')
            style = ViewStyle(self.view)

            s = style.at_point(0)
            self.assertEqual('#111111', s['background'])
            self.assertEqual('#eeeeee', s['foreground'])
            self.assertEqual('', s['fontStyle'])

            s = style.at_point(8)
            self.assertEqual('#111111', s['background'])
            self.assertEqual('#75715e', s['foreground'])
            self.assertEqual('', s['fontStyle'])

            s = style.at_point(19)
            self.assertEqual('#eeeeee', s['foreground'])
            self.assertEqual('italic', s['fontStyle'])

            s = style.at_point(23)
            self.assertEqual('#800080', s['foreground'])
            self.assertEqual('', s['fontStyle'])

            s = style.at_point(32)
            self.assertEqual('#ff0000', s['foreground'])
            self.assertEqual('bold', s['fontStyle'])

            s = style.at_point(37)
            self.assertEqual('#ffff00', s['foreground'])
            self.assertEqual('bold italic', s['fontStyle'])

    def test_at_point_legacy(self):
        with self.loadColorScheme('Packages/ColorSchemeUnit/tests/fixtures/ColorSchemeUnitLegacyTest.hidden-tmTheme'):
            s = ViewStyle(self.view).at_point(0)
            self.assertEqual('#333333', s['background'])
            self.assertEqual('#dddddd', s['foreground'])


class TestColorSchemeResource(unittest.ViewTestCase):

    def test_resource_content_is_dict(self):
        resource = ColorSchemeResource(self.view)
        self.assertTrue(isinstance(resource.content(), dict))

    def test_is_legacy_returns_bool(self):
        resource = ColorSchemeResource(self.view)
        self.assertTrue(isinstance(resource.isLegacy(), bool))
