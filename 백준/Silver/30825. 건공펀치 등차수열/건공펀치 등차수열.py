# https://www.acmicpc.net/problem/30825

n, k = map(int, input().split())
a_list = list(map(int, input().split()))

ans = 0

for i in range(len(a_list) - 1):
    # print(a_list)
    #현재 vs 이후의 값 비교 > k가 아니면 조정 하는 식으로
    if a_list[i + 1] - a_list[i]  != k:#공차수열 아닌 경우
        
        if (a_list[i + 1] - a_list[i]) < k:#이후의 값 조정
            
            
            ans += (a_list[i] + k) - a_list[i + 1]
            # print(ans)
            a_list[i + 1] = a_list[i] + k
            
            
        elif a_list[i + 1] - a_list[i] > k:#현재의 값 조정
            temp_ans = (a_list[i + 1] - a_list[i]) - k
            ans += temp_ans
            # print(ans, '!')
            a_list[i] = a_list[i + 1] - k
            #i가 현재, 0 ~ i-1 까지 tempans만큼 증가시키자
            for i2 in range(0, i -1 + 1):
                a_list[i2] += temp_ans
                ans += temp_ans
                # print(ans, '!!')
                
        else:
            print("예외 경우 발생")

        
# print(a_list)

print(ans)


##현재의 것을 증가시키는 방식은
#다음 것을 증가 시키는 케이스와 충돌

##그냥 뒤에서부터 시작하는건?< 똑같을듯;

#또틀림; 


