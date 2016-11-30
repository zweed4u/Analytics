import requests, BeautifulSoup
session=requests.session()
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}
styleCode='B39254'#'BB1826'
r=session.get('http://www.ebay.com/sch/i.html?_nkw='+str(styleCode)+'&LH_Complete=1&LH_Sold=1',headers=headers)
soup=BeautifulSoup.BeautifulSoup(r.content)
try:
    #more than 48 listings - grid view
    for cardListing in soup.find("ul", {"id": "GalleryViewInner"}).findAll('li'):
        #parse element for title and sold price and when
        #store all prices in array for maths - min, max, mean, volatility    
        print cardListing.find('h3').text
        st=cardListing.findAll("div", {"class":"gvprices"})[0].text.split('$')[1]
        price=st[:st.index('.')+3]
        type=st[st.index('.')+3:]
        print price, type
        print
except:
    #error with findAll - less than 48 items?
    for cardListing in soup.find("ul", {"id":"ListViewInner"}).findAll('li',recursive=False):
        #parse element for title and sold price and when
        #store all prices in array for maths - min, max, mean, volatility    
        print cardListing.find('h3').text
        st=cardListing.findAll("li", {"class":"lvprice prc"})[0].text.split('$')[1]
        price=st[:st.index('.')+3]
        type=cardListing.findAll("li", {"class":"lvformat"})[0].text
        print price, type
        print
        
