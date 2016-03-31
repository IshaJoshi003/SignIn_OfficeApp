# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('Office_App !!'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href="http://www.myofficeapp.com/",
                  _id="web2py-logo")
# display Office App on screen
response.title = request.application.replace('_',' ').title()
response.subtitle = ''


## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [ (T('Home'), False, URL('home', 'index'), [])]



if "auth" in locals(): auth.wikimenu()
