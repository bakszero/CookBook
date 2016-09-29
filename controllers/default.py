# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################
@auth.requires_login()
def index():
    if len(request.args): page=int(request.args[0])
    else: page=0
    items_per_page=5
    limitby=(page*items_per_page,(page+1)*items_per_page+1)
    rows = db().select(db.blog_post.ALL,limitby=limitby)
    items = db().select(db.blog_post.ALL)
    return locals()


@auth.requires_login()
def post():
    cols = db(db.blog_post.created_by==auth.user).select()
    return locals()

def vote():
    item = db.blog_post[request.vars.id]
    new_votes = item.votes + 1
    #if (new_votes==0):
     #   item.update_record(votes=new_votes)
    #elif (new_votes>=2):
      #  item.update_record(votes=0)
    #return str(new_votes)
    item.update_record(votes=new_votes)
    return str(new_votes)

def unvote():
    pass


@auth.requires_login()
def create():
    form = SQLFORM(db.blog_post,request.args(0), deletable=True).process()
    #form.id.readable=False
    if form.accepted:
        session.flash = "Posted!"
        redirect(URL('index'))
    return locals()
@auth.requires_login()
def show():
    post = db.blog_post(request.args(0, cast=int))
    db.blog_comment.blog_post.default = post.id
    db.blog_comment.blog_post.readable = False
    db.blog_comment.blog_post.writable = False
    form = SQLFORM(db.blog_comment).process()
    pic = db(db.blog_post.id ==post.id).select().first().picture
    comments = db(db.blog_comment.blog_post==post.id).select()
    return locals()


@auth.requires_membership('managers')
def manage():
    grid = SQLFORM.grid(db.blog_post)
    return locals()
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
