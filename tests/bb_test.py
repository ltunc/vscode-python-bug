from unittest import TestCase

# Broken discovery

class DemoBbTest(TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_true_fail(self):
        self.assertTrue(False)
