from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()

# Assuming CONN and CURSOR are correctly initialized
Song.create_table()

hello = Song("hello", "adele")
hello.save()

despacito = Song("Despacito", "Vida")
despacito.save()

songs = CURSOR.execute('SELECT * FROM songs')
[row for row in songs]
