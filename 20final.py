
# 1

def gcd(x, y):
    while True:
        if x==y:
            return x
            break
        else:
            if x>y:
                x = x-y
            else:
                y = y-x
num1 = 30
num2 = 18

print("최대공약수 =", gcd(num1, num2))

# 2
def charge (t):
    if t<=15:
        return 0
    elif t<=30:
        return 3000
    else:
        if ((t-30)%15)==0:
            add = (t-30)//15*1000
        else:
            add = (((t-30)//15)+1)*1000
        return 3000 + add

t = int(input("주차한 시간을 분 단위로 입력하시오:"))
print("주차시간 = %d분, 주차요금 = %d원"%(t, charge(t)))

#3
def sum(n):
    sum = 0
    for i in n:
        sum+=int(i)
    return sum
print(sum(input("정수 입력:")))

#4

def count(text):
    sum1=0
    sum2=0
    for i in range(0,10):
        sum1+=text.count(str(i))
      
    for i in "aeiouAEIOU":    
        sum2+=text.count(i)
    
    return sum1, sum2

with open("C:\\Users\\bahng\\Documents\\튜터링\\finaltext.txt","r") as f:
    text = f.read()
print(text)
sum1, sum2 = count(text)
print("모음 개수:",sum2)
print("숫자 개수:",sum1)

#5

class Box:
    def setdata(self, width, depth, height):
        self.width = width
        self.depth = depth
        self.height = height
    def volume(self):
        volume = self.width * self.depth * self.height
        return volume

test = Box()
test.setdata(50,50,50)
print("부피:",test.volume())
