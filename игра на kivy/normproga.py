import pickle
import random

WordList=[]
file = 'file.pk'
with open(file, 'rb') as fi:
  WordList = pickle.load(fi)

#word =  random.choice(WordList)
choice_word=random.choice(WordList)

#def hint(self):

def check(word, get_word):
	bull=0
	cow=0
	listword = list(word.lower())
	listget_word = list(get_word.lower())
	second = []
	check=[]
	for i in range(len(listword)):
		if len(listword)>len(listget_word) or len(listword)<len(listget_word):
			pass
		else:
			if listword[i]==listget_word[i]:
				print(listword[i])
				bull+=1
				check.append(listget_word[i])
			elif listget_word[i] in listword:
				if listget_word[i] in second or listget_word[i] in check:
					pass
				else:
					second.append(listget_word[i])
					cow+=1
			else:
				pass
	return (cow,bull)
	
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist