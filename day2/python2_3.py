#for 변수 in 리스트(튜플 or 문자열):
#    수행문1

a = [1,2,3]
for i in a:
    print(i)

# i는 list의 구성요소
# 아래의 경우는 dicetionary를 의미함
list = [{"name":"가"}, {"name":"나"}, {"name":"다"}]
for i in list:
    print(i)
    print(list[i]["name"])

list2 = [{"name":"이현주", "score":40}, {"name":"김동민", "score":60}]
for i in list2:
    print(list2[i]["name"] + "의 점수는 " + str(list2[i]["score"]))

index = 1
list3 = [{"name":"이현주", "score":40}, {"name":"김동민", "score":60}]
for i in list3:
    print(str(index) + "번째: " + i["name"] + "의 점수는  " + str(i["score"]))
    index = index + 1

# 50점 이상인 사람은 합격 출력하기
index = 1
for i in list3:
    if i["score"] >= 50:
        print(str(index) + "번째: "+ i["name"] + " 합격")
    else:
        print(str(index) + "번째: "+ i["name"] + " 불합격")
    indesx = index + 1


                                  
                                     
