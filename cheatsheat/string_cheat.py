# 해당 성분이 처음 등장하는 인덱스 찾기. 없으면 -1 반환
s = 'Hello'
print(s.find('e'))
# >> 1
s = 'Heeello!'
print(s.find('e'))
# >> 1
# 몇번째로 등장하는 지도 인덱스로 찾을 수 있음
print(s.find('e', 3))
# >> 3
print(s.find('z'))
# >> -1

s = 'Hello World!'
print(s.replace('World', 'Python'))
# >> Hello Python!

# 모든 문자열이 숫자로 이루어져있는 지 확인
s = '1234'
print(s.isdigit())
# >> True
s = 'as123'
print(s.isdigit())
# >> False

## 알파벳으로만 이루어진 지 확인인
s = 'Hello'
print(s.isalpha())
# >> True
s = '1q2w3e4r'
print(s.isalpha())
# >> False
## 알파벳과 숫자로만 이루어져 있는 지 확인
print(s.isalnum())
# >> True

## 문자열 내 몇개 등장했는 지 셈
s = 'Saaay'
print(s.count('a'))
# >> 3

s = 'Hee!23l!3!#$!@o'
for ch in s:
    if not ch.isalnum():
        print(f'{ch}는 특수문자')

## 공식 라이브러리도 활용간으
from string import punctuation
s = "Hello@Python3!"
specials = [ch for ch in s if ch in punctuation]
print(specials)
# >> ['@', '!']