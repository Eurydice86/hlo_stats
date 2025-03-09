def stats(year):
    query = f"""
with hlo as (select name, year, category_name, country, club_name, nationality
from
participations p
join fighters f on f.fighter_id = p.fighter_id
join categories c on p.category_id = c.category_id
join clubs cl on cl.club_id = f.club_id
where year == {year} )
select category_name as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
from hlo
group by category_name
union
select 'Unique for {year}' as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
from hlo
order by 2 desc, 1 desc
;"""
    return query


def returning_all(latest):
    query = f"""
with hlo as (select f.fighter_id, name, year, category_name, country, club_name, nationality
from
participations p
join fighters f on f.fighter_id = p.fighter_id
join categories c on p.category_id = c.category_id
join clubs cl on cl.club_id = f.club_id)

select fighter_id, name, country, club_name, nationality from hlo
where year != {latest}

intersect

select fighter_id, name, country, club_name, nationality from hlo
where year = {latest}
;"""
    return query


def returning_from_last_year(latest, previous):
    query = f"""
with hlo as (select f.fighter_id, name, year, category_name, country, club_name, nationality
from
participations p
join fighters f on f.fighter_id = p.fighter_id
join categories c on p.category_id = c.category_id
join clubs cl on cl.club_id = f.club_id)

select fighter_id, name, country, club_name, nationality from hlo
where year = {previous}

intersect

select fighter_id, name, country, club_name, nationality from hlo
where year = {latest}
;"""
    return query



if __name__ == "__main__":
    query = f".mode table\n"
    years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2022, 2023, 2024]
    years = sorted(years)
    latest_year = years[-1]
    previous_year = years[-2]


    query += returning_all(latest_year) + "\n"
    query += returning_from_last_year(latest_year, previous_year) + "\n"
    query += stats(latest_year) + "\n"

    with open("stats.sql", "w") as out_file:
        out_file.write(query)
