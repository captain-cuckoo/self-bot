import requests
from bs4 import BeautifulSoup as bs
import math
from googletrans import Translator



username = '' #imgflip account username
password = '' #imgflip account password

search = 'https://imgflip.com/memesearch?q='

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
}

lang = dict(map(reversed, LANGUAGES.items()))

#this existss only cause imgflip is a piece of shit who doesnt have the search integrated into their api
def SearchMeme(name):
	search = 'https://imgflip.com/memesearch?q='
	x = name.split()
	for i in range(len(x)):
		if i == 0:
			search = search + x[i]
		else:
			search = search + '+' + x[i]
	search = search + "&nsfw=on"
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
	    'text0':" ",
	    'text1':" ",
	}
	for i in range(0,len(args)):
		params['text'+str(i)] = args[i]
	response = requests.request('POST',URL,params=params).json()
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



#translate
def what(text):
	translator = Translator()
	translation = translator.translate(text)
	return translation.text


def s(l,text):
	translator = Translator()
	language = lang[l]
	translation = translator.translate(text,dest=language)
	return translation.text


print(s('german',"hello how are you"))


	
