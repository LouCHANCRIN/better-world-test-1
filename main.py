def test_chain(chain: str) -> bool:
  '''
  Take a string of parenthesis only and return wether or not it is well formatted.
  A well formatted string means that all opening parenthesis are closed later on and
  all closed parenthesis are placed when there is an open parenthesis that is not closed yet
  '''
  opened_parenthesis = 0
  for char in chain:
    if char == '(':
      opened_parenthesis += 1
    elif char == ')':
      if opened_parenthesis > 0:
        opened_parenthesis -= 1
      else:
        return False
    else:
      return False
  
  if opened_parenthesis != 0:
    return False

  return True
