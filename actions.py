from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet


import sqlite3

class ActionSearchFaculty(Action):
    def name(self):
        return 'action_search_faculty'

    def run(self, dispatcher, tracker, domain):


        db = sqlite3.connect("sqlite.db")

        cursor = db.cursor()
           
        name = tracker.get_slot('faculty_name')
        query = "SELECT about FROM facultydata WHERE First_name="+name+";"
        cursor.execute(query)

        f=0
        l=[]
        for row in cursor:
            f=1
            c=list(row)
            if c is not None:
                l.append(c)
        if f==0:
            #description=glasearch(name)
            #we are not calling glasearch() function because we cannot make our key public
            
            dispatcher.utter_message("sorry no data found")
            return[SlotSet("faculty_name",None)]
        db.close()

        dispatcher.utter_message("here are the details of faculty you asked for")
        description = name
        dispatcher.utter_message("{}".format(l))
        return [SlotSet("faculty_name", description)]






class ActionSearchState(Action):
    def name(self):
        return 'action_search_state'

    def run(self, dispatcher, tracker, domain):

        db = sqlite3.connect("sqlite.db")

        cursor = db.cursor()
           
        name = tracker.get_slot("office_state")
       
        query = "SELECT city,address FROM officedata WHERE state="+name+";"
        cursor.execute(query)
        f=0
        l=[]
        for row in cursor:
            f=1
            c=list(row)
            if c is not None:
             l.append("address  : ")
             l.append(row)
        if f==0:
            dispatcher.utter_message("{}".format(description))
            return [SlotSet("office_state", None)]
        
        db.close()
        
        dispatcher.utter_message("here are the centres present in this state")
        description = l
        dispatcher.utter_message("{}".format(description))
        return [SlotSet("office_state", name)]

class ActionAddName(Action):
    def name(self):
        return'action_add_name'

    def run(self,dispatcher,tracker,domain):

        name=tracker.get_slot('student_name')
        return [SlotSet("student_name",name)]


class ActionAddDegree(Action):
    def name(self):
        return'action_add_degree'

    def run(self,dispatcher,tracker,domain):

        degree=tracker.get_slot('degree')
        return [SlotSet("degree",degree)]
        	
