#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from flask import Flask, render_template, request
import jinja2
import os
import logging
import re

app = Flask(__name__)

#jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


@app.route('/gethints', methods=['GET', 'POST'])
def HintsHandler():
    _wordlength = request.form.get("wordlength").strip()
    _letters    = request.form.get("letters").lower().replace(' ', '', 12)
    _filters    = request.form.get("filters").lower().replace(' ', '', 12)
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
                 cnt+=1
                 _answers += " %s" % word
          if cnt==0:
             _answers = "No valid answers."
       except:
          _answers = "Error executing scrpt."
    else:
       _answers = "Wordlength must be between 3 to 9."

    logging.info("wordlength %s [%s] [%s]" % (_wordlength, _letters, _answers))
    return render_template("answers.htm", answers=_answers)

@app.route('/', methods=['GET', 'POST'])
def MainHandler():
    return render_template("index.htm", wordlength="", letters="", filters="")

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=True)
