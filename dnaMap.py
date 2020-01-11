import numpy as np
import math

X='CATGCCTAGTGGGCGTGGGTCTGATAGT'

Y='TGAAAAATGGATCACGGTGCTGGTTCGTTCAGTTACCGTATTGCTGTAGACGTCAGATTGCATGCCTAGGTTTTAGGTGTTGCTAGCAATACATGGAATAAATCACGTTGGCTGCTCCACGTTGTTGCTCGTTCCGGTTGCATGTGCACTATGGAAACGTCATTCTTCATGCCTAGTGGGCGTGGCAGTTG'

D=np.zeros((len(X)+1,len(Y)+1))

R=[['' for i in range(len(Y)+1)] for j in range(len(X)+1)]
for i in range(1,len(X)+1):
	R[i][0] = R[i-1][0]+'-'
for j in range(1,len(Y)+1):
	R[0][j] = R[0][j-1]+'+'
scq=0
result=''
for i in range(1,len(X)+1):
	for j in range(1,len(Y)+1):
		if X[i-1]==Y[j-1]:
			D[i,j]=D[i-1,j-1]+3
			R[i][j]=R[i-1][j-1]+'='
			if D[i,j]>scq:
				scq=D[i,j]
				result=R[i][j]
				
			
		else:
			D[i,j]=max(D[i-1,j]-1,D[i,j-1]-1,(D[i-1,j-1]+1))
			if D[i,j]==D[i-1,j-1]+1:
				R[i][j] = R[i-1][j-1]+"~"
			elif D[i,j]==D[i-1,j]-1:
				R[i][j] = R[i-1][j]+"-"
			else:
				R[i][j] = R[i][j-1]+"+"
print(result)
startPos=result.find('=')
pos=[]
bias=0
length=0
for i in range(startPos,len(result)):
	if result[i]=='=':
		pos.append(i-bias)
		length=length+1
	elif result[i]=='~':
		pos.append(i-bias)
		length=length+1
	elif result[i]=='-':
		pos.append(-1)
		bias=bias+1
		length=length+1

print(pos)
print(length)


'''for i in range(D.shape[0]):
	print(D[i])
for i in range(D.shape[0]):
	print(R[i])'''

