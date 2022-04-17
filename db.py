import sqlite3

conn = sqlite3.connect('test.db')
print("Opened/Created database success")

conn.execute('''CREATE TABLE Posts
         (UUID           TEXT,
         TEXT        TEXT    NOT NULL,
         IP                      TEXT);''')

# conn.execute("INSERT INTO ShortURL (REAL_URL,SHORT_URL) \
#       VALUES ('www.test.com', '32')");

cursor = conn.execute("SELECT * from Posts")

for item in cursor:
    print(item)

another = conn.execute("SELECT TEXT FROM Posts WHERE UUID=?", (321,))
print(another.fetchone())
conn.commit()

conn.close()