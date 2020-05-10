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
import jinja2
import webapp2
import os
import logging
import re

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class HintsHandler(webapp2.RequestHandler):
    def post(self):
        wordlength = self.request.get("wordlength").strip()
        letters    = self.request.get("letters").lower().replace(' ','',12)
        filters    = self.request.get("filters").lower().replace(' ','',12)
        answers = "No valid answers."
        if re.search(r'\d', wordlength) and 3<=int(wordlength)<=9:
           try:
              words = " ".join(open("w%s" % wordlength).readlines()).split()
              filterlist = ''.join(set(letters))
   
              cnt=0
              answers = "<b>Possible answers are:</b><br>"
              for word in words:
                  if not re.search(r'[^%s]' % filterlist, word):
                     skip = False
                     for ch in filterlist:
              	         if word.count(ch)>letters.count(ch):
              	            skip = True
              	            break
                     if skip:
              	        continue
                     if len(filters)==int(wordlength) and not re.search(r'%s' % filters, word):
                        continue
                     cnt+=1
                     answers += " %s" % word
              if cnt==0:
                 answers = "No valid answers."
           except:
              answers = "Error executing scrpt."
        else:
           answers = "Wordlength must be between 3 to 9."

        logging.info("wordlength %s [%s] [%s]" % (wordlength, letters, answers))
        template_values = {
                           "answers":answers
                          }
        template = jinja_environment.get_template('templates/answers.htm')
        self.response.out.write(template.render(template_values))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {
                             "wordlength":"",
                             "letters":"",
                             "filters":"",
                          }
        template = jinja_environment.get_template('templates/index.htm')
        self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([
                                ('/', MainHandler),
                                ('/gethints', HintsHandler),
                              ], debug=True)
