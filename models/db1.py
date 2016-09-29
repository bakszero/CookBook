# -*- coding: utf-8 -*-


db.define_table('blog_post',
                Field('title', requires= IS_NOT_EMPTY()),
                Field('description', requires=IS_NOT_EMPTY()),
                Field('ingredients', requires=IS_NOT_EMPTY()),
                Field('body', 'text',requires= IS_NOT_EMPTY()),
                Field('picture', 'upload'),
                Field('votes','integer',default=0),
                Field('email',requires=IS_EMAIL()),
                #Field('time_stamp', 'datetime'),
                auth.signature
                #Field('created_by','reference auth_user'),
                #Field('modified_by','reference auth_user'),
                #Field('modified_on','datetime')
               )
db.define_table('blog_comment',
                Field('blog_post', 'reference blog_post'),
                Field('Comments','text',requires=IS_NOT_EMPTY()),
                auth.signature
                )
db.define_table('likes',
                Field('username', 'reference auth_user'),
                Field('blog_post', 'reference blog_post'),
                Field('unique_key', unique=True, notnull=True),
)
db.likes.unique_key.compute = lambda row: "%(username)s-%(blog_post)s" % row
db.blog_post.votes.readable=False
db.blog_post.votes.writable=False
db.blog_post.votes.readable=False
db.blog_post.email.readable=False
db.blog_post.email.writable=False
if "login" not in request.args:
    auth.settings.table_user.password.requires.insert(0, IS_STRONG(min=8, special=1))
