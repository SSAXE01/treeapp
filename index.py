import requests

url = 'https://treeapp102.herokuapp.com'
credinitals = {"si_user": "Saxena",
               "si_user_pass": "Sharvil",
               "si_mail": "sharvil@gmail.com"}
r = requests.get(url, auth=credinitals)
open('dashboard_ui.html')
