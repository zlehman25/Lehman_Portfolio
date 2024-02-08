# Poke API
This project was a way for me to start practicing creating python functions that send and retrieve data using an API. While not particularly interested in Pokemon, the [PokeAPI website](https://pokeapi.co/) was recommended to me by a friend because it is both free and has unlmited calls. 

### Included:
- API tools (Poke API)
- requests library
- json library
  
### Features:
- Performs an HTTP request and returns whether it was successful or not
- Saves response text to json variable
- Returns the name and type(s) of the pokemon in the 'current_team' variable

### Process:

I started the process by researching APIs and how to create requests within Python. The get_data function was the first one that I created and it started as a test to check the status code that I receive from a given URL. When I verified the request was operational the response text was then loaded into a variable that could be parsed for whatever information I wanted to reutrn. The get_name and get_type functions were then created to call the get_data function and return the names and types of the pokemon after iterating through the current_team list. 

### Learnings:
- Using an API
- Using the requests library
- Using the json library
- Calling functions within other functions
- Parsing json data

### Improvement:
- Expand on the information pulled
- Expand on the object-oriented functions
- Split the functions into two files - one to take user input (team) and one to request, parse, and return the information
