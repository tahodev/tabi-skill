import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location(
    'check_urls', Path(__file__).resolve().parents[1] / 'scripts/check-urls.py')
check_urls = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_urls)


class MaterializeTests(unittest.TestCase):
    def test_date_variable_forms(self):
        for variable in ('{TRAVEL_DATE}', '${TRAVEL_DATE}', '$TRAVEL_DATE'):
            with self.subTest(variable=variable):
                self.assertEqual(check_urls.materialize('https://example.test/?date=' + variable),
                                 'https://example.test/?date=20260919')

    def test_mixed_key_and_shell_date(self):
        self.assertEqual(
            check_urls.materialize('https://example.test/?key={KEY}&date=${TRAVEL_DATE}'),
            'https://example.test/?key=INVALID_CI_KEY&date=20260919')

    def test_unknown_variables(self):
        for variable in ('{UNKNOWN}', '${UNKNOWN}', '$UNKNOWN'):
            with self.subTest(variable=variable):
                self.assertEqual(check_urls.materialize('https://example.test/?q=' + variable),
                                 'https://example.test/?q=ci-probe')

    def test_extracted_terminal_placeholder_keeps_brace(self):
        for url in check_urls.items:
            if url.endswith('{KEY') or url.endswith('${TRAVEL_DATE'):
                self.fail('URL extraction removed a placeholder closing brace: ' + url)
        self.assertTrue(any(url.endswith('serviceKey={KEY}') for url in check_urls.items))

    def test_literal_url_is_unchanged(self):
        url = 'https://example.test/?literal=20260919&encoded=%24%7BKEY%7D'
        self.assertEqual(check_urls.materialize(url), url)


if __name__ == '__main__':
    unittest.main()
