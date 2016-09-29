from random import randrange, choice

def write(f, text):
	f.write(text+'\n')

def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if not n % i:
            return False
    return True

def primenumber(fin, fou):
	for i in range(2, 10000):
		if isPrime(i):
			write(fou, str(i))
	fin.close()
	fou.close()

def primedistinction(fin, fou):
	for _ in range(100):
		n = randrange(10, 10000)
		write(fin, str(n))
		write(fou, (isPrime(n) and '1' or '0'))
	fin.close()
	fou.close()

def thenumberoffruits(fin, fou):
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
	action = ['a', 'm', 's']
	n = randrange(88, 99)
	write(fin, str(n))
	s = {}
	for _ in range(n):
		name = "".join([alpha[randrange(0, len(alpha))] for _ in range(randrange(5, 10))])
		count = randrange(0, 100)
		s[name] = count
		write(fin, name + ' ' + str(count))
	m = randrange(8888, 9999)
	write(fin, str(m))
	k = list(s)
	for _ in range(m):
		act = choice(action)
		command = [act]
		if act == 'a':
			tar = choice(k)
			command.append(tar)
			obj = randrange(-100, 100)
			command.append(str(obj))
			s[tar] += obj
		elif act == 'm':
			tar = choice(k)
			command.append(tar)
			obj = randrange(-100, 100)
			command.append(str(obj))
			s[tar] -= obj
		elif act == 's':
			tar = choice(k)
			command.append(tar)
			write(fou, str(s[tar]))
		write(fin, " ".join(command))

def webtooncrawler(fin, fou):
	from bs4 import BeautifulSoup as bs
	from urllib.request import urlopen
	url = 'http://comic.naver.com/webtoon/weekdayList.nhn?week='
	weeks = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

	n = randrange(10, 15)
	write(fin, str(n))
	for _ in range(n):
		query = choice(weeks)
		write(fin, query)
		res = urlopen(url + query)
		txt = bs(res, 'lxml')
		res.close()
		write(fou, ", ".join([ t.findAll('dt')[0].string for t in txt.body.findAll('div', {'class': 'list_area'})[0].findAll('li') ]))

	fin.close()
	fou.close()

problems = [
	primenumber,
	primedistinction,
	thenumberoffruits,
	webtooncrawler
]

def generate(pid, stamp):
	problems[pid](open(stamp + '.in', 'w'), open(stamp + '.vl', 'w'))