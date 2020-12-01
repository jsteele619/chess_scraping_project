<h1>Welcome to my chess analysis project</h1>

<p1> The first part is the code in scrape_chess.py.ipynb. This code scrapes the chess.com site to pull the most recent game data directly from the html. Afterwards, I graph the result to show my progression in the last twenty games.</p1>
  
  https://github.com/jsteele619/chess_scraping_project/blob/main/templates/chessgraph.png

<p1> The next part is in the file "creating_the_master_df.iypnb". I make a series of API calls to the chess.com website. First, I input the username, and get a list of archived months in url format. This list contains every month I've played a chess game on chess.com.</p1>
  
<p1> Then I use the list of archived months, to loop through the master archive to collect the games. This came in a layered, complex json response. The process to combine all the games into a single list was complicated. Then after digging into the json response, the core data of 10-20 elements was contained in the same string. So I parsed through the string, created segments of the string, which I then called to further lists, which I then combined into a single dataframe, with each row containing all the information per game.</p1>

<p1> The information I collected in the dataframe includes: </p1>
  
<h4> Date, Time of Day played, 
  White player name, White Rating, White Result, 
  Black Name, Black Rating, Black Result, 
  Eco Name (refers to the opening moves), Eco Code (same), 
  URL, and PGN score (chess notation). </h4>
