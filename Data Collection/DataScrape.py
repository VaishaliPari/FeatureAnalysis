import pandas as pd 
columns=['Filing Name','Filing Date','Court District','Exchange','Ticker']
data=pd.DataFrame(columns=columns)
data.to_csv("ClassActionLawsuit.csv", header=True, index = False)
for num in range(1, 244):
	url = "http://securities.stanford.edu/filings.html?page="+str(num)+".0"
	data = pd.read_html(url)[0]
	data.to_csv("ClassActionLawsuit.csv", header = False, index = False, mode='a')