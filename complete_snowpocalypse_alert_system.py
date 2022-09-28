#! run pip install bs4
from bs4 import BeautifulSoup
from requests import get
#class="DetailsSummary--extendedData--365A_"
url = "https://weather.com/weather/tenday/l/6c2f27113f565a4d8c589053380697549d56e3f0af8e0a434f1f7745c2271e28b5a767c26b97488355db0ef21e870015"

response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')
ten_day_forecast = soup.find_all(class_ = "DetailsSummary--extendedData--365A_")
for item in ten_day_forecast:
    print(item.text)