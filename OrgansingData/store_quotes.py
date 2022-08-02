import sqlite3

connection = sqlite3.connect(r'quotes.db')

cursor = connection.cursor()
  

cursor.executescript('''
CREATE TABLE Quotes(
QuoteID INTEGER NOT NULL,
Quote TEXT NOT NULL,
PRIMARY KEY(QuoteID)
);
  
CREATE TABLE Author(
AuthorID NUMERIC NOT NULL,
AuthorName NUMERIC NOT NULL,
QuoteID INTEGER,
FOREIGN KEY(QuoteID) REFERENCES Advisor(QuoteID),
PRIMARY KEY(AuthorID)
);
CREATE TABLE Tags(
TagsID NUMERIC NOT NULL,
Tages NUMERIC NOT NULL,
AuthorID INTEGER,
FOREIGN KEY(AuthorID) REFERENCES Advisor(AuthorID),
PRIMARY KEY(TagsID)
);
''')
  
connection.commit()
  
connection.close()