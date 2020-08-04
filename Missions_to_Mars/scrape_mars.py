# import dependencies

import requests
import pymongo
import pandas as pd

from splinter import Browser
from bs4 import BeautifulSoup
import time
import re


# open chrome driver browser
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)

#NASA Mars News - Collect Most Recent Title and Paragraph Text

def scrape():
    browser = init_browser()
    
    # define url
    mars_news_url = "https://mars.nasa.gov/news/"
    browser.visit(mars_news_url)

    # create beautiful soup object 
    html = browser.html
    mars_news_soup = BeautifulSoup(html, 'html.parser')

    # find latest news title
    news_title = mars_news_soup.body.find("div", class_="content_title").text

    # find the paragraph associated with the latest title
    news_paragraph = mars_news_soup.body.find("div", class_="article_teaser_body").text
            
    #JPL Mars Space Images

    # define the url and visit it with browser
    time.sleep(5)
    
    mars_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(mars_image_url)

    # click on the Full Image button.
    browser.click_link_by_id('full_image')

    # click on the more info button to get to the large image
    browser.click_link_by_partial_text('more info')

    # create the soup item
    image_html = browser.html
    soup = BeautifulSoup(image_html, 'html.parser')

    # the large image is within the figue element with class = lede
    image = soup.body.find("figure", class_="lede")

    # the url is within the a element, so search for a element and then extract the url
    link = image.find('a')
    href = link['href']

    # define the beginning of the url as the returned href doesn't included it
    base_url='https://www.jpl.nasa.gov'

    # create the full url
    featured_image_url = base_url + href
    featured_image_url

    #Mars Weather
    # open url in browser
    time.sleep(5)
    mars_weather_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_weather_url)

    #create a soup item
    html = browser.html
    mars_weather_soup = BeautifulSoup(html, 'html.parser')

    #find the tweet text  
    mars_weather = ''
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(5)
    browser.reload()
    time.sleep(5)
    html = browser.html
    time.sleep(5)
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(5)
    results = soup.find('div', class_= 'css-1dbjc4n').find_all('span', class_ ="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
    found = False
    for result in results:
        if (bool(result.find(string=re.compile("InSight"))) & (not found)):
            mars_weather = result.find(string=re.compile("InSight"))
            print(mars_weather)
            found = True
    print(mars_weather)



    # ## Mars Facts
    time.sleep(5)
    
    # define url
    mars_facts_url = "https://space-facts.com/mars/"

    #getting table into pandas
    mars_tables = pd.read_html(mars_facts_url)

    #first table has what we need
    mars_facts = mars_tables[0]
    mars_facts.columns = ["Description", "Value"]

    # convert to html table
    mars_facts_html=mars_facts.to_html()
    mars_facts_html

    #Mars Hemispheres
    #Cerberus Hemisphere
    #Define url and open

    time.sleep(5)

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(mars_hemispheres_url)

    # click on the link for the Cerberus
    browser.click_link_by_partial_text('Cerberus')

    # click on the open button to get to enhanced picture
    browser.click_link_by_partial_text('Open')

    # create a soup item
    hemispheres_html = browser.html
    cerberus_soup = BeautifulSoup(hemispheres_html, 'html.parser')

    cerberus = cerberus_soup.body.find('img', class_ = 'wide-image')
    cerberus_img = cerberus['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    cerberus_url = hem_base_url + cerberus_img

    #Schiaparelli Hemisphere
    #Define url and open
    time.sleep(5)

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemispheres_url)

    #Click on the link for Schiaparelli
    browser.click_link_by_partial_text('Schiaparelli')

    #Click on the open button to get to enhanced picture
    browser.click_link_by_partial_text('Open')

    #create a soup item
    hemispheres_html = browser.html
    schiaparelli_soup = BeautifulSoup(hemispheres_html, 'html.parser')

    schiaparelli = schiaparelli_soup.body.find('img', class_ = 'wide-image')
    schiaparelli_img = schiaparelli['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    schiaparelli_url = hem_base_url + schiaparelli_img

    #Syrtis hemisphere
    # define url and open
    time.sleep(5)

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemispheres_url)

    #Click on the link for Syrtis
    browser.click_link_by_partial_text('Syrtis')

    #click on the link for the Cerberus hemisphere
    browser.click_link_by_partial_text('Open')

    #create a soup item
    hemispheres_html = browser.html
    syrtis_soup = BeautifulSoup(hemispheres_html, 'html.parser')

    syrtis = syrtis_soup.body.find('img', class_ = 'wide-image')
    syrtis_img = syrtis['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    syrtis_url = hem_base_url + syrtis_img
   
    #Valles hemisphere
    # define url and open
    time.sleep(5)

    mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemispheres_url)

    #click on the link for the Valles hemisphere
    browser.click_link_by_partial_text('Valles')

    #click on the link for the Valles hemisphere
    browser.click_link_by_partial_text('Open')

    # create a soup item
    hemispheres_html = browser.html
    valles_soup = BeautifulSoup(valles_html, 'html.parser')

    valles = valles_soup.body.find('img', class_ = 'wide-image')
    valles_img = valles['src']

    hem_base_url = 'https://astrogeology.usgs.gov'
    valles_url = hem_base_url + valles_img
    # print(valles_url)


    #Define list of dictionaries that include each hemisphere

    hemispheres_image_urls = [
        {"title": "Cerberus Hemisphere", "img_url": cerberus_url},
        {"title": "Schiaparelli Marineris Hemisphere", "img_url": schiaparelli_url},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_url},
        {"title": "Valles Marineris Hemisphere", "img_url": valles_url},

    ]
    
    mars_data = {
       "news_title": news_title,
       "news_p": news_p,
       "featured_image_url": featured_image_url,
       "mars_weather": mars_weather,
       "mars_facts": mars_facts,
       "hemisphere_image_urls": hemisphere_image_urls
    }


    browser.quit()
    return mars_data