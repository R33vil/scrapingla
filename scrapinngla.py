from requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=33.77078000000006&lon=-118.18930999999998'
soup = BeautifulSoup(page.content 'html.parser')
weeks = soup.find(id='seven-day-forcast')


items = weeks.find_all(class_='tombstone-container')
print(items)
           