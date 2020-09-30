import requests
from django.shortcuts import render

# Create your views here.
def get_html_content(city):
    import requests
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    city = city.replace(' ','+')
    html_content = session.get(f'https://www.google.com/search?q=clima+en+{city}').text
    return html_content

def clima(request):
    clima_data = None
    if 'city' in request.GET:
        # buscar datos meteorológicos
        city = request.GET.get('city')
        html_content = get_html_content(city)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        clima_data = dict()
        clima_data['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
        clima_data['daytime'] = soup.find("div", attrs={"id": "wob_dts"}).text
        clima_data['status'] = soup.find("span", attrs={"id": "wob_dc"}).text
        clima_data['pbrain'] = soup.find("span", attrs={"id": "wob_pp"}).text
        clima_data['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text
        clima_data['temp'] = soup.find("span", attrs={"id": "wob_tm"}).text
        clima_data['relhum'] = soup.find("span", attrs={"id": "wob_hm"}).text
    return render(request, 'aplicaciones.html', {'clima': clima_data})
