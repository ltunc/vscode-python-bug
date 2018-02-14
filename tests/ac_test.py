from unittest import TestCase

# Broken discovery

class AADemoBbTest(TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_true_fail(self):
        self.assertTrue(False)
