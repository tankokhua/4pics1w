#!/usr/bin/python

import os, sys, re
import string

def HintsHandler(_wordlength, _letters, _filters, _musthave):
    print ("length   : %s" % _wordlength)
    print ("letters  : %s" % _letters)
    print ("filters  : %s" % _filters)
    print ("musthave : %s\n" % _musthave)
    _answers = "No valid answers."

    _mcnts = []
    for x in range(len(_musthave)):
        _mcnts.append(len(_musthave[x].replace('.','')))
    print ("_mcnts", _mcnts)

    _mcnt = len(_musthave[0].replace('.',''))
    skipch = False
    if _mcnt < len(_musthave[0]):
       skipch = True

#   print 'mcnt', _mcnt, len(_musthave), ' skipch', skipch

    cnt=0
    if re.search(r'\d', _wordlength) and 3<=int(_wordlength)<=9:
       try:
          words = " ".join(open("w%s" % _wordlength).readlines()).split()
          filterlist = ''.join(set(_letters))
   
          _answers = ""
          for word in words:
              mcnt = _mcnt
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
                 if _musthave[0] == "":
                    _answers += "%s" % word
                    cnt+=1
                    if cnt%10==0:
                       _answers += "\n"
                    else:
                       _answers += " "
                 else:
                    
#                   print word
                    for idx, ch in enumerate(_musthave[0]):
                        if ch == '.':
                           continue
                        if skipch and word[idx] == ch:
                          #print idx, ch, _musthave[idx], word[idx], word
                           continue
                        if ch in word:
                           mcnt -= 1
                    if mcnt == 0:
                       _answers += "%s" % word
                       cnt+=1
                       if cnt%10==0:
                          _answers += "\n"
                       else:
                          _answers += " "

          if cnt==0:
             _answers = "No valid answers."
       except:
          _answers = "Error executing script."
    else:
       _answers = "Wordlength must be between 3 to 9."

    return (_answers, cnt)


if __name__ == '__main__':
   
   wl = "5"
   ltrs = "abcdefghij"
   fltrs = "." * int(wl)
   musthaves = [""]

   if len(sys.argv)>=2:
      ltrs = sys.argv[1]

   if len(sys.argv)>2:
      fltrs = sys.argv[2]

   if len(sys.argv)>3:
      x = 3
      musthaves = []
      while x < len(sys.argv):
            musthaves.append(sys.argv[x])#= [sys.argv[3:]]
            x+=1
      

   lts = string.ascii_lowercase * 2 #letters.lower()

   _ltrs = ""
   for l in lts:
       if l not in ltrs:
          _ltrs += l

   print (_ltrs)

   results = HintsHandler(wl, _ltrs, fltrs, musthaves)
   if results[1] > 0:
      print (results[0])
      print ("Num of matches:", results[1])
