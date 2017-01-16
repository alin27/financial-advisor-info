import requests, json

firstname = 'alice'
lastname = 'cooper'

url = 'https://www.moneysmart.gov.au/api/FinancialAdvisor/GetFinancialAdvisors/' + firstname + ' ' + lastname

resp = requests.get(url=url)
data = json.loads(resp.text)

for advisor in data:
	num = advisor['RepresentativeNumber']
	items = advisor['Items'][0]
	address = items['addressField']
	status = items['statusField']
	
	url2 = 'https://www.moneysmart.gov.au/api/FinancialAdvisor/GetFinancialAdvisor/' + num
	resp2 = requests.get(url=url2)
	data2 = json.loads(resp2.text)
	print data2
	print data2['Abn']