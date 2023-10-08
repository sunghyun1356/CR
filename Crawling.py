import os
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from urllib.request import urlretrieve
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

# 크롬 드라이버 초기화
script_directory = os.path.dirname(os.path.abspath(__file__))
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chromedriver_path = os.path.join(script_directory, 'chromedriver.exe')

service = ChromeService(executable_path=chromedriver_path)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service, options=options)

# chrome driver
# 무신사 접속
url = 'https://store.musinsa.com/app/styles/lists'
driver.get(url)
time.sleep(10)  # 2초 기다림

# 여성 선택
driver.find_element(By.XPATH, '//*[@id="footerCommonPc"]/div[1]/button[2]').click()
# 남성 선택
    #driver.find_element(By.XPATH, '//*[@id="footerCommonPc"]/div[1]/button[2]').click()
# 스크롤 창의 맨 위로 올리기
driver.execute_script('window.scrollTo(0,0)')

# 옷 카테고리 선택 (카테고리에 맞게 바꾸세요)
for num in range(5,10):
    if num ==1:
        c = "아메리칸 캐주얼"
    elif num ==2:
        c = "캐주얼"
    elif num ==3:
        c = "시크"
    elif num ==4:
        c = "댄디"
    elif num ==5:
        c = "포멀"
    elif num ==6:
        c = "골프"
    elif num ==7:
        c = "스포츠"
    elif num ==8:
        c = "스트릿"
    else:
        c = "고프코어"
    time.sleep(10)  # 2초 기다림
    element = driver.find_element(By.XPATH, f'//*[@id="catelist"]/div[3]/div/dl/dd/ul/li[{num}]/a/span')
    driver.execute_script("arguments[0].click();", element)
    

    # 스크롤 창의 맨 위로 올리기
    driver.execute_script('window.scrollTo(0,0)')

    # 이미지 담을 폴더 만들기 (자기가 맡은 카테고리로 폴더명 설정)
    img_folder = f'./남성_{c}_images'
    os.makedirs(img_folder, exist_ok=True)

    # 전체 페이지 수 구하기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    total_pages = int(soup.find(attrs={'class': 'totalPagingNum'}).get_text().strip())
    print(total_pages)
    # 이미지 url 리스트 만들기
    img_url = []

    for page in range(total_pages):
        print(page)
        # 한 페이지마다 images 긁어오기
        images = driver.find_elements(By.CSS_SELECTOR, "div.style-list-item__thumbnail > a > div > img")
        for image in images:
            url = image.get_attribute('src')
            img_url.append(url)
            

        page_index = page % 10 + 3

        # 마지막 페이지라면 그만
        if (page + 1) == total_pages or page:
            pass
        # 페이지가 10단위라면 화살표 클릭
        elif (page + 1) % 10 == 0:
            time.sleep(0.8)
            driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/form/div[4]/div/div[1]/div/div/a[13]').send_keys(Keys.ENTER)
            time.sleep(0.8)
            
        # 다음 페이지로 이동
        else:
            time.sleep(0.8)
            driver.find_element(By.XPATH, f'/html/body/div[3]/div[2]/form/div[4]/div/div[4]/div/div/a[{page_index}]').send_keys(Keys.ENTER)
            time.sleep(0.8)

        # 폴더에 이미지 저장
    for index, link in enumerate(img_url):
        urlretrieve(link, os.path.join(img_folder, f"{index}.jpg"))