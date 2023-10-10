import os
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

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
driver.find_element(By.XPATH, '//*[@id="footerCommonPc"]/div[1]/button[3]').click()
driver.execute_script('window.scrollTo(0,0)')

# 옷 카테고리 선택 (카테고리에 맞게 바꾸세요)
for num in range(2,12):
    if num ==1:
        c = "아메리칸 캐주얼"
    elif num ==2:
        c = "캐주얼"
    elif num ==3:
        c = "시크"
    elif num ==4:
        c = "포멀"
    elif num ==5:
        c = "걸리시"
    elif num ==6:
        c = "골프"
    elif num ==7:
        c = "레트로"
    elif num ==8:
        c = "로맨틱"
    elif num ==9:
        c = "스포츠"
    elif num ==10:
        c = "스트릿"
    elif num ==11:
        c = "고프코어"


    time.sleep(10)  # 2초 기다림
    element = driver.find_element(By.XPATH, f'//*[@id="catelist"]/div[3]/div/dl/dd/ul/li[{num}]/a/span')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)  # DOM 업데이트를 기다림

    img_folder = f'./여성_{c}_images'
    os.makedirs(img_folder, exist_ok=True)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    li_elements = driver.find_elements(By.XPATH, '//*[@id="brandLayer"]/li')
    for index in range(1, 31):
        element = driver.find_element(By.XPATH, f'//*[@id="brandLayer"]/li[{index}]/a[1]/span[1]')
        driver.execute_script("arguments[0].click();", element)

            # 페이지가 로드될 때까지 기다리는 코드 추가 (필요에 따라 조정)
            # 예를 들어, 5초간 기다릴 경우
          
        time.sleep(5)
        
        brand_name_element = driver.find_element(By.XPATH, f'//*[@id="brandLayer"]/li[{index}]/a/span[1]')
        brand_name = brand_name_element.text
        if brand_name:
            print("yes")
        else:
            print("no")
        print(brand_name)
        time.sleep(2)  # DOM 업데이트를 기다림
                
            # 스크롤 창의 맨 위로 올리기
        driver.execute_script('window.scrollTo(0,0)')

        # 이미지 담을 폴더 만들기 (자기가 맡은 카테고리로 폴더명 설정)
            

            # 전체 페이지 수 구하기
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        total_pages = int(soup.find(attrs={'class': 'totalPagingNum'}).get_text().strip())
        print(total_pages)
            # 이미지 url 리스트 만들기
        img_url = []
        i=0
        for page in range(total_pages):
                
            # 한 페이지마다 images 긁어오기
            images = driver.find_elements(By.CSS_SELECTOR, "div.style-list-item__thumbnail > a > div > img")
            j=0
            for image in images:
                j+=1
                url = image.get_attribute('src')
                i+=1
                print(url)
                
                # Title 가져오기
                title_element = driver.find_element(By.XPATH, f'/html/body/div[3]/div[2]/form/div[4]/div/ul/li[{j}]/div[2]/a')
                title = title_element.get_attribute('title')
                    
                # Date 가져오기
                date_element = driver.find_element(By.XPATH, f'/html/body/div[3]/div[2]/form/div[4]/div/ul/li[{j}]/div[3]/span[1]')
                date_text = date_element.text
                if date_text == 'N':
                    date_element = driver.find_element(By.XPATH, f'/html/body/div[3]/div[2]/form/div[4]/div/ul/li[{j}]/div[3]/span[2]')
                    date_text = date_element.text
                    date_parts = date_text.split('.')

                    second_month = date_parts[1]
                else:
                    date_parts = date_text.split('.')
                    second_month = date_parts[1]
                                    
                file_name = f"여성_{c}_{brand_name}_{title}_{second_month}_{i}.jpg"
                urlretrieve(url, os.path.join(img_folder, file_name))
                        

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
            if page >=10:
                break
        if index == len(li_elements):
            driver.get("https://store.musinsa.com/app/styles/lists")

    for index in range(32, len(li_elements) + 1):
        if index == 31:
            plus = driver.find_element(By.XPATH, '//*[@id="catelist"]/div[2]/dl/dt/div/a')
            driver.execute_script("arguments[0].click()", plus)
            driver.execute_script('window.scrollTo(0,0)')
            time.sleep(5)
            plus_clicked = True  # Set the flag
            if plus_clicked:
                print("The 'plus' element was clicked.")
            else:
                print("The 'plus' element was not clicked.")

        element = driver.find_element(By.XPATH, f'//*[@id="brandLayer"]/li[{index}]/a[1]/span[1]')
        driver.execute_script("arguments[0].click();", element)
        

            # 페이지가 로드될 때까지 기다리는 코드 추가 (필요에 따라 조정)
            # 예를 들어, 5초간 기다릴 경우
          
        time.sleep(5)
        
                        
            # 스크롤 창의 맨 위로 올리기
        driver.execute_script('window.scrollTo(0,0)')

        # 이미지 담을 폴더 만들기 (자기가 맡은 카테고리로 폴더명 설정)
            

            # 전체 페이지 수 구하기
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        total_pages = int(soup.find(attrs={'class': 'totalPagingNum'}).get_text().strip())
        print(total_pages)
            # 이미지 url 리스트 만들기
        img_url = []
        i=0
        for page in range(total_pages):
                
            # 한 페이지마다 images 긁어오기
            images = driver.find_elements(By.CSS_SELECTOR, "div.style-list-item__thumbnail > a > div > img")
            j=0
            for image in images:
                j+=1
                url = image.get_attribute('src')
                i+=1
                print(url)
                brand_element = driver.find_element(By.CSS_SELECTOR, '#brandLayer > li.brandList.selected > a:nth-child(1)')
                brand_name = driver.execute_script("return arguments[0].innerText;", brand_element)

                print(brand_element)

                # Title 가져오기
                title_element = driver.find_element(By.XPATH, f'/html/body/div[3]/div[2]/form/div[4]/div/ul/li[{j}]/div[2]/a')
                title = title_element.get_attribute('title')
                    
                # Date 가져오기
                date_element = driver.find_element(By.XPATH, f'/html/body/div[3]/div[2]/form/div[4]/div/ul/li[{j}]/div[3]/span[1]')
                date_text = date_element.text
                if date_text == 'N':
                    date_element = driver.find_element(By.XPATH, f'/html/body/div[3]/div[2]/form/div[4]/div/ul/li[{j}]/div[3]/span[2]')
                    date_text = date_element.text
                    date_parts = date_text.split('.')

                    second_month = date_parts[1]
                else:
                    date_parts = date_text.split('.')
                    second_month = date_parts[1]
                                    
                file_name = f"여성_{c}_{brand_name}_{title}_{second_month}_{i}.jpg"

                # 파일명에서 불허용 문자 제거
                file_name = "".join(x for x in file_name if x.isalnum() or x in ('_', ' '))

                # 중복된 공백 및 언더스코어 제거
                file_name = ' '.join(file_name.split())

                # 파일 경로로 저장
                file_path = os.path.join(img_folder, file_name)

                urlretrieve(url, file_path)
                        

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
            if page >=4:
                break
        if index == len(li_elements):
            driver.get("https://store.musinsa.com/app/styles/lists")    

            

####################################################################################################################################################################################
# 남성선택
driver.find_element(By.XPATH, '//*[@id="footerCommonPc"]/div[1]/button[3]').click()
driver.execute_script('window.scrollTo(0,0)')

# 옷 카테고리 선택 (카테고리에 맞게 바꾸세요)
for num in range(1,10):
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
    time.sleep(2)  # DOM 업데이트를 기다림

    img_folder = f'./남성_{c}_images'
    os.makedirs(img_folder, exist_ok=True)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    li_elements = driver.find_elements(By.XPATH, '//*[@id="brandLayer"]/li')
    for index in range(1, 31):
        if index > 30:
            plus = driver.find_element(By.XPATH, '//*[@id="ico30"]')
            driver.execute_script("arguments[0].click()", plus)
            time.sleep(5)
            element = driver.find_element(By.XPATH, f'//*[@id="brandLayer"]/li[{index}]/a[1]/span[1]')
            driver.execute_script("arguments[0].click();", element)

            # 페이지가 로드될 때까지 기다리는 코드 추가 (필요에 따라 조정)
            # 예를 들어, 5초간 기다릴 경우
            time.sleep(5)
            brand_name_element = driver.find_element(By.XPATH, f'//*[@id="brandLayer"]/li[{index}]/a[1]/span[1]')
            brand_name = brand_name_element.text
            print(brand_name)
            time.sleep(2)  # DOM 업데이트를 기다림

                
            # 스크롤 창의 맨 위로 올리기
            driver.execute_script('window.scrollTo(0,0)')

            # 이미지 담을 폴더 만들기 (자기가 맡은 카테고리로 폴더명 설정)
            

            # 전체 페이지 수 구하기
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            total_pages = int(soup.find(attrs={'class': 'totalPagingNum'}).get_text().strip())
            print(total_pages)
            # 이미지 url 리스트 만들기
            img_url = []
            i=0
            for page in range(total_pages):
                
                # 한 페이지마다 images 긁어오기
                images = driver.find_elements(By.CSS_SELECTOR, "div.style-list-item__thumbnail > a > div > img")
                for image in images:
                    url = image.get_attribute('src')
                    i+=1

                    # Title 가져오기
                    title_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/form/div[4]/div/ul/li[1]/div[2]/a')
                    title = title_element.get_attribute('title')
                    
                    # Date 가져오기
                    date_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/form/div[4]/div/ul/li[1]/div[3]/span[1]')
                    date_text = date_element.text
                    if date_text == 'N':
                        date_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/form/div[4]/div/ul/li[1]/div[3]/span[2]')
                        date_text = date_element.text
                        date_parts = date_text.split('.')

                        second_month = date_parts[1]
                    else:
                        date_parts = date_text.split('.')
                        second_month = date_parts[1]
                                    
                    file_name = f"남성_{c}_{brand_name}_{title}_{second_month}_{i}.jpg"
                    urlretrieve(url, os.path.join(img_folder, file_name))
                        

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
                if page >=4:
                    break
            if index == len(li_elements):
                driver.get("https://store.musinsa.com/app/styles/lists")

            pass
        else:
            element = driver.find_element(By.XPATH, f'//*[@id="brandLayer"]/li[{index}]/a[1]/span[1]')
            driver.execute_script("arguments[0].click();", element)

            # 페이지가 로드될 때까지 기다리는 코드 추가 (필요에 따라 조정)
            # 예를 들어, 5초간 기다릴 경우
            time.sleep(5)
            brand_name_element = driver.find_element(By.XPATH, f'//*[@id="brandLayer"]/li[{index}]/a[1]/span[1]')
            brand_name = brand_name_element.text
            print(brand_name)
            time.sleep(2)  # DOM 업데이트를 기다림

                
            # 스크롤 창의 맨 위로 올리기
            driver.execute_script('window.scrollTo(0,0)')

            # 이미지 담을 폴더 만들기 (자기가 맡은 카테고리로 폴더명 설정)
            

            # 전체 페이지 수 구하기
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            total_pages = int(soup.find(attrs={'class': 'totalPagingNum'}).get_text().strip())
            print(total_pages)
            # 이미지 url 리스트 만들기
            img_url = []
            i=0
            for page in range(total_pages):
                
                # 한 페이지마다 images 긁어오기
                images = driver.find_elements(By.CSS_SELECTOR, "div.style-list-item__thumbnail > a > div > img")
                for image in images:
                    url = image.get_attribute('src')
                    i+=1
                    print(url)
                    i+=1
                    # Title 가져오기
                    title_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/form/div[4]/div/ul/li[1]/div[2]/a')
                    title = title_element.get_attribute('title')
                   # Date 가져오기
                    date_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/form/div[4]/div/ul/li[1]/div[3]/span[1]')
                    date_text = date_element.text
                    if date_text == 'N':
                        date_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/form/div[4]/div/ul/li[1]/div[3]/span[2]')
                        date_text = date_element.text
                        date_parts = date_text.split('.')
                        second_month = date_parts[1]
                    else:
                        date_parts = date_text.split('.')
                        second_month = date_parts[1]
                                    
                    file_name = f"남성_{c}_{brand_name}_{title}_{second_month}_{i}.jpg"
                    urlretrieve(url, os.path.join(img_folder, file_name))
                    
                        

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
                if page >=4:
                    break
            if index == len(li_elements):
                driver.get("https://store.musinsa.com/app/styles/lists")
    for index in range(32, len(li_elements) + 1):
        if index == 31:
            plus = driver.find_element(By.XPATH, '//*[@id="catelist"]/div[2]/dl/dt/div/a')
            driver.execute_script("arguments[0].click()", plus)
            driver.execute_script('window.scrollTo(0,0)')
            time.sleep(5)
            plus_clicked = True  # Set the flag
            if plus_clicked:
                print("The 'plus' element was clicked.")
            else:
                print("The 'plus' element was not clicked.")

        element = driver.find_element(By.XPATH, f'//*[@id="brandLayer"]/li[{index}]/a[1]/span[1]')
        driver.execute_script("arguments[0].click();", element)
        

            # 페이지가 로드될 때까지 기다리는 코드 추가 (필요에 따라 조정)
            # 예를 들어, 5초간 기다릴 경우
          
        time.sleep(5)
        
                        
            # 스크롤 창의 맨 위로 올리기
        driver.execute_script('window.scrollTo(0,0)')

        # 이미지 담을 폴더 만들기 (자기가 맡은 카테고리로 폴더명 설정)
            

            # 전체 페이지 수 구하기
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        total_pages = int(soup.find(attrs={'class': 'totalPagingNum'}).get_text().strip())
        print(total_pages)
            # 이미지 url 리스트 만들기
        img_url = []
        i=0
        for page in range(total_pages):
                
            # 한 페이지마다 images 긁어오기
            images = driver.find_elements(By.CSS_SELECTOR, "div.style-list-item__thumbnail > a > div > img")
            j=0
            for image in images:
                j+=1
                url = image.get_attribute('src')
                i+=1
                print(url)
                brand_element = driver.find_element(By.CSS_SELECTOR, '#brandLayer > li.brandList.selected > a:nth-child(1)')
                brand_name = driver.execute_script("return arguments[0].innerText;", brand_element)

                print(brand_element)

                # Title 가져오기
                title_element = driver.find_element(By.XPATH, f'/html/body/div[3]/div[2]/form/div[4]/div/ul/li[{j}]/div[2]/a')
                title = title_element.get_attribute('title')
                    
                # Date 가져오기
                date_element = driver.find_element(By.XPATH, f'/html/body/div[3]/div[2]/form/div[4]/div/ul/li[{j}]/div[3]/span[1]')
                date_text = date_element.text
                if date_text == 'N':
                    date_element = driver.find_element(By.XPATH, f'/html/body/div[3]/div[2]/form/div[4]/div/ul/li[{j}]/div[3]/span[2]')
                    date_text = date_element.text
                    date_parts = date_text.split('.')

                    second_month = date_parts[1]
                else:
                    date_parts = date_text.split('.')
                    second_month = date_parts[1]
                                    
                file_name = f"남성_{c}_{brand_name}_{title}_{second_month}_{i}.jpg"

                # 파일명에서 불허용 문자 제거
                file_name = "".join(x for x in file_name if x.isalnum() or x in ('_', ' '))

                # 중복된 공백 및 언더스코어 제거
                file_name = ' '.join(file_name.split())

                # 파일 경로로 저장
                file_path = os.path.join(img_folder, file_name)

                urlretrieve(url, file_path)
                        

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
            if page >=4:
                break
        if index == len(li_elements):
            driver.get("https://store.musinsa.com/app/styles/lists") 