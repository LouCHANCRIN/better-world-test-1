
import unittest

from main import test_chain, find_subchain

well_formatted_chains = [
  '()',
  '()()()()()',
  '((((()()()))))',
  '((()))',
  '',
]

ill_formatted_chains = [
  ')(',
  '()())(()()',
  '(((()()()()()()))))',
  '(((()))))',
  '(',
]

class TestChainsFormat(unittest.TestCase):

  def test_well_formatted(self):
    for chain in well_formatted_chains:
      print(chain)
      self.assertTrue(test_chain(chain))

  def test_ill_formatted(self):
    for chain in ill_formatted_chains:
      self.assertFalse(test_chain(chain))


class TestFindSubchains(unittest.TestCase):

  def test_find_subchains(self):
    self.assertEqual(find_subchain(')('), [])
    self.assertEqual(find_subchain('()())(()()'), ['()', '()', '()', '()'])
    self.assertEqual(find_subchain('(((()))))'), ['(((())))'])
    self.assertEqual(find_subchain('('), [])
    



if __name__ == '__main__':
    unittest.main()