

from bs4 import BeautifulSoup
import requests
import pymongo
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, render_template
from flask_pymongo import PyMongo

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database and collection
db = client.mars_db
collection = db.items

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = "https://mars.nasa.gov/news/"

browser.visit(url)

html = browser.html

soup = BeautifulSoup(html, "html.parser")

broad_titles = soup.select_one("div.list_text")
news_title = broad_titles.find("div", class_="content_title").text.strip()
news_title
news_p = broad_titles.find("div", class_="article_teaser_body").text.strip()
news_p

jpl_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
browser.visit(jpl_url)

featured_image = soup2.find_all("img")[1]["src"]
featured_image

jpl_site_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/"

featured_image_url = jpl_site_url + featured_image
featured_image_url

facts_url = "https://space-facts.com/mars/"

tables = pd.read_html(facts_url)
tables

df = tables[0]
df

tables[1]

mars_facts = tables[2]
mars_facts

mars_facts.columns=["Characteristic", "Value"]
mars_facts

html_table_mars = mars_facts.to_html()
html_table_mars

html_table_mars = html_table_mars.replace('\n', '')
html_table_mars

main_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


browser.visit(main_url)

hemi_views = browser.find_by_css('div.description a.itemLink.product-item')
hemi_views

hemisphere_image_urls = []

for i in range(len(hemi_views)):
    hemi_image_dict = {}

    browser.find_by_css('div.description a.itemLink.product-item')[i].click()
    
    hemi_image_dict["title"] = browser.find_by_css('h2.title').text
    sample = browser.find_by_text("Sample")
    sample.click()
    hemi_image_dict["img_url"] = sample["href"]

    hemisphere_image_urls.append(hemi_image_dict)
    browser.back()
    
hemisphere_image_urls

browser.quit()
