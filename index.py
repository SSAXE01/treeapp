import cgi

print('content-type:text/html\r\n\r\n')

form = cgi.FieldStorage()
si_user = str(form.getvalue("si_user"))
si_user_pass = str(form.getvalue("si_user_pass"))
si_mail = str(form.getvalue("si_mail"))
fle=form['filename']

fn=os.path.basename(fle.filename)
open("starting_page.html"+fn, "wb").write(fle.file.read())

print('<html>')
print('<body><center>')
print('<h1>test\n(%s)</h1>'%si_user)
print('<img src=tem/%s></h1>'%fn)
print('<h2>%s</h2>'%si_user_pass)
print('</center></body></html>')
