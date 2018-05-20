#!/usr/bin/python

from bs4 import BeautifulSoup
import requests

movies, ratings = None, None


def parse_imdb():
    global movies, ratings
    movies = list()
    ratings = list()
    temp = list()
    url = "http://www.imdb.com/chart/top"
    data = requests.get(url)
    response = data.text
    soup = BeautifulSoup(response, "html.parser")

    for item in soup.findAll("td"):
        if item.has_attr("class"):
            l = item.get("class")
            if l[0] == "titleColumn":
                name = item.text.strip()
                name = name.split("\n")
                name[0] = name[0].replace(".", "")
                name[1] = name[1].strip(" \n.")
                name[2] = name[2].strip("()")
                movies.append(name)

            if l[0] == "ratingColumn":
                star = item.text
                star = star.strip()
                temp.append(star)

    for i, v in enumerate(temp):
        if i % 2 == 0:
            ratings.append(v)


def suggest_movie(year):
    global movies, ratings
    parse_imdb()
    temp = list()
    mlen = list()
    count = 0
    print
    for index, movie in enumerate(movies):
        if movie[2] == year:
            count = 1
            item = movie[1] + " (" + ratings[index] + ")"
            mlen.append(len(item))
            temp.append(item)
    if not count:
        print "Sorry! No such movie available"
    else:
        ch = max(mlen)
        print ch * "-"
        for item in temp:
            print item
        print ch * "-"
    print


def suggest_movie_rated(min_rate, max_rate):
    global ratings, movies
    parse_imdb()
    temp = list()
    mlen = list()
    count = 0
    print
    for index, rating in enumerate(ratings):
        if float(rating) < float(min_rate) or float(rating) > float(max_rate):
            continue
        count = 1
        item = movies[index][1] + " (" + ratings[index] + ")"
        mlen.append(len(item))
        temp.append(item)
    if not count:
        print "Sorry! No such movie available"
    else:
        ch = max(mlen)
        print ch * "-"
        for item in temp:
            print item
        print ch * "-"
    print


def main():
    inp = raw_input('1. Search movie by year\n2. Search movie by ratings\n\nEnter Choice: ')
    if inp == '1':
	    year = raw_input('Enter year: ')
	    suggest_movie(year)
    
    elif inp == '2':
        minRate = raw_input('Enter minimum rating: ')
        maxRate = raw_input('Enter maximum rating: ')
        suggest_movie_rated(minRate, maxRate)		
	
    else:
        print 'Incorrect Choice!!!\n'	
		
if __name__ == '__main__':
    main()
	
