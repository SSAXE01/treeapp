import cgi,os

print('content-type:text/html\r\n\r\n')

form = cgi.FieldStorage()
si_user = str(form.getvalue("si_user"))
si_user_pass = str(form.getvalue("si_user_pass"))
si_mail = str(form.getvalue("si_mail"))
fle=form['filename']

open("C:/Users/ranja/OneDrive/Desktop/MyApp/starting_page.html")
