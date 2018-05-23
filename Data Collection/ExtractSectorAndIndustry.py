from bs4 import BeautifulSoup
import urllib2
import re
import pandas as pd

def parsetag(url):
	page2=urllib2.urlopen(url)
	page2 = page2.read()
	s= BeautifulSoup(page2,'lxml')
	section=s.find_all('section',{'id':'company'})[0]
	row=section.find_all('div',{'class':'row-fluid'})[0]
	div=row.find_all('div',{'class':'span4'})[0]
	div2=row.find_all('div',{'class':'span4'})[1]
	sector= div.get_text()
	industry= div2.get_text()
	sectortext= sector[(sector.find(':')+1):]
	industrytext=industry[(industry.find(':')+1):]
	return industrytext, sectortext

sector=list()
industry=list()
for num in range(1, 244):
	print num
	pageurl = "http://securities.stanford.edu/filings.html?page="+str(num)+".0"
	page = urllib2.urlopen(pageurl)
	page = page.read()
	soup = BeautifulSoup(page,'lxml')
	rows = soup.findAll('tr')
	for tr in rows:
		val=tr.get('onclick')
		if val is not None:
			start = val.find('id=')+3
			end=val.find("'",start)
			ids=val[start:end]
			url='http://securities.stanford.edu/filings-case.html?id='+ids
			sec,ind= parsetag(url)
			sector.append(sec)
			industry.append(ind)
df=pd.read_csv("ClassActionLawsuit.csv")
df['Sector']=sector
df['Industry']=industry
df.to_csv("LawsuitWithSectorAndIndustry.csv", header = True, index=False)

