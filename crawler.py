import requests
import urllib.request

from bs4 import BeautifulSoup

def crawler(url, page_num, download_path):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    url = url + str(page_num)
    src = requests.get(url= url, headers= headers).text
    soup = BeautifulSoup(src, 'lxml')

    images = []

    img_links = soup.select('img[src^="https://images.freeimages.com/images"]')

    for i in range(len(img_links)):
        images.append(img_links[i]['src'])

    for i in range(len(images)):
        name = download_path + str(page_num) + str(i) + '.jpg'
        urllib.request.urlretrieve(images[i], name) 

if __name__ == '__main__':
    crawler('https://www.freeimages.com/search/dog/', page_num= 2, download_path= 'data/dogs/')