# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
    """
    #response.flash = "Welcome to web2py!"
    redirect (URL('pesquisa', 'default','data_crud')+"/create/campos/?_next=/pesquisa/default/")


def resultado():
    dic = {}
    for estado in state_list: 
        campos = db(Campos.estado == estado).select(Campos.ALL)
        
        qty_junior = 0
        qty_pleno = 0
        qty_senior = 0
        qty_outro = 0        
        total_salario_junior = 0
        total_salario_pleno = 0
        total_salario_senior = 0 
        total_salario_outro = 0
        
        
        
        for campo in campos:
               if campo.nivel == level_list[0]:
                   qty_junior = qty_junior + 1
                   total_salario_junior = total_salario_junior + campo.salario
                   
               elif campo.nivel == level_list[1]:
                   qty_pleno = qty_pleno + 1           
                   total_salario_pleno = total_salario_pleno + campo.salario
               
               elif campo.nivel == level_list[2]:
                   qty_senior = qty_senior + 1
                   total_salario_senior = total_salario_senior + campo.salario
                   
               elif campo.nivel == level_list[3]:
                   qty_outro = qty_outro + 1
                   total_salario_outro = total_salario_outro + campo.salario
               
        try:
            media_salario_junior = float(total_salario_junior)/qty_junior
        
        except:
            media_salario_junior = 0
            
        try:
            media_salario_pleno = float(total_salario_pleno)/qty_pleno
        
        except:
            media_salario_pleno = 0
            
        try:
            media_salario_senior = float(total_salario_senior)/qty_senior
        
        except:
            media_salario_senior = 0
            
        try:
            media_salario_outros = float(total_salario_outros)/qty_outros
        
        except:
            media_salario_outros = 0                        


        
        dic[estado] = {'junior': media_salario_junior,
                       'pleno': media_salario_pleno,
                       'senior': media_salario_senior, 
                       'outros':media_salario_outros
                      }
        
    return {"dic": dic, "state_list": state_list}

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

def data_crud():
    return dict(form=crud())
