# -*- coding: utf-8 -*-
import gluon 
# database connection using DAL object
db = DAL('mysql://root:root@localhost/visitor_log', auto_import=True)
# table definition using gluon module
db.define_table(
    'visit_log',
    Field('visitor_id','id'),
    Field('name','string',requires=IS_NOT_EMPTY()),
    Field('phone_number','bigint',requires = IS_MATCH('^[1-9]\d{9}$',error_message='invalid phone number')),
    Field('email','string', requires=IS_EMAIL()),
    Field('date','datetime', default=request.now),
    Field('address','string'),
    Field('emp_id','integer'),
    redefine=True)







#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

## app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)


#if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    #db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'])
#else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    #db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    #session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')
