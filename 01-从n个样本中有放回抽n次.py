'''
从n个样本中抽n次，被抽到的样本点的比例趋近于1-1/e
1-(1-1/n)**n = 1-1/e，（n->infinity）
采用动态规划方法解答如下：
'''
def solution(n):
    def nToTheNthPower(n):
        a = n
        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= a
            a = a ** 2
            n = n // 2
        return res
    
    def accounts(n):
        res = [0] * (n+1)
        res[1] = n
        for i in range(2, n+1):
            for j in range(i, 1, -1):
                res[j] = res[j] * j + res[j-1] * (n-j+1)
        # print(res)
        ans = 0
        for i in range(1, n+1):
            ans += i * res[i]
        return ans

    
    return accounts(n) / nToTheNthPower(n) / n

print(solution(300))