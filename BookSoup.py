import requests
from bs4 import BeautifulSoup


def list_grabber():
    genre_pick = genre_grabber()
    genre_format = genre_pick.lower().replace(' ', '-') + '/'
    page = requests.get('https://www.nytimes.com/books/best-sellers/' + genre_format)

    
    if page.ok:
        soup = BeautifulSoup(page.text, 'html.parser')
        titles = []
        authors = []

        print(f'The Best-selling books in the {genre_pick} genre are: ')

        not_books = soup.findAll(True, {'class':['css-1817wkr', 'css-o8xfej']})
        for i in not_books:
            i.decompose()

        parent_titles = soup.find(class_ = 'css-46u0bd')
        titles_list = parent_titles.findAll('h3')
        parent_authors = soup.find(class_ = 'css-46u0bd')
        authors_list = parent_authors.findAll(class_='css-hjukut')

        for i in titles_list:
            titles.append(i.contents[0])

        for i in authors_list:
            authors.append(i.contents[0])

        combined = zip(titles, authors)
        print(tuple(combined))

    else:
        print('Request failed.')


def genre_grabber():
    page = requests.get('https://www.nytimes.com/books/best-sellers/')
    
    if page.ok:
        soup = BeautifulSoup(page.text, 'html.parser')
        genres = []

        drop = soup.findAll(True, {'class':['css-dk53ly', 'css-1dv1kvn, css-ok8je7']})
        for i in drop:
            i.decompose()

        genre_names = soup.find(itemscope_ = '')
        genres_list = genre_names.findAll(class_='css-nzgijy')

        for i in genres_list:
            genres.append(i.contents[0].string)
        
        print(f'The New York Times has several best seller lists. They are as follows: {genres}')
        
        while True:
            choice = input('Please choose one of the genres above: ')
            if choice in genres:
                return choice
                break
            else:
                print('Please try again, your genre was not listed above. ')
    else:
            print('Request failed.')


list_grabber()

