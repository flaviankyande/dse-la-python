# installing packages
# --------------------
# pip install bs4
# pip install selenium

# importing packages and modules
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re, os, time, wget

# url input
url_link = input('Enter your instagram media link: ')

# url regex
reel_link = bool(re.search('https://www.instagram.com/reel/', url_link))
img_link = bool(re.search('https://www.instagram.com/p/', url_link))
vid_link = bool(re.search('https://www.instagram.com/tv/', url_link))

# check if url is correct
if reel_link or img_link or vid_link == True:
    print('Great, this is an IG media link')
    time.sleep(2)
    print('Processing your media...')

    # login manually to save session and prevent further log ins in future
    options = Options()
    options.add_argument("--user-data-dir=specify the path to an empty folder here")
    options.page_load_strategy = 'normal'

    # assign web driver
    driver = webdriver.Chrome(executable_path="specify the path to your driver here", chrome_options=options)

    # run link on web driver
    driver.get(url_link)
    time.sleep(2)

    #parse link html
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    images = soup.find_all('img')
    videos = soup.find_all('video')
    
    
    # save media to project folder
    path = os.getcwd()
    path = os.path.join(path, time.localtime)
    os.mkdir(path)
    path
    for image in images:
        image_link = image.get('src')
        save_img = os.path.join(path, time.localtime + 'jpg')
        wget.download(image, save_img)

    for video in videos:
        video_link = video.get('src')
        save_vid = os.path.join(path, time.localtime + 'mp4')
        wget.download(video, save_vid)



else:
    print('Please enter a valid link!')
