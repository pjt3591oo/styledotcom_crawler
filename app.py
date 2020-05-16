import requests as rq
import pandas as pd

URL = "https://api.sta1.com/api/front/v1/stores?ps=60&pg=%d&type=S&gndr=F&ages=&sort=nv"
current_page = 1

# In-Sess에 따라 세션만료가 될 수 있음.
# 세션 만료시 401 코드발생
# chrome-DevTools/네트워크 탭에서 URL을 찾은 뒤 Request Headers 영역에서 in-sess를 찾은 뒤 변경해준다
headers = {
  'In-Sess': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxNDU0M2UyOWRlZjE0Njg5OTFkOGJjNDk3YTlmNTM1MSIsImlhdCI6MTU4OTY2ODU1NywiZXhwIjoxNTg5NjcyMTU3LCJob3N0IjoiVyIsImRldmMiOiJQIiwiaXR5cCI6IlIiLCJwc2VxIjoxLCJwY25vIjowLCJvc2VxIjowLCJva3NxIjowLCJpcCI6IjEyMS4xNjEuMTYuMTYxIiwiYXBwaWQiOiIiLCJvc3RwIjoiIiwiYXBwdiI6IiIsInBzaWQiOiIifQ.1fSZascScIo0AnyAZvqF3LCWcqjZOEWyl3F2ya9mOU8'
}

is_continue = True

result = {
  "storeName": [],
  "webUrl": [],
  "description": [],
  "cateNames": [],
  "ageNames": [],
}

while is_continue:
  res = rq.get(URL%(current_page), headers=headers)

  data = res.json()
  shops = data['data']

  for shop in shops:
    result['storeName'].append(shop.get('storeName', ''))
    result['webUrl'].append(shop.get('webUrl', ''))
    result['description'].append(shop.get('description', ''))
    result['cateNames'].append(shop.get('cateNames', ''))
    result['ageNames'].append(shop.get('ageNames', ''))
    print(shop.get('storeName', ''))

  current_page += 1 # current_page = current_page + 1

  if not len(shops):
    is_continue = False

df = pd.DataFrame(result)
df.to_csv('styledotcom.csv')