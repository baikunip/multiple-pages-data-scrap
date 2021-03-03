# import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options #Use your own web browser
from user_agent import generate_user_agent, generate_navigator
import json

DRIVERPATH ="your browser driver path"
options = Options()
driver=webdriver.Chrome(DRIVERPATH)
iPage=1 
linkArray=[]
geoJson={
  "type": "FeatureCollection",
  "features": [
#     The JSON Object Structure
#     {
#       "type": "Feature",
#       "properties": {
#         "Luas": 5000,
#         "Harga": 300000000
#       },
#       "geometry": {
#         "type": "Point",
#         "coordinates": [
#           101.45132308825778,
#           0.6859889286088628
#         ]
#       }
#     }
  ]
}
while iPage < 8:
    options.add_argument(f'user-agent={generate_user_agent()}')
    driver.get("the page path that contain list of pages to scrap"+str(iPage)) # The 'iPage' can be customized according to how the pattern of the web page's link
    xPathLink ='The xpath of corresponded data' # used to find the links
    scrapingLink = driver.find_elements_by_xpath(xPathLink)
    iPage +=1 
    i=1
#     while loop through the list of xpath contain the link of pages
    while i < len(scrapingLink)+1:
        try:
            dataLink = driver.find_element_by_xpath(xPathLink+str([i])+"/div/div[2]/div[1]/h2/a")
            linkArray.append(dataLink.get_attribute('href'))
        except:
            dataLink = None
        i +=1
#         For looping through the list of scraped link
for link1 in linkArray:
    driver.get(str(link1))
    time.sleep(10)
    dataLayer=driver.execute_script("return dataLayer;") #Get corresponded container; In my case, they are in a JSON named 'dataLayer'
    y= {
      "type": "Feature",
      "properties": {
        "Luas": dataLayer[0]['attributes']['land_size'], #Get the data
        "Harga": dataLayer[0]['attributes']['price']
      },
      "geometry": {
        "type": "Point",
        "coordinates": [
          dataLayer[0]['attributes']['location_longitude'],
          dataLayer[0]['attributes']['location_latitude']
        ]
      }
    }
    geoJson['features'].append(y)

driver.quit()
print(geoJson)



