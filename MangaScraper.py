import os.path
import urllib
import urlparse
import requests
import ConfigParser
from bs4 import BeautifulSoup

mangaName = "one-piece"			# enter the part in []: http://www.mangapanda.com/[naruto]/618/2
saveMangaFolder = "/home/akd/Desktop/Workspace/MangaScraper/" + mangaName	#Save path on your system
mangaChapterMax = 2						#Last chapter to be crawled

mangaPage = ""
mangaChapter = 0
mangaSheet = 0
imageUrl = ""

def getMangaPageUrl ():
	global mangaPage
	mangaPage = "http://www.mangapanda.com/" + mangaName + "/" + str(mangaChapter) + "/" + str(mangaSheet)
	# print "Manga Page: " + mangaPage
	return mangaPage

def getHtmlPageForUrl ():
	return BeautifulSoup (urllib.urlopen(getMangaPageUrl()).read(), "html.parser")

def getMangaChapterName ():


def getImageUrlIfAvailable ():
	global imageUrl
	htmlPage = getHtmlPageForUrl()
	try:
		divImage = htmlPage.body.table.img['src']
		imageUrl = urlparse.urljoin(mangaPage, divImage)
		return True
	except AttributeError:
		print "Next Chapter!"
		return False

def getSavePath ():
	return os.path.join(saveMangaFolder, str(mangaChapter) + "-" + str(mangaSheet) + ".jpg")

def saveImageIntoJpeg ():		#some websites block urllib downloads, use saveFile instead
	print "Image Link: " + imageUrl
	savePath = getSavePath()
	print "Being saved into: " + savePath
	urllib.urlretrieve(imageUrl, savePath)

def saveFile (url):
	print "URL to be saved: " + url
	local_filename = getSavePath()
	r = requests.get(url)
	f = open(local_filename, 'wb')
	for chunk in r.iter_content(chunk_size=512 * 1024): 
		if chunk: # filter out keep-alive new chunks
			f.write(chunk)
	f.close()
	return 

# To download all the chapters, mention the last chapter number of the manga [mangaChapterMax (integer)]
for j in range(1, mangaChapterMax):
	for i in range(1, 100):
		mangaChapter = j
		mangaSheet = i
		if getImageUrlIfAvailable():
			saveFile(imageUrl)
			# saveImageIntoJpeg()
		else:
			break

print "All done! :)"
