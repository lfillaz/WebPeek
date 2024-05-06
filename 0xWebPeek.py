import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import random
import time

def main():
    print("\033[94m" + r"""
                                                                     

  ______         _  _  _         _      ______                 _     
 / __   |       | || || |       | |    (_____ \               | |    
| | //| | _   _ | || || |  ____ | | _   _____) )  ____   ____ | |  _ 
| |// | |( \ / )| ||_|| | / _  )| || \ |  ____/  / _  ) / _  )| | / )
|  /__| | ) X ( | |___| |( (/ / | |_) )| |      ( (/ / ( (/ / | |< ( 
 \_____/ (_/ \_) \______| \____)|____/ |_|       \____) \____)|_| \_)
                                                                     
BY @lfillaz v1.0
""" + "\033[0m")
    xin_url = input("Please input the website URL: ")
    print("Choose an action:")
    print("1. Fetch URLs of all images from the website")
    print("2. List all pages on the website")


    xin_option = input("Enter your choice 1 or 2: ")

    if xin_option == "1":
        xin_fetch_image_urls(xin_url)
    elif xin_option == "2":
        xin_list_all_pages(xin_url)
    else:
        print("Invalid choice. Please enter 1 or 2.")

def xin_get_random_user_agent():
    xin_user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    ]
    return random.choice(xin_user_agents)

def xin_fetch_image_urls(xin_url):
    xin_headers = {'User-Agent': xin_get_random_user_agent()}

    try:
        xin_response = requests.get(xin_url, headers=xin_headers)
        xin_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return

    xin_soup = BeautifulSoup(xin_response.content, 'html.parser')

    xin_images = xin_soup.find_all('img', src=True)

    if xin_images:
        print("Images found on the website:")
        for xin_img in xin_images:
            xin_src = xin_img['src']
            xin_absolute_url = urljoin(xin_url, xin_src)
            print("Image URL:", xin_absolute_url)
            time.sleep(2) 
    else:
        print("No images found on the website.")

def xin_list_all_pages(xin_url):
    xin_headers = {'User-Agent': xin_get_random_user_agent()}

    try:
        xin_response = requests.get(xin_url, headers=xin_headers)
        xin_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return

    xin_soup = BeautifulSoup(xin_response.content, 'html.parser')

    xin_links = xin_soup.find_all('a', href=True)

    if xin_links:
        print("All pages found on the website:")
        for xin_link in xin_links:
            xin_href = xin_link['href']
            xin_absolute_url = urljoin(xin_url, xin_href)
            print("Page URL:", xin_absolute_url)
            time.sleep(2)  
    else:
        print("No internal pages found on the website.")

if __name__ == "__main__":
    main()
