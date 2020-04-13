from bs4 import BeautifulSoup as bs
import requests
import csv

csv_file = open('Output.csv','w',newline = '')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Business Name','Link','Conatact Name','Job Title','E-mail','Phone Number','Address'])

##url=input()
ps=[]
ls=[]
for i in range(1,38):
    ps+=["https://www.ccab.com/main/ccab_member/page/" + str(i)]


for j in ps:
    req = requests.get(j)
    sooup = bs(req.content,'lxml')
    for j in sooup.findAll('div', class_='article'):
        ls+=[j.a['href']]
        print(ls)

print(ls)

for k in ls:
	r = requests.get(k)
	soup = bs(r.content,'lxml')
	bus_name = soup.find('div',id='PageTitle').text
	try:
	    link = soup.find('div',class_='webSite').a.text
	except:
	    link = None

	contact_info = soup.findAll('span',class_='content')
	try:
		contact_name = contact_info[0].text
	except:
		contact_name = None

	try:
		job_title = contact_info[1].text
	except:
		job_title = None

	try:
		email = contact_info[2].text
	except:
		email = None

	try:
		p_no = contact_info[3].text
	except:
		p_no = None

	try:
		if(soup.find('h2',class_='MembershipText').find_next().text == 'Billing Address'):
			for i in range(0,len(soup.findAll('p'))):
				if(soup.findAll('p')[i].text=='Billing Address'):
					address=' '.join(soup.findAll('p')[i+1].text.split('\n'))
				else:
					pass
		else:
			address = ' '.join(soup.find('h2',class_='MembershipText').find_next().text.split('\n')[1:])

	except:
	    address = None
	print([bus_name,link,contact_name,job_title,email,p_no,address])
	csv_writer.writerow([bus_name,link,contact_name,job_title,email,p_no,address])
csv_file.close()
