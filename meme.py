import requests
from bs4 import BeautifulSoup as bs
import cowsay
import subprocess
import math
username = 'captain_cuckoo' #imgur account username
password = 'asdasdasd' #imgur account password

search = 'https://imgflip.com/memesearch?q='

#this existss only cause imgflip is a piece of shit who doesnt have the search integrated into their api
def SearchMeme(name):
	search = 'https://imgflip.com/memesearch?q='
	x = name.split()
	for i in range(len(x)):
		if i == 0:
			search = search + x[i]
		else:
			search = search + '+' + x[i]
	
	page = requests.get(search) 
	
	soup = bs(page.content, 'html5lib')
	
	s = soup.findAll('a') 
	
	links = []
	
	for i in s:
		links.append(i['href'])
	
	
	ids = []
	
	for i in links:
		x = i.split('/')
		for i in range(0,len(x)):
			if x[i] == "memetemplate":
				ids.append(x[i+1])



	try:

		print(ids)
		return ids[0]
	except:
		return "```template not found```"
	

#actually generates the meme using the imgflip api
def GenerateMeme(id,*args):



	URL = 'https://api.imgflip.com/caption_image'
	params = {
	    'username':username,
	    'password':password,
	    'template_id':id,
	    'text0':None,
	    'text1':None,
	}
	for i in range(0,len(args)):
		params['text'+str(i)] = args[i]
	print(params)
	response = requests.request('POST',URL,params=params).json()
	print(response)
	data = response['data']
	return(data['url'])


#just create the meme with the imgflip api cant add more than 2 texts cause their api is shit
def GetMeme(name,*args):
	id = SearchMeme(name)
	link = GenerateMeme(id,*args)
	return link
	
def SearchEmoji(name):
	search = 'https://api.kaomoji.moe/web/search?search='
	x = name.split()
	for i in range(len(x)):
		if i == 0:
			search = search + x[i]
		else:
			search = search + '+' + x[i]
	page = requests.get(search) 
	
	soup = bs(page.content, 'html5lib')
	s = soup.find('body').text 
	
	return(s)

#i dont know why i coded this im sorry
def generateUwU(input_text): 
      
    length = len(input_text) 
      
    output_text = '' 
      
    for i in range(length): 
          
        current_char = input_text[i] 
        previous_char = '&# 092;&# 048;'
          
        if i > 0: 
            previous_char = input_text[i - 1] 
          
        if current_char == 'L' or current_char == 'R': 
            output_text += 'W'
          
        elif current_char == 'l' or current_char == 'r': 
            output_text += 'w'
          
        elif current_char == 'O' or current_char == 'o': 
            if previous_char == 'N' or previous_char == 'n' or previous_char == 'M' or previous_char == 'm': 
                output_text += "yo"
            else: 
                output_text += current_char 
          
        else: 
            output_text += current_char 
  
    return output_text 

#BUNNY
def bunny(inStr):
	words = inStr.split(' ')
	signLen = max([len(x) for x in words])
	padLen = 0 if signLen >= 14 else math.floor((14 - signLen)/2)
	out = " " * padLen + '┌' + "─" * signLen + "┐\n"
	for i in words:
		out += " " * padLen + "│" + i.ljust(signLen, ' ') + "│\n"
	out += " " * padLen + "└" + "─" * signLen + """┘
(\__/) ││
(•ㅅ•) ││
/ 　 づ"""
	return out



print(bunny("this shit better work"))

#MOO
def GetCow(text):
	command = "python -m cowsay"+ " "+text
	proc = subprocess.run(command, shell=True, capture_output=True)
	x = proc.stdout.decode()
	return x




	
