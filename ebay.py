import requests, BeautifulSoup
session=requests.session()
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
styleCode='bb1826'
r=session.get('http://www.ebay.com/sch/i.html?_nkw='+str(styleCode)+'&LH_Complete=1&LH_Sold=1',headers=headers)
soup=BeautifulSoup.BeautifulSoup(r.content)
for cardListing in soup.find("ul", {"id": "GalleryViewInner"}).findAll('li'):
    #parse element for title and sold price and when
    #store all prices in array for maths - min, max, mean, volatility    
    print cardListing
    print
    
