
"""
Sources:
-------------------------------------------


div.css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0
div.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0
div.css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0 


div.css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0
div.css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0
          









"""













import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import bs4
import textblob
import re

def clean_tweet(tweet): 
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def sentiment(statement):
	x = textblob.TextBlob(str(statement))
	l = x.sentiment.polarity
	if l==0:
		return "Neutral"
	elif l>0:
		return "Positive"
	elif l<0:
		return "Negative"



browser = webdriver.Chrome() 

base_url = 'https://twitter.com/search?q='
query = input("query: ")
url = base_url + query 


browser.get(url) 
time.sleep(3) 

body = browser.find_element_by_tag_name('body')
 
for _ in range(100): 
    #body.send_keys(Keys.PAGE_DOWN) 
    #time.sleep(0.1) 
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.2)
time.sleep(10)

#THIS WORKS VERY WELL DO NOT DELETE#tweets = browser.find_elements_by_css_selector('div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1ny4l3l.r-1udh08x.r-1yt7n81.r-ry3cjt')
#THIS WORKS VERY WELL DO NOT DELETE#
tweets = browser.find_elements_by_css_selector('div.css-901oao.r-hkyrab.r-1qd0xha.r-a023e6.r-16dba41.r-ad9z0x.r-bcqeeo.r-bnwqim.r-qvutc0')
replies = browser.find_elements_by_css_selector('div.css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0')

mytweets = []
for tweet in tweets:
    try:
        mytweets.append(tweet.text)
    except:
        continue

for reply in replies:
    try:
        mytweets.append(reply.text)
    except:
        continue



score = []
for i in mytweets:
    print("\n"+clean_tweet(i)+"\n"+sentiment(clean_tweet(i)))
    score.append(sentiment(clean_tweet(i)))

print("\n\nSummary")
print("="*12)
print("Got "+str(len(mytweets))+" Tweets\n")
print("Positive: "+str(int(score.count("Positive")/len(mytweets)*100)))
print("Negative: "+str(int(score.count("Negative")/len(mytweets)*100)))
print("Neutral: "+str(int(score.count("Neutral")/len(mytweets)*100)))
print("="*12)

browser.quit()
