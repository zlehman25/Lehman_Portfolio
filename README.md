# BookSoup 
This project was continued practice with creating python programs to automate tasks that interest me. In particular, I used the requests and BeautifulSoup libraries to scrape the New York Times best sellers website.

### Included:
- requests library
- Beautiful Soup (bs4) library
  
### Features:
- Performs HTTP requests scraping data from multiple web pages
- Saves the scraped text into different lists based on book genre, title, and author
- Decomposes and removes scraped data that is not needed in the output
- Prompts the user for input allowing them to choose a genre of book, returns the list of books and their authors based on the input

### Process:

The initial function was created just to scrape the different genre of best seller lists that were available on the New York Times website. After I could successfully identify which classes the text I wanted to scrape was located in, this data was pulled in and stored in the program. Since some of the data pulled was unrelated to the goal of the program, I decomposed it using the BeautifulSoup library to remove it from the output. The user was prompted for an input and if it matches one of the genres in the stored list, the program runs successfully. This 'genre_grabber' function was then placed inside of another Python function that uses the selected genre to navigate to the corresponding webpage with the best seller list of the selected genre. The same scraping and decomposing processes were performed and the user is presented with a list of best selling books. 

### Learnings:
- Webscraping with Beautiful Soup
- Using the requests library
- Nested Functions
- Zipping multiple lists into tuples

### Improvement:
- Expand on the information pulled - scrape more data related to the books
- With the scraped data transform it and do some sort of analysis
