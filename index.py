import cgi,os


form = cgi.FieldStorage()
si_user = str(form.getvalue("si_user"))
si_user_pass = str(form.getvalue("si_user_pass"))
si_mail = str(form.getvalue("si_mail"))
fle=form['filename']

print(si_user)
