__author__ = 'besimaltnok'
__author__ = 'octosec'

#Downloader 1
import wget
wget.download("http://img.prntscr.com/img?url=http://i.imgur.com/YZNV4tI.png", 'deneme.png')

#Downloader 2 
import urllib2

url = "http://img.prntscr.com/img?url=http://i.imgur.com/zJyGz19.png"
file_name = url.split('/')[-1]
file = urllib2.urlopen(url)
download = open(file_name,'wb')
download.write(file.read())
download.close()
