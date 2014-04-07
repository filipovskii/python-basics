import sqlite3


with sqlite3.connect(':memory:') as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE students(name, pl)')
    students = [('Kolya', 'javascript'), ('Vasya', 'brainfuck')]

    cursor.execute('BEGIN DEFERRED')
    cursor.executemany('INSERT INTO students VALUES (?, ?)', students)
    cursor.execute('''
        UPDATE students
        SET name="Ninja"
        WHERE pl="javascript"''')
    connection.commit()

    for row in cursor.execute('SELECT * from students'):
        print row
