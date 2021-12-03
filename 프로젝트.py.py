import random

print("<결혼을 약속한 알라딘과 공주는 행복한 나날을 보내고 있었다>")
print()
print("<하지만 결혼식 전날 공주가 도적단에게 납치 당했다>")
print("........ ..")
print()
print("<알라딘은 모든 일을 멈추고 공주를 찾아 나섰지만 쉽게 찾기 힘들었다.>" )
print()
print("<공주의 소식을 들었고 많은 돈을 준다면 공주를 다시 돌려주겠다고 말한다.>")
print()
print("<알라딘은 금이 많다는 동굴에 가서 금화를 얻기로 하는데...>")
print()
print()
print("========================================================")
print()
print("<동굴에 도착한 알라딘은 지니를 만나게 되었다.>")
print()
print("지니:너도 금화를 얻으러 왔는가? 금화를 얻으려면 나와 게임을 해야해 할 거지?")
print()
print("알라딘: 물론 할 거야")
print()
print("지니: 그럼 게임을 시작하지.")
print()
print("=====================================================================")



#지니가 가위바위보 이겼을때
def winGennie():
    print("지니: 내가 먼저하지")
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    res1=dice1+dice2
    print()
    print("총", res1, "이군")
    
    n1=int(input("지니:준비되면 1을 입력하게==>"))
    if n1==1:
        dice3=random.randint(1,6)
        dice4=random.randint(1,6)
        res2=dice3+dice4
        print("알라딘: 총", res2, "이야")

    if res1>res2:
        print("지니: 내가 이겼네. 자네는 금화를 가질 수 없어.")
        print()
    else:
        print("알라딘: 이겼다")
        print()
        print("알라딘: 이제 금화를 줘")
        print("알라딘 금화 획득")
        print("<알라딘 소지 금화:", money+10,"개>")
    


#알라딘이 가위바위보 이겼을때        
def winAladin():
    print("알라딘: 내가 먼저하지")
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    res1=dice1+dice2
    print()
    print("총", res1, "이야")

    n1=int(input("알라딘: 준비되면 1을 입력해"))
    if n1==1:
        dice3=random.randint(1,6)
        dice4=random.randint(1,6)
        res2=dice3+dice4
        print("총", res2, "이군")

    if res1<res2:
        print("지니: 내가 이겼네. 자네는 금화를 가질 수 없어.")
    else:
        print("알라딘: 이겼다")
        print()
        print("알라딘:이제 금화를 줘")
        print()
        print("알라딘 금화 획득")
        print("<알라딘 소지 금화:", money+10,"개>")


print("지니:이번 게임은 단판 승부다. 이 주사위 2개를 던져서 나오는 합의 수가 크거나 같으면 이기는 게임이다. 이기면 금화를 주도록 하지")
print()
money=5
#알라딘 소지 금액 표시
print("<알라딘 소지 금화:", money,"개>") 
print("지니: 먼저 가위바위보로 순서를 정하자")
print()

#가위바위보
while True:
 gennie = random.choice(['가위', '바위', '보'])
 player = input('가위 바위 보 중 하나를 입력하세요: ')
 if gennie == '가위':
    print('지니: 가위')
    if player == '가위':
        print('알라딘: 가위')
        print()
        print('무승부')
        continue
    
    elif player == '바위':
        print('알라딘:바위')
        print()
        print('알라딘 승리')
        hap=winAladin()
        break
    
    elif player == '보':
        print('알라딘: 보')
        print()
        print('지니 승리')
        hap=winGennie()
        break
    
 elif gennie == '바위':
    print('지니: 바위')
    if player == '가위':
        print('알라딘: 가위')
        print()
        print('지니 승리')
        hap=winGennie()
        break
    
    elif player == '바위':
        print('알라딘=바위')
        print()
        print('무승부')
        continue
    elif player == '보':
        print('알라딘:보')
        print()
        print('알라딘 승리')
        hap=winAladin()
        break
    
 elif gennie == '보':
    print('지니=보')
    if player == '가위':
        print('알라딘=가위')
        print()
        print('알라딘 승리')
        hap=winAladin()
        break
    
    elif player == '바위':
        print('지니=바위')
        print()
        print('지니 승리')
        hap=winGennie()
        break
    
    elif player == '보':
        print('알라딘= 보')
        print()
        print('무승부')
        continue


print(" 지니 : 이번엔 보너스로 금화를 더 얻을 수 도 있고..")
print(" 지니 : 모두 잃을 수도 있으니 조심하도록 해라...")
print()
print(" 지니 : 자 그럼 따라오도록 하지")
print()

# 카드 지정
card = 1,2,3
card2 = 4,5



print(" 지니 : 반갑다, 알라딘")
print(" 지니 : 보너스 금화 게임을 시작하도록 하지!!")
print()
print(" 지니 : 단계를 통화하면  너가 걸었던 금화의 3배를 주도록하지!! ")
print ("=" * 50)
print()

# 소지 금화 표시

print()

# 금화 갯수 입력받기
gold = int (input(" 지니 : 게임할 금화를 입력해라. 금화 갯수:>>>"))
print(" 지니 :  총 ",gold, "개를 걸었군..")
print()

# 카드 랜덤 지정
print(card)
card_num = random.randint (1,3)

a_choice = int(input(" 지니 : 3가지의 카드 중 하나의 카드를 선택해라. {{{1,2,3}}}   >>>"))
print()

# 카드 게임 
if a_choice == card_num :
    print(" 지니 : 축하한다. 3배를 주도록 하지. 총 금화가 ", gold * 3, "개이다.")
    print()
    b_choice = input(" 지니:한 번 더 할 것인가? 이번엔 2배를 주도록 하지!!   한다 or 안한다>>>")
    print()
    if  b_choice == "한다" :
        print(" 자니: 다음 단계로 가도록 하지 ")
        print()

       # 두번째 게임
        print(card2)
        card2_num = random.randint(4,5)
       
        c_choice = int(input(" 지니 : 2가지의 카드 중 하나의 카드를 선택해라. {{{4 ,5}}} >>>"))
        print()

        if card2_num == c_choice:
            print(" 지니: 축하한다. 2배를 주도록 하지. 총 금화가 ", gold*5,"개이다.")
            print()
            print("< 알라딘은 지니를 이겼다! >")
            print()
            print("< 공주를 구할 돈을 얻은 알라딘은 바로 공주에게 달려간다.. >")
            print()
            print("< 공주를 만나 행복하게 결혼식을 했다.. >")

        else:
            print(" 지니 : 아쉽군.. 금화는 내가 다 가져가도록 하지...")
            print()
            print("< 알라딘은 지니를 이기지 못했다.. >")
            print()
            print("< 금화가 부족한 알라딘은 눈물을 흘리며 고민에 빠지게 된다... >")
            
            
    else:
        print(" 지니 : 여기까지인가.. 총 금화가 ", gold* 3,"개이다. 잘가라..")
        print()
        print("< 지니를 이긴 알라딘은 공주에게 달려간다.. >")
        print()
        print("< 공주를 만나 행복하게 결혼식을 했다.. >")
        

else:
    print(" 지니 : 아쉽군.. 금화는 내가 다 가져가도록 하지")
    print()
    print("< 알라딘은 지니를 이기지 못했다.. >")
    print()
    print("< 금화가 부족한 알라딘은 눈물을 흘리며 고민에 빠지게 된다... >")

