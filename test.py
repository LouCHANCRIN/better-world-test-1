
import unittest

from main import test_chain

well_formatted_chains = [
  '()',
  '())()()()()',
  '((((()()()))))',
  '((())) ',
  '',
]

ill_formatted_chains = [
  ')(',
  '()())(()()',
  '(((()()()()()()))))',
  '(((()))))',
  '(',
]

class TestChains(unittest.TestCase):

    def test_well_formatted(self):
      for chain in well_formatted_chains:
        self.assertTrue(test_chain(chain))

    def test_ill_formatted(self):
      for chain in ill_formatted_chains:
        self.assertFalse(test_chain(chain))

if __name__ == '__main__':
    unittest.main()