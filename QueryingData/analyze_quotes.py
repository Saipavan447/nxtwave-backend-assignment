import sqlite3

connection = sqlite3.connect('quotes.db')
cursor = connection.cursor()
cursor.execute("SELECT COUNT(Quote) FROM Quotes INNER JOIN Author USING(QuoteID) GROUP BY AuthorName "
"SELECT MAX(tags),MIN(tags),AVG(tags) FROM Quotes INNER JOIN Tags USING(AuthorID)" 
"SELECT MAX(quotes) AS no_of_quotes FROM Quotes INNER JOIN Author USING(AuthorID) ORDER BY no_of_quotes DESC")
print(cursor.fetchall())
connection.commit()
connection.close()