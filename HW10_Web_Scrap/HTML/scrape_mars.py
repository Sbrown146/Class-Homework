# Scrape_mars.py Scott Brown

# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

# Declare blank dictionary
mars_data={}

# Set browser path
executable_path = {"executable_path": "chromedriver.exe"}
browser=Browser("chrome", **executable_path, headless=False)


# News function.  Only thing added not in jupyter is that the new_title and news_paragraph variables are added to the global mars_data dictionary.  This is the same for all the functions in this python file.

def Mars_News():
    
    url="https://mars.nasa.gov/news/"
    browser.visit(url)
    html=browser.html
    soup=BeautifulSoup(html, "lxml")
    article=soup.find("div", class_='list_text')
    news_title=article.find("div", class_="content_title").text
    news_paragraph=article.find("div", class_ ="article_teaser_body").text
    mars_data['News_Title']=news_title
    mars_data['News_Paragraph']=news_paragraph
    return mars_data
    


def Mars_Image():
    
    featured_image_url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(featured_image_url)
    html=browser.html
    soup=BeautifulSoup(html, "lxml")
    image=soup.find("img", class_="thumb")["src"]
    featured_image_url=featured_image_url[0:-35]
    featured_image_url=featured_image_url+image
    mars_data["Featured_Image_URL"]=featured_image_url
    return mars_data


def Mars_Weather():

    mars_weather_url="https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_weather_url)
    mars_weather_html=browser.html
    soup=BeautifulSoup(mars_weather_html, 'lxml')

    weather_tweet=soup.find("div", class_="js-tweet-text-container").text
    #This works for any standard weather tweet
#     weather_tweet_strip=weather_tweet[9:-27]

#   This is the format for the tweet on 8/27 about no further updates for 2 weeks.  It is not in the same format as the standard weather tweets.
    weather_tweet_strip=weather_tweet[:-27]
    mars_weather=weather_tweet_strip
    mars_data["Latest_Weather_Tweet"]=mars_weather
    return mars_data


def Mars_Facts():

    mars_facts_df=pd.read_html("https://space-facts.com/mars/")
    mars_facts_df=mars_facts_df[1]
    mars_facts_df=mars_facts_df.rename(columns={0: "Description", 1: "Value"})
    mars_facts_df=mars_facts_df.set_index("Description")
    mars_facts_df_html=mars_facts_df.to_html()
    mars_data["Mars_Facts"]=mars_facts_df_html
    return mars_data


def Mars_Hem():
    Mars_hemispheres_images_url=[]

    Mars_hems_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Strip the useless information from the url
    Default_url=Mars_hems_url[:29]

    browser.visit(Mars_hems_url)
    Mars_hems_html=browser.html
    soup=BeautifulSoup(Mars_hems_html, 'lxml')

    # First branch
    Hem_url=soup.find_all("div", class_="item")


    for hemispheres in Hem_url:
    
        # Get the headline
        Headline_url=hemispheres.find('h3').text
        Headline_url=Headline_url[:-9]
    
        # Link to the individual hemisphere page
        Pic_home_url=hemispheres.find("a")["href"]
    
        browser.visit(Default_url+Pic_home_url)
    
        Pic_home_html=browser.html
    
        soup=BeautifulSoup(Pic_home_html, 'lxml')
    
        # Path to image within the hemisphere page
        Pic_html=soup.find("img", class_="wide-image")["src"]
    
        # Add to the default url
        Destination_url=Default_url + Pic_html
    
        # Create dictionary
        Mars_hemispheres_images_url.append({  \
                "Title": Headline_url, "Image_Url": Destination_url
        }
        )


        mars_data["Hemisphere_URLs"]=Mars_hemispheres_images_url

    return mars_data
