### 두 원 사이의 정수 쌍
### Lv 2
-  일단 보류... 시간 초과..
```
def solution(r1, r2):
    count = 0 
    for i in range(0 , r2 +1):
        for j in range(0, r2 +1):
            width =  ((i)**2 + (j)**2)**0.5
            if width >= r1 and width <= r2 :
                count += 1
    return (count *4) - ((r2-r1+1)*2)*2
```

![image](https://github.com/wldud01/Algorithm_Test/assets/64887559/c24fec58-fc51-4479-9e61-a63ea6f06530)
