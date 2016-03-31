# -*- coding: utf-8 -*-
# importing re module 

import re

# index() function which prompts admin to enter username and password
def index():

    
    form=FORM('Username',INPUT(_name="username",_VALUE=request.vars.username),'Password',INPUT(_name='password',_VALUE=request.vars.password,_type='password'), INPUT(_type='submit')).process()
    #form=SQLFORM.factory(Field('username'),Field('password'),_type='hidden').process()
    # passing vars 
    username=request.vars.username
    password=request.vars.password
    # use of regular expression 
    name_check=re.match(r'Admin101',str(username))
    passwd_check=re.match(r'root101',str(password))

    login=False
    # use of try and except which handles exception raised when Admin enters invalid username and password
    try:
        if form.accepted:
            if name_check and passwd_check:
                login=True
            else:
                raise Exception
    except Exception as e:
            response.flash=T('Invalid Username or Password')

    if login:
        redirect(URL('Admin'))
   

    return dict(form=form)


# admin function displays list of visitors
def Admin():
    #Define the query object. 
    if request.vars.date1 != None and request.vars.date2 !=None  and request.vars.date2 != "" and request.vars.date1 != "":
        query=((db.visit_log.date >= request.vars.date1) & (db.visit_log.date <= request.vars.date2))
    else:
        query=((db.visit_log.id > 0))

    #Define the fields to show on grid. 
    fields = (db.visit_log.id, db.visit_log.name, db.visit_log.phone_number,db.visit_log.address,db.visit_log.date, db.visit_log.email,db.visit_log.emp_id)

    #Define headers as dictionaries
    headers = {'visit_log.id':   'ID',
           'visit_log.name': ' Name',
           'visit_log.phone_number':'Phone_number',
           'visit_log.address': 'Address',
           'visit_log.date':'Date',
           ' visit_log.email':'Email',
            'visit_log.emp_id':'Employee_id'  }

    # default sort order on visitor_id
    default_sort_order=[db.visit_log.id]

    # Condition to check user put right date in To date and From Date box

    if (request.vars.date1 >= request.vars.date2):
        response.flash=T('To Date should be greater than From Date')
    else:
        pass
    
    # creating form
    form1=FORM('From Date', INPUT(_name='date1', _class='datetime', _VALUE=request.vars.date1),'To Date',INPUT(_name='date2', _class='datetime',_VALUE=request.vars.date2),INPUT(_type='submit'))    
    form1.add_button('Logout', URL('index'))
    #Creating the grid object
    form = SQLFORM.grid(query=query, fields=fields, headers=headers, orderby=default_sort_order,searchable=True, selectable=None,
                deletable=False, editable=False, maxtextlength=64, paginate=25, csv=True)

    # inserting form1 to form 
    form[0].insert(-1,form1)

    return dict(form=form)
