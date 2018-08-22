import os 

print ('''
         _           _                _     _ 
        | |         | |              | |   (_)
   __ _ | | __ __ _ | |_  ___  _   _ | | __ _ 
  / _` || |/ // _` || __|/ __|| | | || |/ /| |
 | (_| ||   <| (_| || |_ \__ \| |_| ||   < | |
  \__,_||_|\_\\__,_| \__||___/ \__,_||_|\_\|_|
                        
			By arleigh_burke ^_^                     
                                              
''')
print ('================================================')
print ('')
print (' [0] Information Gathering ')
print (' [1] Vulnerability Analysis')
print (' [2] Web Application analysis  ')
print (' [3] Password attacks  ')
print (' [4] Wireless Attack  ')
print (' [5] sniffing & spoofing  ')
print (' [6] Social Engineering  ')
print (' [7] Exit  ')
print ('')
i = input ('Select Your choise : ')
if i == 0 :
	print ('================================================')
	print (' [0] whois ')
	print (' [1] whatweb')
	print (' [2] nmap  ')
	print (' [3] dmitry  ')
	print (' [4] recon-ng  ')
	print (' [5] back')
	i1 = input ('Select Your Tool : ')
	if i1 == 0 :
		os.system('whois')
	else :
		print ('Tools not install Try to install ,')
	if i1 == 1 :
		os.system('whatweb')
	else:
		print ('Tools not install Try to install ,')
	if i1 == 2 :
		os.system('nmap')
	else:
		print ('Tools not install Try to install ,')
	if i1 == 3 :
		os.system('dmitry')
	else:
		print ('Tools not install Try to install ,')
	if i1 == 4 :
		os.system('recon-ng')
	else:
		print ('Tools not install Try to install ,')
	if i1 == 5 :
		print ('================================================')
		print ('')
		print (' [0] Information Gathering ')
		print (' [1] Vulnerability Analysis')
		print (' [2] Web Application analysis  ')
		print (' [3] Password attacks  ')
		print (' [4] Wireless Attack  ')
		print (' [5] sniffing & spoofing  ')
		print (' [6] Social Engineering  ')
		print (' [7] Exit  ')
		print ('')
	i = input ('Select Your choise : ')
if i == 1 :
	print ('================================================')
	print (' [0] golismero ')
	print (' [1] lynis ')
	print (' [2] nikto  ')
	print (' [3] nmap  ')
	print (' [4] unix-privesc-check  ')
	print (' [5] back')
	i1 = input ('Select Your Tool : ')
	if i1 == 0 :
		os.system('golismero')
	else:
		print ('Tools not install Try to install ,')
	if i1 == 1 :
		os.system('lynis')
	else:
		print ('Tools not install Try to install ,')
	if i1 == 2 :
		os.system('nikto')
	else:
		print ('Tools not install Try to install ,')
	if i1 == 3 :
		os.system('nmap')
	else:
		print ('Tools not install Try to install ,')
	if i1 == 4 :
		os.system('unix-privesc-check')
	else:
		print ('Tools not install Try to install ,')
	if i1 == 5 :
		print ('================================================')
		print ('')
		print (' [0] Information Gathering ')
		print (' [1] Vulnerability Analysis')
		print (' [2] Web Application analysis  ')
		print (' [3] Password attacks  ')
		print (' [4] Wireless Attack  ')
		print (' [5] sniffing & spoofing  ')
		print (' [6] Social Engineering  ')
		print (' [7] Exit  ')
		print ('')
	i = input ('Select Your choise : ')

