hints=[]
words=[]
import os;

def addhint():
	give=raw_input('any hint?: ')
	if(give==''):
		checkDes(False)
	else:
		print('insert '+give+' ...')
		hints.append(give)

		checkDes(True)
	

def checkDes(stat):
	if (stat):
		print(len(hints))
		addhint();
	else:
		os.system('clear');
		addword()




def addword():
	give=raw_input('any word?: ')
	if(give==''):
		checkWdes(False)
	else:
		print('insert '+give+' ...')
		words.append(give)

		checkWdes(True)

def creatpass():
	give=raw_input('name of the wordlist? (default: passList.txt): ');
	if (give==''):
		f=open('passList.txt','w');
		give='passList'
	else:
		f=open(give+'.txt','w');
	
	import datetime
	x = datetime.datetime.now()
	f.write('#created on '+str(x)+' .'+'\n');
	f.close();
	
	print('starting ...');
	x=0;

	f=open(give+'.txt','a');
	for hint in hints:
		for year in range(1962,2020):
			x += 1
			f.write(hint+str(year)+'\n')
			f.write(hint+str(year)+str(year)+'\n')
			f.write(hint+str(year)+'\n')
			f.write(hint+str(year)+str(year)+'\n')

			f.write(hint.capitalize()+str(year)+'\n')
			f.write(hint.capitalize()+str(year)+str(year)+'\n')
			f.write(hint.capitalize()+str(year)+'\n')
			f.write(hint.capitalize()+str(year)+str(year)+'\n')

			f.write((hint.capitalize()+str(year)+'\n').upper())
			f.write((hint.capitalize()+str(year)+str(year)+'\n').upper())
			f.write((hint.capitalize()+str(year)+'\n').upper())
			f.write((hint.capitalize()+str(year)+str(year)+'\n').upper())
	
	
	print('10% ...');

	for hint in hints:
		x += 1
		f.write(hint+'\n')
		f.write(hint.capitalize()+'\n')

    		f.write((hint+'\n').upper())
		f.write((hint.capitalize()+'\n').upper())

	print('15% ...');

	for word in words:
		x += 1
		f.write(word+'\n')
	print('18% ...');

	for hint in range(len(hints)):
		for hint2 in range(len(hints)):
			x += 1


			f.write(hints[hint]+hints[hint2]+'\n')
			f.write(hints[hint].capitalize()+hints[hint2]+'\n')
			f.write(hints[hint].capitalize()+hints[hint2].capitalize()+'\n')


			f.write((hints[hint]+hints[hint2]+'\n').upper())
			f.write((hints[hint].capitalize()+hints[hint2]+'\n').upper())
			f.write((hints[hint].capitalize()+hints[hint2].capitalize()+'\n').upper())

			if(len(hints)>hint2+1):

				f.write(hints[hint]+hints[hint2]+hints[hint2+1]+'\n')
				f.write(hints[hint].capitalize()+hints[hint2]+hints[hint2+1]+'\n')
				f.write(hints[hint].capitalize()+hints[hint2].capitalize()+hints[hint2+1]+'\n')
				f.write(hints[hint].capitalize()+hints[hint2]+hints[hint2+1].capitalize()+'\n')	


				f.write((hints[hint]+hints[hint2]+hints[hint2+1]+'\n').upper())
				f.write((hints[hint].capitalize()+hints[hint2]+hints[hint2+1]+'\n').upper())
				f.write((hints[hint].capitalize()+hints[hint2].capitalize()+hints[hint2+1]+'\n').upper())
				f.write((hints[hint].capitalize()+hints[hint2]+hints[hint2+1].capitalize()+'\n').upper())	

			for word in range(len(words)):

				f.write(hints[hint]+hints[hint2]+words[word]+'\n')
				f.write(hints[hint].capitalize()+hints[hint2]+words[word]+'\n')
				f.write(hints[hint].capitalize()+hints[hint2].capitalize()+words[word]+'\n')


				f.write((hints[hint]+hints[hint2]+words[word]+'\n').upper())
				f.write((hints[hint].capitalize()+hints[hint2]+words[word]+'\n').upper())
				f.write((hints[hint].capitalize()+hints[hint2].capitalize()+words[word]+'\n').upper())

				if(len(hints)>hint2+1):

					f.write(hints[hint]+hints[hint2]+hints[hint2+1]+words[word]+'\n')
					f.write(hints[hint].capitalize()+hints[hint2]+hints[hint2+1]+words[word]+'\n')


					f.write((hints[hint]+hints[hint2]+hints[hint2+1]+words[word]+'\n').upper())
					f.write((hints[hint].capitalize()+hints[hint2]+hints[hint2+1]+words[word]+'\n').upper())

			for word in range(len(words)):
				for year in range(1962,2020):
					f.write(hints[hint]+hints[hint2]+words[word]+str(year)+'\n')
					f.write(hints[hint]+hints[hint2]+str(year)+words[word]+'\n')

          				f.write((hints[hint]+hints[hint2]+words[word]+str(year)+'\n').upper())
					f.write((hints[hint]+hints[hint2]+str(year)+words[word]+'\n').upper())

					f.write(hints[hint].capitalize()+hints[hint2]+words[word]+str(year)+'\n')
					f.write(hints[hint].capitalize()+hints[hint2].capitalize()+str(year)+words[word]+'\n')
					if(len(hints)>hint2+1):
						f.write(hints[hint]+hints[hint2]+hints[hint2+1]+words[word]+str(year)+'\n')
						f.write(hints[hint].capitalize()+hints[hint2]+hints[hint2+1]+words[word]+str(year)+'\n')
						f.write(hints[hint].capitalize()+hints[hint2].capitalize()+hints[hint2+1].capitalize()+words[word].capitalize()+str(year)+'\n')

            					f.write((hints[hint]+hints[hint2]+hints[hint2+1]+words[word]+str(year)+'\n').upper())
						f.write((hints[hint].capitalize()+hints[hint2]+hints[hint2+1]+words[word]+str(year)+'\n').upper())
						f.write((hints[hint].capitalize()+hints[hint2].capitalize()+hints[hint2+1].capitalize()+words[word].capitalize()+str(year)+'\n').upper())

	print('70% ...');
	for hint in hints:
		for word in words:
			x += 1
			f.write(hint+str(word)+'\n')
			f.write(str(word)+hint+'\n')
			f.write(hint+str(word)+str(word)+'\n')

			f.write(hint.capitalize()+str(word)+'\n')
			f.write(str(word)+hint.capitalize()+'\n')
			f.write(hint.capitalize()+str(word)+str(word)+'\n')


			f.write((hint.capitalize()+str(word)+'\n').upper())
			f.write((str(word)+hint.capitalize()+'\n').upper())
			f.write((hint.capitalize()+str(word)+str(word)+'\n').upper())

	print('80% ...');
	for hint in hints:
		for word in words:
			x += 1
			
			f.write(hint+str(word)+'\n')
			f.write(hint+str(word)+str(word)+'\n')
			f.write(hint.capitalize()+str(word)+'\n')
			f.write(hint.capitalize()+str(word)+str(word)+'\n')

      			f.write((hint+str(word)+'\n').upper())
			f.write((hint+str(word)+str(word)+'\n').upper())
			f.write((hint.capitalize()+str(word)+'\n').upper())
			f.write((hint.capitalize()+str(word)+str(word)+'\n').upper())

	print('90% ...');
	for hint in hints:
		for word in words:
			for year in range(1962,2020):
				x += 1
				
				f.write(hint+word+str(year)+'\n')
				f.write(hint+word+word+str(year)+'\n')
				f.write(hint+word+str(year)+str(year)+'\n')


				f.write((hint+word+str(year)+'\n').upper())
				f.write((hint+word+word+str(year)+'\n').upper())
				f.write((hint+word+str(year)+str(year)+'\n').upper())

				f.write(hint.capitalize()+word+str(year)+'\n')
				f.write(hint.capitalize()+word+word+str(year)+'\n')
				f.write(hint.capitalize()+word+str(year)+str(year)+'\n')
	print('100% ...');
	
	print('successfully Generated! \n ['+str(x)+' words created]');
	

def checkWdes(stat):
	if (stat):
		print(len(words))
		addword();
	else:
		os.system('clear');
		print('Generating passwords ...');
		creatpass()
addhint()

