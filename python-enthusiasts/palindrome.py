spec_chars = [';', ':', '!', "*", ' ', ',']

def sanitize(string):
  #Convert string to all lowercase and remove all special chars
  clean = string.lower()
  clean = ''.join((filter(lambda c: c not in spec_chars, clean)))
  return clean

def main():
  strs = []
  answers = []

  #Build list of phrases from user
  num = input("How many phrases: ")
  for x in range(int(num)):
    strs.append(input("Phrase " + str(x + 1) + ": "))

  #Take a cleaned string and determine if it's a palindrome or not
  for s in strs:
    clean = sanitize(s)
    mod = len(clean)%2
    mid = len(clean)//2

    if mod == 1: # If the string is odd length, remove the middle char
      if clean[:mid] == clean[mid+1:][::-1]: #Split phrase in half and reverse the last half. Compare if both are the same or not.
        answers.append('Y')
      else:
        answers.append('N')
    elif mod == 0: # If the string is even length, keep middle char
      if clean[:mid] == clean[mid:][::-1]: #Split phrase in half and reverse the last half. Compare if both are the same or not.
        answers.append('Y')
      else:
        answers.append('N')

  for a in answers:
    print(a, end = ' ')

  print()

if __name__ == "__main__":
  main()
