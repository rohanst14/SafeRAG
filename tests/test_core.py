from saferag import answer
import unittest
class Tests(unittest.TestCase):
    def test_grounding(self): self.assertEqual(answer("reactor pressure",{"a":"reactor pressure rises","b":"ocean waves"})["citations"],["a"])
    def test_abstention(self): self.assertTrue(answer("banana",{"a":"pressure"})["abstained"])
    def test_empty(self): self.assertTrue(answer("",{})["abstained"])
