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


def find_subchain(chain: str) -> list[str]:
  well_formatted_subchains = []
  opened_parenthesis = 0
  subchain = ''
  
  for i in range(0, len(chain)):
    subchain += chain[i]
    if chain[i] == '(':
      opened_parenthesis += 1
    elif chain[i] == ')':
      if opened_parenthesis > 0:
        opened_parenthesis -= 1
      else:
        subchain = subchain[1:]
        if subchain:
          well_formatted_subchains.append(subchain[1:])
        subchain = ''

    if opened_parenthesis == 0 and subchain:
      well_formatted_subchains.append(subchain)
      subchain = ''
  if opened_parenthesis > 0 and subchain:
    well_formatted_subchains += find_subchain(subchain[1:])
    
  return well_formatted_subchains

def find_wellformed_subchain(chain: str) -> int:
  '''Take a well formatted chain and find the size of the longest subchain'''
  subchains = find_subchain(chain)
  subchains_length = [len(subchain) for subchain in subchains]
  if subchains_length:
    return max(subchains_length)
  else:
    return 0
