import requests
from bs4 import BeautifulSoup
import tweepy # Library Used For twitter

auth = tweepy.OAuthHandler('NZIjCl060lClQIcGIvQZY7Er5','FFafAZfS4PuCIBajvzmTQLU2jW140DeQsDBxhnWneEUk82TvOQ') # this is one of the tokens and secret keys to initialize the API

auth.set_access_token('905298941830418432-kqrO4GcUWlSUt3M50mnVYadYrPuemAD','rztBW3cTEcudo3wK5lGDxzjjTarHRwJa5YCrcAMvA8nxn') # this is one of the tokens and secret keys to initialize the API

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


URL = 'https://www.google.com/search?q=weather+in+mumbai&rlz=1C1CHBF_enIN868IN868&oq=weather+&aqs=chrome.0.69i59j69i57j69i60l3.1072j0j7&sourceid=chrome&ie=UTF-8'
headers = {"User_Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}



page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
    
temp = soup.find(id= "wob_tm").get_text() # this accesses the website where the data is, and finds the correct ID for the current temperature

login= api.me()
api.update_status(temp) # this tweets out the temperature in Mumbai at any given time





