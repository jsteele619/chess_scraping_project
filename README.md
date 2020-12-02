<h1>Welcome to my chess analysis project</h1>

<p1> The first part is the code in scrape_chess.py.ipynb. This code scrapes the chess.com site to pull the most recent game data directly from the html. Afterwards, I graph the result to show my progression in the last twenty games.</p1>
  
  https://github.com/jsteele619/chess_scraping_project/blob/main/templates/chessgraph.png

<p1> The next part is in the file "creating_the_master_df.iypnb". I make a series of API calls to the chess.com website. First, I input the username, and get a list of archived months in url format. This list contains every month I've played a chess game on chess.com.</p1>
  
<p1> Then I use the list of archived months, to loop through the master archive to collect the games. This came in a layered, complex json response. The process to combine all the games into a single list was complicated. Then after digging into the json response, the core data of 10-20 elements was contained in the same string. So I parsed through the string, created segments of the string, which I then called to further lists, which I then combined into a single dataframe, with each row containing all the information per game.</p1>

<p1> The information I collected in the dataframe includes: </p1>
  
<h4> Date, and Time of Day played </h4>
 <h4> White player name, White Rating, and White Result, </h4>
 <h4> Black Name, Black Rating, and Black Result, </h4>
<h4>  Eco Name (refers to the opening moves), and Eco Code (same), </h4>
 <h4>  URL, and PGN score (chess notation). </h4>

<p1> I saved this created dataframe to "master_df.csv". <p1>
<p1> From there, I transferred the data to Postgres//Sql to query the data. First I created the table, and then imported the data. In SQL, I can make complicated queries to find out trends from the entire database of chessgames. Some questions I want to answer are; do I play better during certain parts of the day? Do I have certain openings that I play better against? And I would like to graph various results as well. </p1>

<p1> Last but not least, and still to be done, I want to link a chess engine computer to python within jupyter notebook, and analyze every single move I've played. Part of the data cleaning process was getting the PGN score into a computer readable format. With the chess engine, I can find further answers to my skill. </p1>
