# Day 45 - Web Scraping with Beautiful Soup 

## What I Learned

Today I learned about **Web Scraping** using Python and the **Beautiful Soup (bs4) module**.

I also created a small project using web scraping to practice extracting information from a website.

The topics I learned today include:

- What is Web Scraping
- Beautiful Soup Module
- Parsing HTML
- Finding and extracting data from websites
- Working with HTML elements
- Building a small Web Scraping Project

---

#  What is Web Scraping?

**Web Scraping** is the process of automatically collecting or extracting information from websites.

Instead of manually copying information from a webpage, Python programs can request the webpage, read its HTML content, and extract the required information.

## 100 Movies that You Must Watch - PROJECT

# Objective

Scrape the top 100 movies of all time from a website. Generate a text file called `movies.txt` that lists the movie titles in ascending order (starting from 1). 
The result should look something like this:

```
1) The Godfather
2) The Empire Strikes Back
3) The Dark Knight
4) The Shawshank Redemption
... and so on
```
The central idea behind this project is to be able to use BeautifulSoup to obtain some data - like movie titles - from a website like Empire's (or from, say Timeout or Stacker that have curated similar lists). 

### ⚠️ Important: Use the Internet Archive's URL

Since websites change very frequently, **use this link** 
```
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
```
from the Internet Archive's Wayback machine. That way your work will match the solution video.

(Do *not* use https://www.empireonline.com/movies/features/best-movies-2/ which I've used in the screen recording)

