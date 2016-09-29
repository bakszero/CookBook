# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('Cookbook'),XML(' &nbsp;'),
                  _class="navbar-brand",_href="/Cookbook/default/index",
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('All Posts'), False, URL('default', 'index'), []),
    (T('Create'), False, URL('default','create')),
    (T('My Recipes'),False,URL('default','post')),
    (T('Manage'),False,URL('default','manage'))
]

#if auth.has_membership('managers'):
 #   response.menu.append( (T('Manage'),False, URL('default','manage')))


if "auth" in locals(): auth.wikimenu()
