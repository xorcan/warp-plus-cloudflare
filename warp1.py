import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
import pathlib

script_version = '4.0.1.S+'
script_title   = f"[i] WARP-PLUS-CLOUDFLARE - ALIILAPRO / XORCAN (v{script_version})"
os.system('title ' + script_title if os.name == 'nt' else 'PS1="\[\e]0;' + script_title + '\a\]"; echo $PS1')
os.system('cls' if os.name == 'nt' else 'clear')
print ("---------------------------------------------------------------------------")
print ("[1] 1.1.1.1 için sınırsız WARP+ verisi (betik) - soran sürüm (S+)")
print ("---------------------------------------------------------------------------")
print ("[?] S; WARP+ kimliği (id) nasıl alınır?")
print ("[-] C; 1.1.1.1 uygulamasından: [ Ayarlar/Gelişmiş/Tanılamalar/Kimlik ]")
print ("[-] C; Bu yolu izleyip Kimlik kısmındaki koda basılı tutarak kopyalayın")
print ("---------------------------------------------------------------------------")
print ("[?] S; Daha açıklayıcı birşey yok mu?")
print ("[-] C; Birisi güzelce anlatmış: [ is.gd/birbir ]")
print ("---------------------------------------------------------------------------")
print ("[i] bu sürüm, kimlik girmenizi isteyerek çalışır.")
print ("[i] soru sormadan çalışan sürüm de mevcut: [warp2.py]")
print ("---------------------------------------------------------------------------")
print ("[i] aliilapro tarafından yazıldı [ aliilapro.github.io ]")
print ("[i] xorcan tarafından türkçeleştirildi [ github.com/xorcan ]")
print ("---------------------------------------------------------------------------")

def newID():
	while True:
		referrer  = input("[#] WARP+ Kimliğinizi girin:")
		user_input = input(f"[?] Kimliğinizin \"{referrer}\" olduğu doğru mu? (e/h):")
		if user_input == "e":
			save_id = input("[?] Kimliğinizi kaydetmek ister misiniz? (e/h):")
			if save_id == "e":
			    with open("warpkimlik.txt","w") as file:
				    file.write(referrer)
			    return referrer
			elif save_id == "h":
				return referrer
			else:
			    print(f"\"{save_id}\" geçerli bir parametre değil.")
		elif user_input == "h":
			user_input = None
		else:
			print(f"\"{user_input}\" geçerli bir parametre değil.")

def progressBar():
	animation     = ["[□□□□□□□□□□]","[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]"]
	progress_anim = 0
	save_anim     = animation[progress_anim % len(animation)]
	percent       = 0
	while True:
		for i in range(10):
			percent += 1
			sys.stdout.write(f"\r[+] İstek gönderiliyor... " + save_anim + f" %{percent}")
			sys.stdout.flush()
			if result.is_alive():
				time.sleep(0.1)
			else:
				time.sleep(0.005)
		progress_anim += 1
		save_anim = animation[progress_anim % len(animation)]
		if percent == 100:
			sys.stdout.write("\r[+] Yanıt alındı.         [■■■■■■■■■■] %100")
			break

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)	

def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)

url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'

from threading import Thread

class sendRequest(Thread):
	def run(self):
		try:
			install_id  = genString(22)
			body        = {"key": "{}=".format(genString(43)),
					"install_id": install_id,
					"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
					"referrer": referrer,
					"warp_enabled": False,
					"tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
					"type": "Android",
					"locale": "zh-CN"}
			data        = json.dumps(body).encode('utf8')
			headers     = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'}
			req         = urllib.request.Request(url, data, headers)
			response    = urllib.request.urlopen(req)
			status_code = response.getcode()
			self.status = status_code
		except Exception as error:
			self.status = error

if pathlib.Path("warpkimlik.txt").exists():
	while True:
		user_input = input("[?] Kaydedilmiş WARP+ kimliğini kullanmak ister misiniz? (e/h):")
		if user_input == "e":
			with open("warpkimlik.txt","r") as file:
				referrer = file.read().strip()
			break
		elif user_input == "h":
			referrer = newID()
			break
		else:
			print(f"\"{user_input}\" geçerli bir parametre değil.")
else:
	referrer = newID()

g = 0
b = 0
while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("")
	print(f"{script_title}")
	print("[w] github.com/xorcan/warp-plus-cloudflare")
	print("")
	result = sendRequest()
	result.start()
	print(f"[-] Üzerinde çalışılan kimlik: {referrer}")
	print(f"[#] Toplam: {g} Başarılı, {b} Başarısız.")
	print("")
	progressBar()
	if result.status == 200:
		g += 1
		print("")
		print(f"[#] {g} GB kullanım hakkı hesabınıza eklendi.")
		for i in range(18,0,-1):
			sys.stdout.write(f"\r[*] {i} saniye sonra yeni bir istek gönderilecek.")
			sys.stdout.flush()
			time.sleep(1)
	else:
		b += 1
		print(f"\n[#] Toplam: {g} Başarılı, {b} Başarısız.")
		print("")
		print("[#] Sunucuya bağlanırken hata oluştu: " + str(result.status))
		for i in range(18,0,-1):
			sys.stdout.write(f"\r[*] {i} saniye içinde tekrar deneniyor...")
			sys.stdout.flush()
			time.sleep(1)
