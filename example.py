from cs50 import SQL

db = SQL('sqlite:///shows.db')

actor_name = input('Enter an actors name: ')

rows = db.execute('''SELECT title from shows
WHERE id IN (
    SELECT show_id FROM stars
    WHERE person_id = (
        SELECT id FROM people
        WHERE name = ?
    )
);''', actor_name)

print(rows)
