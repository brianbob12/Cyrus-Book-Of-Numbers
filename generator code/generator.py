import math
import time

n=100000#nubmer of numbers being evaluated
#features
#-------------------------
#prime
#finbonacci
#tribonacci
#mercen primces
#perfect numbers
#factorial numbers


def getPrimes():#gets all primes up to n
    found=1#number of found primes
    guess=n/math.log(n)#a guess at how many primes to be calculated for n
    #see prime number theorem
    alert=0.01#the threashold to alert user of progress
    alertsGiven=0
    lt=time.time()#stores the last time in seconds that an alert was given
    averageTD=0#stores the average differnence in time since last alert
    
    protoPrimes=[True for i in range(n)]
    protoPrimes[0]=False
    a=1
    while a<n:
        if protoPrimes[a]:
            #deal with alerting stuff
            found+=1
            fg=found/guess
            if(fg>alert*alertsGiven):
                td=time.time()-lt
                averageTD=((averageTD*alertsGiven)+td)/(alertsGiven+1)
                print("computing primes-\t"+format(fg*100,".3f")+"%\t"+format(td,".3f")+"-"+format(averageTD,".3f"))
                lt=time.time()
                alertsGiven+=1
            
            #update numbers to go
            b=(a+1)*2
            while b-1<n:
                protoPrimes[b-1]=False
                b+=a+1
        a+=1
    final=[]
    for i,v in enumerate(protoPrimes):
        if v:
            final.append(i+1)
    return final

class Number:
    def __init__(self,val):
        self.val=val
        self.score=-1#unevaluated score
        #sequences
        self.fibonacci=False
        self.tribonacci=False
        self.lucas=False
        
        self.polygonal=[]#each element is a list:[polygonNumber,place in sequence]
        self.harshad=[]#each base in which it is a harshad number

        #divisors & number theory
        self.perfect=False
        self.abundant=False
        self.weird=False
        self.semiPerfect=False
        self.highlyAbundant=False
        self.deficient=False
        self.superAbundant=False
        self.highlyComposite=False
        self.superiorHighlyComposite=False
        self.colossallyAbundant=False
        self.primitiveAbundant=False

        #psudoprimes
        self.poulet=False#fermat psuodoprime in base 2
        self.lucasPsudoprime=False

    def __str__(self):
        out=""
        out+="\t"+str(self.val)+"\t"
        out+="\n\n"
        if self.prime:
            if self.mersenne:
                out+="mersenne prime number\n"
            else:
                out+="prime number\n"
        else:
            if self.poulet:
                out+="Poulet number(base 2 fermat psudoprime)\n"
            if self.lucasPsudoPrime:
                out+="Lucas psudoprime\n"
            out+="Prime Factors:\n"
            uniquePrimes=[]
            for i in self.primeFact:
                unique=True
                for j in uniquePrimes:
                    if j[0]==i:
                        unique=False
                        j[1]+=1
                        break
                if unique:
                    uniquePrimes.append([i,1])
            for i in uniquePrimes:
                out+="\t"
                out+=str(primes[i[0]])
                if i[1]>1:
                    out+="^"+str(i[1])
                out+="\n"
            out+="\n"
        if len(self.polygonal)>1 and self.val!=1:
            out+=("Polygonals:")
            for i in self.polygonal:
                if len(self.polygonal)>1:
                    out+="\t"
                out+=ordinal(i[1])+" "+getPolygonalName(i[0])+"("+str(i[0])+"-gon) number"
                out+="\n"
        if self.fibonacci:
            out+=ordinal(self.fibonacciNumber)+" fibonacci number\n"
        if self.tribonacci:
            out+=ordinal(self.tribonacciNumber)+" tribonacci number\n"
        if self.lucas:
            out+=ordinal(self.lucasNumber)+" lucas number\n"

        out+="Number Theory:\n"
        if self.perfect:
            out+="\tperfect number\n"
        if self.semiPerfect:
            out+="\tsemiPerfect\n"
        if self.weird:
            out+="\tweird number\n"
        if self.colossallyAbundant:
            out+="\tcolossally abundant number\n"
        if self.superAbundant:
            out+="\tsuper abundant number\n"
        if self.highlyAbundant:
            out+="\thighly abundant number\n"
        if self.abundant:
            out+="\tabundant number\n"
        if self.primitiveAbundant:
            out+="\tprimitive abundant\n"
        if self.deficient:
            out+="\tdeficient number\n"
        if len(self.primeFact)>1:
            out+="\tcomposite number\n"
        if self.highlyComposite:
            out+="\thighly composite number\n"
        if self.superiorHighlyComposite:
            out+="\tsuperior highly composite number\n"
        out+=("\n")
        
        if self.score!=-1:
            out+=("score:"+str(self.score))
        return out
        
    def getPrimeFactors(self):#returns nothing
        x=self.val
        k=0
        self.primeFact=[]#stores the list of indexes to primes of prime factors
        while x!=1:
            if x%primes[k]==0:
                x/=primes[k]
                self.primeFact.append(k)
            else:
                k+=1
        if len(self.primeFact)==1:
            self.prime=True
            l2=math.log(self.val+1)/math.log(2)#check for mersenne prime
            if(l2==int(l2)):
                self.mersenne=True
            else:
                self.mersenne=False
        else:
            self.prime=False

    def properDivisors(self):#returns the sum or proper divisors,the number of (non proper) divisors
        proper=1
        number=1
        uniquePrimes=[]
        for i in self.primeFact:
            unique=True
            for j in uniquePrimes:
                if j[0]==i:
                    unique=False
                    j[1]+=1
                    break
            if unique:
                uniquePrimes.append([i,1])
        for i in uniquePrimes:
            proper*=sum([primes[i[0]]**(j) for j in range(i[1]+1)])
            number*=i[1]+1
        proper-=self.val
        return proper,number
            
    def getScore(self):#produces an intrest score for the number and stores it
        self.score=0#returns score

        #prime stuff
        if self.prime:
            self.score+=10
            if self.mersenne:
                self.score+=1
        else:
            if self.poulet:
                self.score+=1
            if self.lucasPsudoprime:
                self.score+=1
                    
        #sequences
        if self.fibonacci:
            self.score+=1
            if self.tribonacci:
                self.score+=28
        if self.tribonacci:
            self.score+=1
        if self.lucas:
            self.score+=1
        #polygonal
        if self.polygonal!=[] and self.val!=1:
            self.score+=1.35**len(self.polygonal)

        #number theory

        #abundance
        abundanceScore=0
        if self.abundant:
            abundanceScore+=0.5
        if self.highlyAbundant:
            abundanceScore+=1
        if self.superAbundant:
            abundanceScore+=2
        if self.colossallyAbundant:
            abundanceScore+=4
        if self.primitiveAbundant:
            abundanceScore*=1.5
        self.score+=abundanceScore

        #compositeNess
        if self.highlyComposite:
            self.score+=1
        if self.superiorHighlyComposite:
            self.score+=10

        if self.perfect:
            self.score+=5
        if self.semiPerfect:
            self.score+=1
        if self.weird:
            self.score+=30
        if self.deficient:
            self.score+=1
        
        return self.score
            
def calcPrimeFactors():
    alert=0.001#the threashold to alert user of progress
    alertsGiven=0
    lt=time.time()#stores the last time in seconds that an alert was given
    averageTD=0#stores the average differnence in time since last alert
    for i in range(n):
        if(i/n>alert*alertsGiven):
            td=time.time()-lt
            averageTD=((averageTD*alertsGiven)+td)/(alertsGiven+1)
            print("computing prime factors-\t"+format(i/n*100,".3f")+"%\t"+format(td,".3f")+"-"+format(averageTD,".3f"))
            lt=time.time()
            alertsGiven+=1
        numbers.append(Number(i+1))
        numbers[i].getPrimeFactors()

def calcFib():
    a=1
    b=1
    c=2
    count=3
    numbers[0].fibonacci=False
    while c<n:
        numbers[c-1].fibonacci=True
        numbers[c-1].fibonacciNumber=count
        a=b
        b=c
        c=a+b
        count+=1

def calcLucas():
    out=[1,3]
    a=1
    b=3
    c=4
    count=3
    numbers[0].lucas=False
    while count<=n:
        if c<=n:
            numbers[c-1].lucas=True
            numbers[c-1].lucasNumber=count
        out.append(c)
        a=b
        b=c
        c=a+b
        count+=1
    return out

def calcTrib():
    count=4
    a=1
    b=1
    c=1
    d=3
    numbers[0].tribonacci=False
    while d<n:
        numbers[d-1].tribonacci=True
        numbers[d-1].tribonacciNumber=count
        a=b
        b=c
        c=d
        d=a+b+c
        count+=1

def getPolygonalName(x):#regurns a string of an x-sided polygonal
    specNames={3:"triangular",4:"square",9:"nonagonal",20:"icosagonal",120:"hecatonicosagonal",1000000:"megagonal"}
    if x in specNames.keys():
        return specNames[x]
    name="gonal"[::-1]
    if x>100000:
        return("fail")

    if x%100>=10 and x%100<20:
        name+="deca"[::-1]
        p={0:"",1:"hen",2:"do",3:"tri",4:"tetra",5:"penta",6:"hexa",7:"hepta",8:"octa",9:"ennea"}
        name+=p[x%10][::-1]
    else:
        p={0:"",1:"hen",2:"di",3:"tri",4:"tetra",5:"penta",6:"hexa",7:"hepta",8:"octa",9:"ennea"}
        name+=p[x%10][::-1]
        
    if x>=10:
        if(x%10!=0):
            name+="kai"[::-1]
        p={0:"",1:"",2:"icosi",3:"triaconta",4:"tetraconta",5:"pentaconta",6:"hexaconta",7:"heptaconta",8:"octaconta",9:"ennaconta"}
        t=(x//10)%10
        name+=p[t][::-1]
        
    if x>=100:
        p={0:"",1:"hecta",2:"dohecta",3:"triahecta",4:"tetrahecta",5:"pentahecta",6:"hexahecta",7:"heptahecta",8:"octahenta",9:"ennahecta"}
        t=(x//100)%10
        name+=p[t][::-1]
    if x>=1000:
        if((x//100)%10!=0):
            name+="kai"[::-1]
        p={0:"",1:"chilia",2:"dichilia",3:"trichilia",4:"tetrachilia",5:"pentachilia",6:"hexachilia",7:"heptachilia",8:"octachilia",9:"ennachilia"}
        t=(x//1000)%10
        name+=p[t][::-1]
        
    if x>=10000:
        if((x//100)%10!=0):
            name+="kai"[::-1]
        p={0:"",1:"myria",2:"dimyria",3:"trimyria",4:"tetramyria",5:"pentamyria",6:"hexamyria",7:"heptamyria",8:"octamyria",9:"ennamyria"}
        t=(x//10000)%10
        name+=p[t][::-1]

    return name[::-1]

def ordinal(n):
    if n%100>=4 and n%100%100<=20:
        return str(n)+"th"
    elif n%10==1:
        return str(n)+"st"
    elif n%10==2:
        return str(n)+"nd"
    elif n%10==3:
        return str(n)+"rd"
    else:
        return str(n)+"th"

def polygonal(s,q):
    out=(s-2)*(q**2)-(s-4)*q
    out/=2
    return int(out)

def calcPolynomials():
    levels=min([n,99999])
    threash=10000
    print("levels calculating:\t"+str(levels))
    for level in range(3,levels+1):
        if level%threash==0:
            print("-"*20)
            print("level:\t"+str(level))
        g=1
        q=1
        while g<n:
            numbers[g-1].polygonal.append([level,q])
            q+=1
            g=polygonal(level,q)
        if level%threash==0:
            print("up to-\t"+str(q))
            print("-"*20)

def devisorStuff():
    #load semiperfect numbers
    #because I have already calculated them
    with open("generatedSemiperfect.txt","r")as f:
        semiperfect=[int(i) for i in f.readlines()]
        for i in semiperfect:
            if i-1<n:
                numbers[i-1].semiPerfect=True
            else:
                break
    #load superiorHiglyComposite numbers
    #because they are tough to calculate and there aren't so many of them
    with open("superiorHighlyComposite.txt","r")as f:
        SHC=[int(i.split(" ")[1]) for i in f.readlines()]
        for i in SHC:
            if i-1<n:
                numbers[i-1].superiorHighlyComposite=True
            else:
                break
    #load colosallyAbundant numbers
    with open("colossallyAbundant.txt","r")as f:
        CA=[int(i.split(" ")[1]) for i in f.readlines()]
        for i in CA:
            if i-1<n:
                numbers[i-1].colossallyAbundant=True
            else:
                break
    #load colosallyAbundant numbers
    with open("primitiveAbundant.txt","r")as f:
        PA=[int(i.split(" ")[1]) for i in f.readlines()]
        for i in PA:
            if i-1<n:
                numbers[i-1].primitiveAbundant=True
            else:
                break
    
    alert=0.01#the threashold to alert user of progress
    alertsGiven=0
    lt=time.time()#stores the last time in seconds that an alert was given
    averageTD=0#stores the average differnence in time since last alert
    #trakers
    maxDiv=0#highest recorded sum of divisors
    superAbundantM=0#tracker for max(sigma(m)/m)
    maxNumDiv=1#tracker for the max number of divisors
    for i in range(n):
        if(i/n>alert*alertsGiven):
            td=time.time()-lt
            averageTD=((averageTD*alertsGiven)+td)/(alertsGiven+1)
            print("divisor stuff-\t"+format(i/n*100,".3f")+"%\t"+format(td,".3f")+"-"+format(averageTD,".3f"))
            lt=time.time()
            alertsGiven+=1
        div,numDiv=numbers[i].properDivisors()
        #check for highlyComposite
        if numDiv>maxNumDiv:
            numbers[i].highlyComposite=True
            maxNumDiv=numDiv
        #check for perfect
        if div==numbers[i].val:
            numbers[i].perfect=True
        #check for abundant
        elif div>numbers[i].val:
            numbers[i].abundant=True
            #check for weird
            if not numbers[i].semiPerfect:
                numbers[i].weird=True
        #check for higlyAbundant
        if div+numbers[i].val>=maxDiv:
            maxDiv=div+numbers[i].val
            numbers[i].highlyAbundant=True
        #check for defficent
        if div+numbers[i].val<numbers[i].val*2:
            numbers[i].deficient=True
        #check for superAbundant
        if (div+numbers[i].val)/numbers[i].val>superAbundantM:
            superAbundantM=(div+numbers[i].val)/numbers[i].val
            numbers[i].superAbundant=True

#baseConv only accepts int
def baseConv(x,y):#converts x to a list of base y didgits in reverse order e.x. base(10,2)=[0,1,0,1] or base(170,16)=[10,10]
    out=[]
    p=1
    while x>0:
        temp=x%(y**p)
        out.append(int(temp/(y**(p-1))))
        x-=temp
        p+=1
    return out[::-1]

def findHarshadNumbers():
    limit=50#base limiter for evaluating harshad Numbers
    alert=0.001#the threashold to alert user of progress
    alertsGiven=0
    lt=time.time()#stores the last time in seconds that an alert was given
    averageTD=0#stores the average differnence in time since last alert
    predictedEnd=(n**2)/2
    for i in range(n):
        num=numbers[i].val
        for j in range(2,limit+1):
            if num%sum(baseConv(num,j))==0:
                numbers[i].harshad.append(j)
        part=(i**2)/2
        if(part/predictedEnd>alert*alertsGiven):
            td=time.time()-lt
            try:
                averageTD=((averageTD*(alertsGiven-1))+td)/(alertsGiven)
            except:
                averageTD+=td
            print("harshad numbers-\t"+format(part/predictedEnd*100,".3f")+"%\t"+format(td,".3f")+"-"+format(averageTD,".3f")+"-"+str(i+1))
            lt=time.time()
            alertsGiven+=1
            
def fermatPsudoprime(a,b):#returns a boolean if b is a fermat psudoprime in base a
    if (a**(b-1)-1)%b==0:
        return True
    return False

def findPsudoprimes():
    alert=0.01#the threashold to alert user of progress
    alertsGiven=0
    lt=time.time()#stores the last time in seconds that an alert was given
    averageTD=0#stores the average differnence in time since last alert
    for i in range(n):
        if not numbers[i].prime:
            if fermatPsudoprime(2,numbers[i].val):
                numbers[i].poulet=True
            #if (lucasNumbers[i]-1)%numbers[i].val==0:
                #numbers[i].lucasPsudoprime=True
        if(i/n>alert*alertsGiven):
            td=time.time()-lt
            try:
                averageTD=((averageTD*(alertsGiven-1))+td)/(alertsGiven)
            except:
                averageTD+=td
            print("psudoprimes-\t"+format(i/n*100,".3f")+"%\t"+format(td,".3f")+"-"+format(averageTD,".3f")+"-"+str(i+1))
            lt=time.time()
            alertsGiven+=1
            
    numbers[0].poulet=False

def scoreNumbers():
    out=[]
    for i in numbers:
        out.append(i.getScore())

if __name__=="__main__":
    #important golbals
    
    numbers=[]#list of Number objects
    #note n at the top
    #note primes below

    #begin evaluations
    print("start computing primes")
    primes=getPrimes()
    print("end computing primes")
    print()
    print("calculating prime factors")
    calcPrimeFactors()#dependent on getPrimes
    print("end calculating prime factors")
    print()
    print("caculating sequences")
    calcFib()#threadable
    calcTrib()#threadable
    lucasNumbers=calcLucas()#threadable
    print("end calculating sequences")

    #polygonals
    print("calculation polygonals")
    calcPolynomials()#threadable
    print("end calculation polygonals")
    print()
    #divisor stuff
    print("starting divisor stuff")
    devisorStuff()#dependant of calcPrimeFactors
    #little fixes
    numbers[0].highlyComposite=True
    print("end divisor stuff")
    print()
    print("starting harshad numbers")
    findHarshadNumbers()#threadable
    print("finished harshad numbers")
    print()
    print("finding psudoprimes")
    findPsudoprimes()#threadable
    print("finished with psudoprimes")
    print()
    print("start scoreing")
    scores=scoreNumbers()#dependant on everything
    print("end scoreing")
