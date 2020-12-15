from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://kellogg.campusgroups.com/club_signup?group_type=275&_ga=2.140050935.53865912.1607220126-183222809.1595038809'
uClient = uReq(my_url)
page_html=uClient.read()
uClient.close()

#Module Beautiful Soup parses our html url.
page_soup = soup(page_html, "html.parser")

#Grabs each CLUB listing
listings=page_soup.findAll("div",{"listing-element__title-block col-xxs-9_5 col-xs-19 col-sm-10_5 col-md-5_5"})
person = page_soup.findAll("p", {"style": "margin-top:10px"})

#File name creation
filename = "NW_groups.csv"
f = open(filename, "w")
#naming the header
header = "Organization, Website, Contact_name, School\n"

f.write(header)

for list in listings:
    org_name = list.div.a.img['alt']
    website = list.div.a['href'].strip()
    try:
        contact_name = list.find("p", {"style": "margin-top:10px"}).a.text
    except:
        contact_name = "NA"
    school = 'www.northwestern.edu'
    print("orgname: " + org_name)
    print("website: " + website)
    print("contact_name: " + contact_name)
    print("school: " + school)
    f.write(org_name + "," + website + "," + contact_name + "," + school + "\n")
f.close()
