def stats(year):
    query = f"""
    with hlo as (select name, year, category_name, country, club_name, nationality
    from
    participations p
    join fighters f on f.fighter_id = p.fighter_id
    join categories c on p.category_id = c.category_id
    join clubs cl on cl.club_id = f.club_id
    where year == {year})
    select category_name as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    group by category_name
    union
    select 'Unique for {year}' as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    order by 2 desc, 1 desc
    ;"""
    return query


if __name__ == "__main__":
    query = f".mode table\n"
    for year in [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2022, 2023, 2024]:

        query += stats(year) + "\n"
        with open("stats.sql", "w") as file:
            file.write(query)
