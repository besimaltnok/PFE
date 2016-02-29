__author__ = 'besimaltnok'

import urllib


app_list = ['com.trello', 'com.voices', 'com.fjsoft.myphoneexplorer.client', 'com.google.android.apps.adm', 'com.security.client']
url = 'https://play.google.com/store/apps/details?id='
play_app    = []
unknown_app = []

for app in app_list:
    play_url = url+app
    open = urllib.urlopen(play_url)
    code = open.getcode()
    if code == 200:
        print "True"
        play_app.append(app)
    else:
        unknown_app.append(app)

print "Google Play Apps      : ", play_app
print "Unknown source Apps   : ", unknown_app
