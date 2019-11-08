'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  count = 0
  i = 0

  def get_count():

    nonlocal count
    nonlocal i

    # If end of loop reached, stop
    if i >= len(word)-1:
      return

    # If second to last letter not `t`, stop
    if i == len(word)-2 and word[i] != "t":
      return

    # If prev check passes but following letter isn't `h` stop
    if i == len(word)-2 and word[i+1] != "h":
      return

    # If letter is "t" and next letter "h", incr count by 1 and incr index by 2
    if word[i] == "t" and word[i+1] == "h":
      count += 1
      i += 2
      get_count()

    # If letter is not "t" and next letter isn't "h" incr index by 1
    else:
      i += 1
      get_count()
  
  get_count()
  
  return count
