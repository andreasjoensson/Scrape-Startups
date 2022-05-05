from bs4 import BeautifulSoup
import requests
import csv

def scrapeCompanies():
 f = open('companies.csv', 'a',newline='', encoding='utf-8')
 writer = csv.writer(f)
 for x in range(1, 1829):
  page = requests.get("https://www.eu-startups.com/directory/page/" + str(x) +"/")
  soup = BeautifulSoup(page.content, 'html.parser')
  print("DEN HER SIDE:",x)

  for a in soup.select('#wpbdp-listings-list'):
     title = a.select('.listing-title > a')
     for text in title:
      link = text['href']
      companyPage = requests.get(link)
      companySoup = BeautifulSoup(companyPage.content, 'html.parser')
      hasDescription = companySoup.select_one('.wpbdp-field-business_description > .value')
      if hasDescription != None:
       hasLongDescription = companySoup.select_one('.wpbdp-field-long_business_description > .value')
       if hasLongDescription != None:
        businessDescription = companySoup.select_one('.wpbdp-field-long_business_description > .value').text
        cleanText = businessDescription.replace("\n","").strip()
        industrys = companySoup.select_one('.wpbdp-field-tags > .value')
        if industrys != None:
         industrys = companySoup.select_one('.wpbdp-field-tags > .value').text.replace("\n","").strip().split(",")
         print(cleanText)
         print(industrys)
         writer.writerow([cleanText,industrys])
       else: 
        businessDescription = companySoup.select_one('.wpbdp-field-business_description > .value').text
        cleanText = businessDescription.replace("\n","").strip()
        industrys = companySoup.select_one('.wpbdp-field-tags > .value')
        if industrys != None:
         industrys = companySoup.select_one('.wpbdp-field-tags > .value').text.replace("\n","").strip().split(",")
         print(cleanText)
         print(industrys)
         writer.writerow([cleanText,industrys])
      else:
       print("IKKE NOGET HER")

 f.close()


scrapeCompanies()


    


