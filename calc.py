#RPN CALCULATOR
# use ' ' to divide different integers
# use _ to indicate a minus number
import os
snum_lst = ['0','1','2','3','4','5','6','7','8','9']
num_lst = [0,1,2,3,4,5,6,7,8,9]
opr_lst = ['+','-','*','/','^','!']

stackL=[]
fL = []

def sPush(a):
	stackL.append(a)

def sPop():
	stackL.pop()

def opreate(sign):
	stklen = len(stackL)
	if sign == '+':
		reg = stackL[stklen-1] + stackL[stklen-2]
		sPop()
		sPop()
		sPush(reg)

	if sign == '-':
		reg = stackL[stklen-2] - stackL[stklen-1]
		sPop()
		sPop()
		sPush(reg)

	if sign == '*':
		reg = stackL[stklen-1] * stackL[stklen-2]
		sPop()
		sPop()
		sPush(reg)

	if sign == '/':
		reg = stackL[stklen-2] / stackL[stklen-1]
		sPop()
		sPop()
		sPush(reg)

	if sign == '^':
		reg = stackL[stklen-2] ** stackL[stklen-1]
		sPop()
		sPop()
		sPush(reg)

def parse(seq):
	glst = list(seq)
	tempstr = ''
	stklst = []
	for i in range(0,len(glst)):
		if glst[i] == '_':
			tempstr += '-'

		if glst[i] in snum_lst:
			#idx = snum_lst.index(glst[i])
			#glst[i] = num_lst[idx] 
			tempstr += glst[i]

		if glst[i] == ' ':
			#check tempstr
			if tempstr == '':
				pass
			else:
			 	stklst.append(int(tempstr))

			tempstr = ''

		if glst[i] in opr_lst:
			#check tempstr
			if tempstr == '':
				pass
			else:
			 	stklst.append(int(tempstr))
			stklst.append(glst[i])
			tempstr = ''

	return stklst

def calc(seq):

	lst = parse(seq)
	for i in lst:
		if str(type(i)) == "<class 'int'>":
			sPush(i)
		if i in opr_lst:
			opreate(i)

	return stackL[0]

if __name__ == '__main__':
	
	os.system('clear')
	print('--------------------------------\n')
	while True:
		a = input('RPNExpr:')
		if(a == 'END'):
			os.system('clear')
			break
		else:
			print('> '+str(calc(a)))
			del stackL
			stackL = []
			print('\n--------------------------------\n')


