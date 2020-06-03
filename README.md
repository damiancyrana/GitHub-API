# GitHub-API
A simple application based on the Github API, its task is to obtain data on the popularity of top-rated repositories divided  by technology published on GitHub.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install request packets.
```bash
pip3 install requests
```

## URL
Original API url
```python
https://api.github.com/search/repositories?q=language:javascript&sort=stars'
```
Modified url for query handling for all programming languages
```python
programming_language = input("Choose programming language to check the most popular projects on GitHub: ")
url = f'https://api.github.com/search/repositories?q=language:{programming_language}&sort=stars'
```

Where **programming_language** it's for example: python, javascript, java etc.

## USAGE
[![asciicast](https://asciinema.org/a/urh4xtvoEcoizrNj4WYMAZ0UP.svg)](https://asciinema.org/a/urh4xtvoEcoizrNj4WYMAZ0UP)

## ROADMAP
New features in the future:
- Data visualization by [PyGal](http://www.pygal.org/en/stable/)
- Migration to [Flask](https://flask.palletsprojects.com/en/1.1.x/) aplication

## PROJECT STATUS
unfinished
