import requests

# OpenWeatherMap API 키 (자신의 API 키로 대체하세요)
API_KEY = 'your_api_key_here'
# 사용할 도시 이름 (예: Seoul, New York, Tokyo)
city = 'Seoul'
# API 엔드포인트 URL
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

try:
    # API 호출
    response = requests.get(url)
    # 응답이 성공적으로 반환되었는지 확인
    response.raise_for_status()
    # JSON 데이터 파싱
    data = response.json()

    # 필요한 정보 추출
    city_name = data['name']
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']

    # 결과 출력
    print(f"City: {city_name}")
    print(f"Temperature: {temperature}°C")
    print(f"Weather: {weather_description}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")