# # # 퀴즈 1번 변형으로 반복문으로 품
# while True:
#     입력 = input('안녕하세요를 입력하세요')
#     if 입력 == '안녕하세요':
#         print('반갑습니다.')
#         break
#     else:
#         print('다시 작성하세요')

# # # 퀴즈 2번 반복문으로 품
# while True:
#     숫자 = int(input('숫자를 입력하시오'))
#
#     계산 = 숫자 + 100
#     if 계산 > 150:
#         print(숫자)
#         break
#     else:
#         if 계산 <= 150:
#             print('값이 부족합니다. 다른 숫자를 입력하쇼')
#
# # 퀴즈 3번 else 구문을 쓰면 편함
# 입력 = int(input('숫자를 입력하시오 2'))
# if 5<입력<10 :
#     print('ok')
# elif 입력<=5 :
#     print('no')
# elif 10<=입력 :
#     print('no')
# else :
#     print('no')

입력 = input('자 여기서 문제 계절 하나를 입력해보세요')
fruit = {'봄':'딸기', '여름':'토마토', '가을': '사과'}
if 입력 in fruit.values() :
    print('정답입니다.')
else :
    print('오답입니다.')
# 벨류안에 있는지 알고싶으면 values()를 넣으면 됨 아니면 기본적으로 키값만 찾아준다
# 퀴즈는 항상 새로운 파일을 만들자

