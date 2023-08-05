#coding=utf-8
import os, sys, base64, time

r = '\033[1;31m'
h = '\033[1;32m'
k = '\033[1;33m'
b = '\033[1;34m'
u = '\033[1;35m'
c = '\033[1;36m'
p = '\033[1;0m'
def logo():
#	os.system("clear")
	print(r + '  ╬═════════════════════════════════════════════╬  ')
	print(p + ' ENCRYPT & DECRIPT BASE + AES256 + PASSWORD ')
	print(r + '  ╬═════════════════════════════════════════════╬  ')

def menu():
   logo()
   print(p + " Pembuat : Jengkolonline ")
   print(p + " Tujuan : Membasmi Kang Recode ")
   print(p + " 1.pembuka ")
   print(p + " 2.pengunci ")
   print(r + " ╬═════════════════════════════════════════════╬ ")
   pilih = raw_input(p + 'nomor : ')
   if pilih =="1":
      a = raw_input('file : ')
      print "masukan sandi script"
      try:
         os.system('cp ' + a + ' .dec.aes')
         os.system("openssl enc -aes-256-cbc -d -in .dec.aes -out .dec.py")
         with open('.dec.py','r') as c:
	   d = c.read()
	   e = base64.b64decode(str(d))
           eval(base64.b64decode(e))
           os.system('rm -rf .dec.py')
         try:
            os.system('python2 .dec.py && rm -rf .dec.py')
            a = raw_input(' coba gan :')
            print "masukan sandi anda"
         except KeyboardInterrupt:
             try:
                os.remove('.dec.py')
             except:
                 os.system('rm -rf .dec.py')
         except EOFError:
             try:
                os.remove('.dec.py')
             except:
                 os.system('rm -rf .dec.py')
      except:
          print('error')

   elif pilih =="2":
	a = raw_input('file : ')
	with open(a,'r') as c:
		d = c.read()
		e = base64.b64encode(d)
                g = 'import os, base64\nexec(base64.b64decode("' + e + '"))'
                f = open('.hd.py','w')
                f.write(g)
                f.close()
		os.system("openssl enc -aes-256-cbc -salt -in .hd.py -out croot.py")
                try:
                   os.remove('.hd.py')
                except:
                    os.system('rm -rf .hd.py')
   else:
       print('Pilihan tidak ada')
       time.sleep(1)
       menu()

menu()

