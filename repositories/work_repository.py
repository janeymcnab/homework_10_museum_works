from db.run_sql import run_sql

from models.museum import Museum
from models.work import Work
import repositories.museum_repository as museum_repository

# Write your functions here

def save(work):
    sql = "INSERT INTO works (title, artist, year, museum_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [work.title, work.artist, work.year, work.museum.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    work.id = id
    return work

def select_all():
    works = []

    sql = "SELECT * FROM works"
    results = run_sql(sql)

    for row in results:
        museum = museum_repository.select(row['museum_id'])
        work = Work(row['title'], row['artist'], row['year'], museum, row['id'])
        works.append(work)
    return works

def select(id):
    work = None
    sql = "SELECT * FROM works WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        museum = museum_repository.select(result['museum_id'])
        work = Work(result['title'], result['artist'], result['year'], museum, result['id'])
    return work