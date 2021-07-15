
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies and Setup\n",
    "from bs4 import BeautifulSoup\n",
    "from splinter import Browser\n",
    "import pandas as pd\n",
    "import datetime as dt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from webdriver_manager.chrome import ChromeDriverManager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - ====== WebDriver manager ======\n",
      "[WDM] - Current google-chrome version is 89.0.4389\n",
      "[WDM] - Get LATEST driver version for 89.0.4389\n",
      "[WDM] - Driver [C:\\Users\\sabra\\.wdm\\drivers\\chromedriver\\win32\\89.0.4389.23\\chromedriver.exe] found in cache\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Set Executable Path & Initialize Chrome Browser\n",
    "executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# NASA MARS NEWS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# NASA Mars News Site Web Scraper\n",
    "def mars_news(browser):\n",
    "    # Visit the NASA Mars News Site\n",
    "    url = \"https://mars.nasa.gov/news/\"\n",
    "    browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Get First List Item & Wait Half a Second If Not Immediately Present\n",
    "browser.is_element_present_by_css(\"ul.item_list li.slide\", wait_time=0.5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Parse the data\n",
    "html = browser.html\n",
    "news_soup = BeautifulSoup(html, \"html.parser\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "'return' outside function (<ipython-input-24-1d18b26b49a0>, line 12)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-24-1d18b26b49a0>\"\u001b[1;36m, line \u001b[1;32m12\u001b[0m\n\u001b[1;33m    return None, None\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m 'return' outside function\n"
     ]
    }
   ],
   "source": [
    "# Parse Results HTML with BeautifulSoup\n",
    "\n",
    "try:\n",
    "    slide_element = news_soup.select_one(\"ul.item_list li.slide\")\n",
    "    slide_element.find(\"div\", class_=\"content_title\")\n",
    "\n",
    "    # Scrape the Latest News Title\n",
    "    news_title = slide_element.find(\"div\", class_=\"content_title\").get_text()\n",
    "\n",
    "    news_paragraph = slide_element.find(\"div\", class_=\"article_teaser_body\").get_text()\n",
    "except AttributeError:\n",
    "    return None, None \n",
    "return news_title, news_paragraph"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# JPL SPACE IMAGES"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# NASA JPL (Jet Propulsion Laboratory) Site Web Scraper\n",
    "def featured_image(browser):\n",
    "    # Visit the NASA JPL (Jet Propulsion Laboratory) Site\n",
    "    url = \"https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars\"\n",
    "    browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "ename": "ElementDoesNotExist",
     "evalue": "no elements could be found with id \"full_image\"",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, index)\u001b[0m\n\u001b[0;32m     41\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 42\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_container\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     43\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mIndexError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mElementDoesNotExist\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-13-8ef0714189e1>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#Splinter to go to site and click button with class name full image\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mfull_image_button\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_by_id\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"full_image\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mfull_image_button\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36m__getattr__\u001b[1;34m(self, name)\u001b[0m\n\u001b[0;32m     74\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__getattr__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     75\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 76\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfirst\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     77\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     78\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36mfirst\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m     55\u001b[0m             \u001b[1;33m>>\u001b[0m\u001b[1;33m>\u001b[0m \u001b[1;32massert\u001b[0m \u001b[0melement_list\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m==\u001b[0m \u001b[0melement_list\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfirst\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     56\u001b[0m         \"\"\"\n\u001b[1;32m---> 57\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     58\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     59\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0mproperty\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, index)\u001b[0m\n\u001b[0;32m     42\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_container\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     43\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mIndexError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 44\u001b[1;33m             raise ElementDoesNotExist(\n\u001b[0m\u001b[0;32m     45\u001b[0m                 u'no elements could be found with {0} \"{1}\"'.format(\n\u001b[0;32m     46\u001b[0m                     \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_by\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mquery\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mElementDoesNotExist\u001b[0m: no elements could be found with id \"full_image\""
     ]
    }
   ],
   "source": [
    "#Splinter to go to site and click button with class name full image\n",
    "#<button class=\"full_image\"> Full Image </button>\n",
    "full_image_button = browser.find_by_id(\"full_image\")\n",
    "full_image_button.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\sabra\\anaconda3\\lib\\site-packages\\splinter\\driver\\webdriver\\__init__.py:490: FutureWarning: browser.find_link_by_partial_text is deprecated. Use browser.links.find_by_partial_text instead.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "ename": "ElementDoesNotExist",
     "evalue": "no elements could be found with link by partial text \"more_info\"",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, index)\u001b[0m\n\u001b[0;32m     41\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 42\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_container\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     43\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mIndexError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mElementDoesNotExist\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-25-dd408466a15a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mis_element_present_by_text\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'more info'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mwait_time\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mmore_info_element\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mbrowser\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_link_by_partial_text\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"more_info\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[0mmore_info_element\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36m__getattr__\u001b[1;34m(self, name)\u001b[0m\n\u001b[0;32m     74\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m__getattr__\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     75\u001b[0m         \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 76\u001b[1;33m             \u001b[1;32mreturn\u001b[0m \u001b[0mgetattr\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfirst\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     77\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mAttributeError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     78\u001b[0m             \u001b[1;32mtry\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36mfirst\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m     55\u001b[0m             \u001b[1;33m>>\u001b[0m\u001b[1;33m>\u001b[0m \u001b[1;32massert\u001b[0m \u001b[0melement_list\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m==\u001b[0m \u001b[0melement_list\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfirst\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     56\u001b[0m         \"\"\"\n\u001b[1;32m---> 57\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     58\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     59\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0mproperty\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\splinter\\element_list.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, index)\u001b[0m\n\u001b[0;32m     42\u001b[0m             \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_container\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mindex\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     43\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mIndexError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 44\u001b[1;33m             raise ElementDoesNotExist(\n\u001b[0m\u001b[0;32m     45\u001b[0m                 u'no elements could be found with {0} \"{1}\"'.format(\n\u001b[0;32m     46\u001b[0m                     \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_by\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mquery\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mElementDoesNotExist\u001b[0m: no elements could be found with link by partial text \"more_info\""
     ]
    }
   ],
   "source": [
    "#Find \"More Info\" and be able to click the button \n",
    "browser.is_element_present_by_text('more info',wait_time=1)\n",
    "more_info_element = browser.find_link_by_partial_text(\"more_info\")\n",
    "more_info_element.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "'return' outside function (<ipython-input-27-b16780880f42>, line 9)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-27-b16780880f42>\"\u001b[1;36m, line \u001b[1;32m9\u001b[0m\n\u001b[1;33m    return None\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m 'return' outside function\n"
     ]
    }
   ],
   "source": [
    "#Parse into Beautiful Soup \n",
    "html = browser.html\n",
    "image_soup = BeautifulSoup(html, \"html.parser\")\n",
    "\n",
    "img = image_soup.select_one(\"figure.lede a img\")\n",
    "try:\n",
    "    img_url = img.get(\"src\")\n",
    "except AttributeError:\n",
    "    return None "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'img_url' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-28-127c7975a3b2>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;31m#Base_url\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 2\u001b[1;33m \u001b[0mimg_url\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34mf\"https://www/jpl.nasa.gov{img_url}\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      3\u001b[0m \u001b[1;32mreturn\u001b[0m \u001b[0mimg_url\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'img_url' is not defined"
     ]
    }
   ],
   "source": [
    "#Base_url \n",
    "img_url = f\"https://www/jpl.nasa.gov{img_url}\"\n",
    "return img_url"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Weather"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars Weather Twitter Account Web Scraper\n",
    "def twitter_weather(browser):\n",
    "    # Visit the Mars Weather Twitter Account\n",
    "    url = \"https://twitter.com/marswxreport?lang=en\"\n",
    "    browser.visit(url)\n",
    "    \n",
    "    # Parse Results HTML with BeautifulSoup\n",
    "    html = browser.html\n",
    "    weather_soup = BeautifulSoup(html, \"html.parser\")\n",
    "    \n",
    "    # Find a Tweet with the data-name `Mars Weather`\n",
    "    mars_weather_tweet = weather_soup.find(\"div\", \n",
    "                                       attrs={\n",
    "                                           \"class\": \"tweet\", \n",
    "                                            \"data-name\": \"Mars Weather\"\n",
    "                                        })\n",
    "   # Search Within Tweet for <p> Tag Containing Tweet Text\n",
    "    mars_weather = mars_weather_tweet.find(\"p\", \"tweet-text\").get_text()\n",
    "    return mars_weather"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars Facts Web Scraper\n",
    "def mars_facts():\n",
    "    # Visit the Mars Facts Site Using Pandas to Read\n",
    "    try:\n",
    "        df = pd.read_html(\"https://space-facts.com/mars/\")[0]\n",
    "    except BaseException:\n",
    "        return None\n",
    "    df.columns=[\"Description\", \"Value\"]\n",
    "    df.set_index(\"Description\", inplace=True)\n",
    "\n",
    "    return df.to_html(classes=\"table table-striped\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Mars Hemispheres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Mars Hemispheres Web Scraper\n",
    "def hemisphere(browser):\n",
    "    # Visit the USGS Astrogeology Science Center Site\n",
    "    url = \"https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars\"\n",
    "    browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    " hemisphere_image_urls = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "'return' outside function (<ipython-input-36-c6ea8a742a82>, line 21)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-36-c6ea8a742a82>\"\u001b[1;36m, line \u001b[1;32m21\u001b[0m\n\u001b[1;33m    return hemisphere_image_urls\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m 'return' outside function\n"
     ]
    }
   ],
   "source": [
    "# Get a List of All the Hemisphere\n",
    "links = browser.find_by_css(\"a.product-item h3\")\n",
    "for item in range(len(links)):\n",
    "    hemisphere = {}\n",
    "        \n",
    "    # Find Element on Each Loop to Avoid a Stale Element Exception\n",
    "    browser.find_by_css(\"a.product-item h3\")[item].click()\n",
    "        \n",
    "    # Find Sample Image Anchor Tag & Extract <href>\n",
    "    sample_element = browser.find_link_by_text(\"Sample\").first\n",
    "    hemisphere[\"img_url\"] = sample_element[\"href\"]\n",
    "        \n",
    "    # Get Hemisphere Title\n",
    "    hemisphere[\"title\"] = browser.find_by_css(\"h2.title\").text\n",
    "        \n",
    "    # Append Hemisphere Object to List\n",
    "    hemisphere_image_urls.append(hemisphere)\n",
    "        \n",
    "     # Navigate Backwards\n",
    "    browser.back()\n",
    "return hemisphere_image_urls"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Helper Function\n",
    "def scrape_hemisphere(html_text):\n",
    "    hemisphere_soup = BeautifulSoup(html_text, \"html.parser\")\n",
    "    try: \n",
    "        title_element = hemisphere_soup.find(\"h2\", class_=\"title\").get_text()\n",
    "        sample_element = hemisphere_soup.find(\"a\", text=\"Sample\").get(\"href\")\n",
    "    except AttributeError:\n",
    "        title_element = None\n",
    "        sample_element = None \n",
    "    hemisphere = {\n",
    "        \"title\": title_element,\n",
    "        \"img_url\": sample_element\n",
    "    }\n",
    "    return hemisphere"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Web Scraping "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - ====== WebDriver manager ======\n",
      "[WDM] - Current google-chrome version is 89.0.4389\n",
      "[WDM] - Get LATEST driver version for 89.0.4389\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[WDM] - Driver [C:\\Users\\sabra\\.wdm\\drivers\\chromedriver\\win32\\89.0.4389.23\\chromedriver.exe] found in cache\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "cannot unpack non-iterable NoneType object",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-39-8450d3304b3b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     22\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     23\u001b[0m \u001b[1;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;34m\"__main__\"\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 24\u001b[1;33m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mscrape_all\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32m<ipython-input-39-8450d3304b3b>\u001b[0m in \u001b[0;36mscrape_all\u001b[1;34m()\u001b[0m\n\u001b[0;32m      2\u001b[0m     \u001b[0mexecutable_path\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;34m'executable_path'\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mChromeDriverManager\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0minstall\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m     \u001b[0mbrowser\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mBrowser\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"chrome\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m**\u001b[0m\u001b[0mexecutable_path\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mheadless\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mFalse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m     \u001b[0mnews_title\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mnews_paragraph\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mmars_news\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbrowser\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m     \u001b[0mimg_url\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mfeatured_image\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbrowser\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m     \u001b[0mmars_weather\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mtwitter_weather\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mbrowser\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: cannot unpack non-iterable NoneType object"
     ]
    }
   ],
   "source": [
    "def scrape_all():\n",
    "    executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    "    browser = Browser(\"chrome\", **executable_path, headless=False)\n",
    "    news_title, news_paragraph = mars_news(browser)\n",
    "    img_url = featured_image(browser)\n",
    "    mars_weather = twitter_weather(browser)\n",
    "    facts = mars_facts()\n",
    "    hemisphere_image_urls = hemisphere(browser)\n",
    "    timestamp = dt.datetime.now()\n",
    "\n",
    "    data = {\n",
    "        \"news_title\": news_title,\n",
    "        \"news_paragraph\": news_paragraph,\n",
    "        \"featured_image\": img_url,\n",
    "        \"weather\": mars_weather,\n",
    "        \"facts\": facts,\n",
    "        \"hemispheres\": hemisphere_image_urls,\n",
    "        \"last_modified\": timestamp\n",
    "    }\n",
    "    browser.quit()\n",
    "    return data \n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    print(scrape_all())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}