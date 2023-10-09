# CR
Cloth_Recommandation
![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=235&section=footer&text=무천장Project&fontColor=423F3E&fontSize=90&animation=fadeIn)

##  프로젝트 - 무신사 옷장 추천 시스템
**김성현**

## Introduction
### 국내 최대 쇼핑몰 무신사의 코디를 활용한 나만의 코디 추천 시스템
<br>
1. 내가 가지고 있는 옷을 올리면, 무신사에서 비슷한 코디를 추천해줍니다. <br>
2. 원하는 스타일을 선택하면, 무신사에서 그와 비슷한 코디 집단을 출력해줍니다.

## DataSet
- 무신사 코디 페이지 이미지 크롤링
- 기준 
  1. 성별 2. 카테고리 3. 계절 구분
  
## Model
- Feature Extraction by **VGG16**
- 16개 층으로 구성된 모델
- 하나의 이미지 (224*224*3)에서 4096개의 feature 추출

### Model-A
- 각 사진의 Feature끼리 cosine similarity 계산
- 가장 유사한 상위 5개 이미지 추천 
