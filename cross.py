import random 
word1='aaaaaabbbbbb'
word2='ccccccdddddd'
word1=list(word1)
word2=list(word2)

rand = random.randint(1, 10)
cross1=[]
cross2=[]
cross1.extend(word2[0:rand])
cross1.extend(word1[rand:len(word1)])
cross2.extend(word1[0:rand])
cross2.extend(word2[rand:len(word2)])

print ''.join(cross1)
print ''.join(cross2)