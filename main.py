#create a NYT api call to scrap every year and all its months into individual txt files so that I can do a sentiment analysis month by month


#imports request function
import requests
#gets the datetime so I can get the current year
import datetime

import time

API_KEY =


def files_and_count():
  #NYT data goes back to the year 1850

  today = datetime.date.today()
  year = today.year

  for i in range(1850, year):

    for months in range(1,13):
      
      query = str(year) + "/"+ str(months)
      real_file_name = str(year) + "_"+ str(months)
      file_name = str('txt_folder/'+ real_file_name +'.txt')
      file = open(file_name, 'w')
      
      search(query,API_KEY,file)




#Function that takes the API query and writes them into a file
def search(query,API_KEY,file):
  #here is the url with the query and API key as values so it is more flexible
  url = f'https://api.nytimes.com/svc/archive/v1/{query}.json?api-key={API_KEY}'
  
  print(url)

  #time between each API call
  time.sleep(12)
  
  try:
    #request the url
    response = requests.get(url)
  
    #find the JSON content
    content = response.json()
  
    #for loop to go through the text the request pulled from NYT
    for item in  content["response"]["docs"]:
      #searches in the JSON for the titles of the articles
      text = item["headline"]["main"]
      #for every article title there is a newline character added to the end of it so that each title is on a new line
      file.write(text+"\n")
      
  except ValueError:
    print('Could not pull content from/connect to API')
  




files_and_count()
