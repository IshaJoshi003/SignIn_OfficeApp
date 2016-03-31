# -*- coding: utf-8 -*-
# function prints welcome message to visitor and takes arguments from signin guest
def index():
    message="welcome %s " % request.vars.name ," Please wait in the lobby"
   
    return locals()
