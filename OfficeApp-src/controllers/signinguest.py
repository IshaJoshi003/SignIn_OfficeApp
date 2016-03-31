# -*- coding: utf-8 -*-

# function which prompts visitors to enter their details
def index(): 
    #SQLFORM.factory which generates a form very similar to SQLFORM from the description of a table 'visit_log'with python dictionary.
    form=SQLFORM.factory(db.visit_log,labels = {'name':'Enter your Name:','phone_number':'Enter your phone number','email':'Enter your email address','address':'Enter your address',
                                                'emp_id':'Enter Employee Id'},
                         fields=['name','phone_number','email','address','emp_id'],submit_button='Sign In').process()
    if form.accepted:
        response.flash=T( 'Form has accepted!')
        # inserts data into database table 'visit_log'
        db.visit_log.insert(**db.visit_log._filter_fields(form.vars))
        # redirects URL to welcome index and passes name to index function of welcome.py 
        redirect(URL('welcome' ,'index',vars={'name':form.vars.name} ))

    elif form.errors:
        response.flash = T('form has errors ')
    else :
        pass

    return locals()
