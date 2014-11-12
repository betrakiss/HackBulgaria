import sqlite3
from copy import deepcopy


class ReservationSystem:
    MAX_SEATS = 100

    def __init__(self):
        self.database = None
        self.cursor = None

        self.cinema_hall = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                            ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

        self.create_databases()

    def create_databases(self):
        self.database = sqlite3.connect('movies.db')
        self.cursor = self.database.cursor()

        self.cursor.execute('PRAGMA foreign_keys=ON')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
            Movies(id INTEGER PRIMARY KEY, name TEXT, rating REAL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
            Projections(id INTEGER PRIMARY KEY, movie_id INTEGER, type TEXT, date TEXT, time TEXT,
            FOREIGN KEY(movie_id) REFERENCES Movies(id))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS
            Reservations(id INTEGER PRIMARY KEY, username TEXT, projection_id INTEGER,
            row INTEGER, col INTEGER, FOREIGN KEY(projection_id) REFERENCES Projections(id))''')

    def fill_movies(self):
        self.add_movie('The Hunger Games: Catching Fire', 7.9)
        self.add_movie('Wreck-It Ralph', 7.8)
        self.add_movie('Her', 8.3)

    def fill_projections(self):
        self.add_projection(1, '3D', '2014-04-01', '19:10')
        self.add_projection(1, '2D', '2014-04-01', '19:00')
        self.add_projection(1, '4DX', '2014-04-02', '21:00')
        self.add_projection(3, '2D', '2014-04-05', '20:20')
        self.add_projection(2, '3D', '2014-04-02', '22:00')
        self.add_projection(2, '2D', '2014-04-02', '19:30')

    def fill_reservations(self):
        self.add_reservation('RadoRado', 1, 2, 1)
        self.add_reservation('RadoRado', 1, 3, 5)
        self.add_reservation('RadoRado', 1, 7, 8)
        self.add_reservation('Ivo', 3, 1, 1)
        self.add_reservation('Ivo', 3, 1, 2)
        self.add_reservation('Mysterious', 5, 2, 3)
        self.add_reservation('Mysterious', 5, 2, 4)

    def add_movie(self, name, rating):
        self.cursor.execute('INSERT INTO Movies(name, rating) VALUES(?, ?)', (name, rating))
        self.database.commit()

    def add_projection(self, movie_id, type, date, time):
        self.cursor.execute('''INSERT INTO Projections(movie_id, type, date, time)
            VALUES(?, ?, ?, ?)''', (movie_id, type, date, time))
        self.database.commit()

    def add_reservation(self, username, projection_id, row, col):
        self.cursor.execute('''INSERT INTO Reservations(username, projection_id, row, col)
            VALUES(?, ?, ?, ?)''', (username, projection_id, row, col))
        self.database.commit()

    def remove_movie(self, name):
        self.cursor.execute('DELETE FROM Movies WHERE name = ?', (name,))
        self.database.commit()

    def show_movies(self):
        movies = self.cursor.execute('SELECT * FROM Movies ORDER BY rating DESC')

        for movie in movies:
            print('[{}] - {} ({})'.format(movie[0], movie[1], movie[2]))

    def make_reservation(self):
        name = input('Input name > ')
        tickets = input('Number of tickets > ')

        print('Current Movies: ')
        self.show_movies()

        choice = input('Choose a movie > ')
        movie_name = self.cursor.execute('SELECT name FROM Movies WHERE ? = id', (choice,)).fetchone()[0]

        print('Projections for {}: '.format(movie_name))
        projections = self.cursor.execute('SELECT id, date, time, type FROM Projections WHERE movie_id = ?',
                                          (choice,))
        for proj in projections:
            #slots = self.cursor.execute('SELECT Projections. )
            print('[{}] - {} {} ({})'.format(proj[0], proj[1], proj[2], proj[3]))

    #def go(self):


ReservationSystem().make_reservation()
