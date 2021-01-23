<h1>Welcome to my Chess Analysis</h1>

You can run this code to get user chess information from chess.com, and automatically print out relevant graph to visualize the users data.

<p1> Please input the username. The created dataframe saves to graphs/{username}.</p1>

<p1> For a technical explanation of the code, Python makes a series of API calls to the chess.com website with the input username. Python receives a list of archived months in url format. This list contains every month the user has played a chess game on chess.com.</p1>
  
<p1> The list of archived months is used to loop through the master archive to collect the games. This came in a complex, unsegmented json response. I wrote the code to parse through the json response for the appropriate data and format. I then combined the revelant information into a single dataframe, with each row representing all the information per single game.</p1>

<p1> From there, the data transfers to Postgres//Sql to query the data. In SQL, I can make the relevant queries to get the correct data format to be able to graph. Some of the questions I asked are, what time of day is the user more or less successful? What openings does the user play? How much success does the user have with each opening?</p1>

<p1> You can run the code yourself. Please make sure to make your own config.py file with the same format; login = ("username:password) </p1>
 
<h2> The information I collected in the dataframe includes: </h2>
  
<h4> * Date, and Time of Day played </h4>
 <h4> * White player name, White Rating, and White Result, </h4>
 <h4> * Black Name, Black Rating, and Black Result, </h4>
<h4>  * Eco Name (refers to the opening moves), and Eco Code (same), </h4>
 <h4>  * URL, and PGN score (chess notation). </h4>
 
<p1> Last but not least, and still to be done, I want to link a chess engine computer to python within jupyter notebook, to analyze every single move I've played. </p1>
