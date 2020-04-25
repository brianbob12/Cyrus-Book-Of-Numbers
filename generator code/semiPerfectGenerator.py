m=1000000
semiPerfect=[]
with open("primitiveSemiperfect.txt","r") as f:
    primitives=[int(i.split(" ")[1]) for i in f.readlines()]

i=0
while primitives[i]<m:
    semiPerfect.append(primitives[i])
    j=primitives[i]*2
    while j<m:
        if not j in semiPerfect:
            semiPerfect.append(j)
        j+=primitives[i]
    i+=1

print(len(semiPerfect))
print("Done generating")
print()
print("starting sorting")
semiPerfect=sorted(semiPerfect)
print("done sorting")
print()
print("saving")
with open("generatedSemiperfect.txt","w") as f:
    for i in semiPerfect:
        f.write(str(i)+"\n")
print("done saving")
