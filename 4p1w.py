#!/usr/bin/env python
import os, sys, re

def HintsHandler(_wordlength, _letters, _filters, _musthave=""):
    _letters    = _letters.lower().replace(' ', '', 12)
    _filters    = _filters.lower().replace(' ', '', 12)
    _answers = "No valid answers."
    if re.search(r'\d', _wordlength) and 3<=int(_wordlength)<=9:
       try:
          words = " ".join(open("w%s" % _wordlength).readlines()).split()
          filterlist = ''.join(set(_letters))
   
          cnt=0
          _answers = ""
          for word in words:
              if not re.search(r'[^%s]' % filterlist, word):
                 skip = False
                 for ch in filterlist:
                   if word.count(ch)>_letters.count(ch):
                      skip = True
                      break
                 if skip:
                    continue
                 if len(_filters)==int(_wordlength) and not re.search(r'%s' % _filters, word):
                    continue
                 _answers += "%s" % word
                 cnt+=1
                 if cnt%10 == 0:
                    _answers += "\n"
                 else:
                    _answers += " "
          if cnt==0:
             _answers = "No valid answers."
       except:
          _answers = "Error executing scrpt."
    else:
       _answers = "Wordlength must be between 3 to 9."

    return _answers

if __name__ == '__main__':

   _musthave = ""

   if len(sys.argv)>=3: 
      _wordlength = sys.argv[1]
      _letters = sys.argv[2]
      _filters = '.'* len(_letters)

   if len(sys.argv)>=4: 
      _filters = sys.argv[3]

   print (HintsHandler(_wordlength, _letters, _filters, _musthave))
