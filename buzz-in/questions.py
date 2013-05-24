#/usr/bin/python
#
# Copyright 2013 Luke Hackett
# https://github.com/LukeHackett
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random

class Questions(object):

	def __init__(self):
		pass		


	def get_questions(self):
		return { "What is five plus seven?" : "12",
			 "Which day occurs after Monday?" : "Tuesday",
			 "How may days are there in a year?" : "365",
			 "David Beckham has played for Manchester United (True or False)?" : "True"
			}

	def get_random_question(self):
		questions = self.get_questions()
		question = random.sample(questions, 1)[0]
		answer = questions[question]
		return (question, answer)

