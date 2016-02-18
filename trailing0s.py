def n5(n):
    """divide n by 5, if n is an integer
    you will get the integer quotient with
    no remainder"""
    return n/5

def maxPower5(n):
    """return highest x such that 5^x is less than n"""
    i = 0
    while 5**i <= n:
        i += 1
    return i

def fact(n):
    """recursively calculate n!"""
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
    
def n0s(n):
    """calculate the number of trailing 0's n! would have"""
    #base cases
    if n <= 5:
        if n==5:
            return 1
        else:
            return 0
    #if n%5 then # 0s will increase
    elif n%5==0:
        #find what power of 5 is in the prime factorization
        #this is how much the 0s will increase from n-1 to n
        powerOf5=1
        x = n/5
        while x%5==0:
            powerOf5 += 1
            x=x/5
        #since the # 0s won't increase on n not divisible by 5, 
        #don't need to recurse through every value to find the prior # of 0s
        return powerOf5 + n0s(n-5)
    else:
        #the # 0s will not increase
        #don't need to recurse through every value to find the prior # of 0s
        diff = (n-1)%5
        return n0s(n-1-diff)
    
def n0s2(n):
    """simplified version to predict number of trailing 0's in n!"""
    i = 1
    sum0s = 0
    while 5**i <= n:
        sum0s += n/5**i
        i += 1
        #print i, sum0s
    return sum0s
    
class memoFact(object):
    def __init__(self):
        self.memo = {}
        self.memo0s = {}
        
    def setFact(self, n, nfactorial):
        """memoize a factorial"""
        if n in self.memo.keys():
            pass
        else:
            self.memo[n] = nfactorial
            
    def effFact(self, n):
        """efficient factorial, uses memoized values of
        previously run factorials"""
        if n == 0:
            return 1
        elif n in self.memo.keys():
            #print "use a value in the dict"
            return self.memo[n]
        else:
            #print "recurse"
            return n*self.effFact(n-1)
        
    def factSeries(self, n1, n2, step=1):
        """memoizes factorials and trailing 0s between n1 and n2 inclusive
        n2 > n1"""
        for i in xrange(n1, n2+1, step):
            ifact = self.effFact(i)
            i0s = self.countTrailing0s(ifact)
            self.setFact(i, ifact)
            self.set0s(i, i0s)
            #print ifact
        return None
    
    def countTrailing0s(self, nfactorial):
        """returns number of 0s at end of n!"""
        strn = str(nfactorial)
        i = -1
        count = 0
        while strn[i] == "0":
            #print i, strn[i]
            count += 1
            i -= 1
        return count
    
    def set0s(self, n, n0s):
        """memoizes the number of trailing 0s for n!"""
        if n in self.memo0s.keys():
            pass
        else:
            self.memo0s[n] = n0s
            
    def __repr__(self):
        rangei = self.memo.keys()
        rangei.sort()
        strself = ""
        for i in rangei:
            if i in self.memo0s.keys():
                i0s = self.memo0s[i]
            else:
                i0s = self.countTrailing0s(self.memo[i])
                self.memo0s[i] = i0s
            #prediction = n0s(i)
            prediction = n0s2(i)
            #strself += str(i) + "\t" + str(self.memo[i]) + "\t" + str(i0s) + "\n"
            #strself += str(i) + "\t" + str(i0s) + "\t" + str(n5(i)) + "\t" + str(maxPower5(i)) + "\n"
            strself += str(i) + "\t" + str(i0s) + "\t" + str(prediction) + "\t" + str(prediction == i0s) + "\n"
        return strself
        
#store = memoFact()
#ser = store.factSeries(0, 81, 4)
#ser2 = store.factSeries(618, 627)
#ser3 = store.factSeries(24, 26)
#print store