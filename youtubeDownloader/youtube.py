import urllib
import urllib2
from bs4 import BeautifulSoup
import youtube_dl

def getLink():
	margin = 50
	print '-' * margin
	query = raw_input('I want to download: ')
	print '-' * margin
	url = 'https://www.youtube.com/results?search_query=' + urllib.quote(query)
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html,'html.parser')
	l = list()
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
		if not vid['href'].startswith('https://googleads.g.doubleclick.net/'):
			l.append('https://www.youtube.com' + vid['href'])
	
	downloadVideo(l[0])

	
def downloadVideo(url):
	ydl_opts = {}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([url])
	
	
def main():
	print '1. Download Audio\n2.Download Video\n\n'
	choice = raw_input('Enter choice: ')
	if choice == '1':
	
	elif choice == '2':
		getLink()
	
	else:
		print 'Invalid choice'
		
if __name__ == '__main__':
	main()