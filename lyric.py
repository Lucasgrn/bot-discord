from bs4 import BeautifulSoup
import requests
import json
  
def getUrl(term):
  response = requests.get(f'https://cse.google.com/cse/element/v1?rsz=filtered_cse&num=10&hl=pt-PT&source=gcsc&cselibv=8fa85d58e016b414&cx=000985329112107235723%3Aorkf-eprrfa&q={term}&safe=off&cse_tok=AB-tC_7x8n6yNiduvNlxi_2_WABI%3A1733166715196&sort=&exp=cc%2Capo&oq={term}&gs_l=partner-generic.3...105618.110187.1.110381.19.19.0.0.0.0.192.1704.12j6.18.0.csems%2Cnrl%3D10...0....1.34.partner-generic..13.6.537.wTCPP8DU7Fc&cseclient=hosted-page-client&callback=google.search.cse.api11563&rurl=https%3A%2F%2Fcse.google.com%2Fcse%3Foe%3Dutf8%26ie%3Dutf8%26source%3Duds%26q%3Dend%2520this%2520way%25205fdp%26safe%3Doff%26sort%3D%26cx%3D000985329112107235723%3Aorkf-eprrfa%26start%3D0')      
  data_string = response.text[35:-2]
  data = json.loads(data_string)
  url = ''
  if 'tradução' in data['results'][0]['title']:
    url = data["results"][1]["unescapedUrl"]
  else:
    url = data["results"][0]["unescapedUrl"]
  print(url)
  return url
#.gs-title .gs-title tentar dps
def getLyrics(term):
  url = getUrl(term)
  response = requests.get(url)
  if response.status_code == 200:
    response.encoding = "utf-8"
    content = BeautifulSoup(response.text, "html.parser")
    element = content.select_one('#lyrics')
    raw_lyric = element.get_text(separator="<br/>")
    verses = raw_lyric.split('<br/>')

    lyric = []
    for verse in verses:
      lyric.append(verse)

    return lyric
  else:
    error = 'Não foi possível acessar a letra!'
    return error