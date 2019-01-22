"""Does a given string have balanced pairs of brackets?

Given a string, return True or False depending on whether the string
contains balanced (), {}, [], and/or <>.

Many of the same test cases from Balance Parens apply to the expanded
problem, with the caveat that they must check all types of brackets.

These are fine::

   >>> has_balanced_brackets("<ok>")
   True

   >>> has_balanced_brackets("<{ok}>")
   True

   >>> has_balanced_brackets("<[{(yay)}]>")
   True

These are invalid, since they have too many open brackets::

   >>> has_balanced_brackets("(Oops!){")
   False

   >>> has_balanced_brackets("{[[This has too many open square brackets.]}")
   False

These are invalid, as they close brackets that weren't open::

   >>> has_balanced_brackets(">")
   False

   >>> has_balanced_brackets("(This has {too many} ) closers. )")
   False

Here's a case where the number of brackets opened matches
the number closed, but in the wrong order::

    >>> has_balanced_brackets("<{Not Ok>}")
    False

If you receive a string with no brackets, consider it balanced::

   >>> has_balanced_brackets("No brackets here!")
   True

"""

class Stack:
 def __init__(self):
   self.items = []

 def isEmpty(self):
   return self.items == []

 def push(self, item):
   self.items.append(item)

 def pop(self):
   return self.items.pop()

 def peek(self):
   return self.items[len(self.items)-1]

 def size(self):
   return len(self.items)


def has_balanced_brackets(phrase):
  """Does a given string have balanced pairs of brackets?

  Given a string as input, return True or False depending on whether the
  string contains balanced (), {}, [], and/or <>.
  """
  stack = Stack()
  opening_set = set(['<','[','{','('])
  closing_set = set(['>',']','}',')'])
  pairs = {'>':'<', ']':'[', '}':'{', ')':'('}

  if phrase[0] in closing_set:
    return False

  for ch in phrase:
    if ch in opening_set:
      stack.push(ch)
    elif ch in closing_set and not stack.isEmpty():
      paren = stack.pop()
      if pairs.get(ch) != paren:
        return False
    elif ch in closing_set and stack.isEmpty():
      return False

  return stack.isEmpty()

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY BRACKETS!\n")
