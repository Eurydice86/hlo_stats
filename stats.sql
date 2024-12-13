.mode table

    with hlo as (select name, year, category_name, country, club_name, nationality
    from
    participations p
    join fighters f on f.fighter_id = p.fighter_id
    join categories c on p.category_id = c.category_id
    join clubs cl on cl.club_id = f.club_id
    where year == 2014)
    select category_name as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    group by category_name
    union
    select 'Unique for 2014' as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    order by 2 desc, 1 desc
    ;

    with hlo as (select name, year, category_name, country, club_name, nationality
    from
    participations p
    join fighters f on f.fighter_id = p.fighter_id
    join categories c on p.category_id = c.category_id
    join clubs cl on cl.club_id = f.club_id
    where year == 2015)
    select category_name as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    group by category_name
    union
    select 'Unique for 2015' as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    order by 2 desc, 1 desc
    ;

    with hlo as (select name, year, category_name, country, club_name, nationality
    from
    participations p
    join fighters f on f.fighter_id = p.fighter_id
    join categories c on p.category_id = c.category_id
    join clubs cl on cl.club_id = f.club_id
    where year == 2016)
    select category_name as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    group by category_name
    union
    select 'Unique for 2016' as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    order by 2 desc, 1 desc
    ;

    with hlo as (select name, year, category_name, country, club_name, nationality
    from
    participations p
    join fighters f on f.fighter_id = p.fighter_id
    join categories c on p.category_id = c.category_id
    join clubs cl on cl.club_id = f.club_id
    where year == 2017)
    select category_name as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    group by category_name
    union
    select 'Unique for 2017' as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    order by 2 desc, 1 desc
    ;

    with hlo as (select name, year, category_name, country, club_name, nationality
    from
    participations p
    join fighters f on f.fighter_id = p.fighter_id
    join categories c on p.category_id = c.category_id
    join clubs cl on cl.club_id = f.club_id
    where year == 2018)
    select category_name as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    group by category_name
    union
    select 'Unique for 2018' as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    order by 2 desc, 1 desc
    ;

    with hlo as (select name, year, category_name, country, club_name, nationality
    from
    participations p
    join fighters f on f.fighter_id = p.fighter_id
    join categories c on p.category_id = c.category_id
    join clubs cl on cl.club_id = f.club_id
    where year == 2019)
    select category_name as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    group by category_name
    union
    select 'Unique for 2019' as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    order by 2 desc, 1 desc
    ;

    with hlo as (select name, year, category_name, country, club_name, nationality
    from
    participations p
    join fighters f on f.fighter_id = p.fighter_id
    join categories c on p.category_id = c.category_id
    join clubs cl on cl.club_id = f.club_id
    where year == 2020)
    select category_name as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    group by category_name
    union
    select 'Unique for 2020' as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    order by 2 desc, 1 desc
    ;

    with hlo as (select name, year, category_name, country, club_name, nationality
    from
    participations p
    join fighters f on f.fighter_id = p.fighter_id
    join categories c on p.category_id = c.category_id
    join clubs cl on cl.club_id = f.club_id
    where year == 2022)
    select category_name as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    group by category_name
    union
    select 'Unique for 2022' as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    order by 2 desc, 1 desc
    ;

    with hlo as (select name, year, category_name, country, club_name, nationality
    from
    participations p
    join fighters f on f.fighter_id = p.fighter_id
    join categories c on p.category_id = c.category_id
    join clubs cl on cl.club_id = f.club_id
    where year == 2023)
    select category_name as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    group by category_name
    union
    select 'Unique for 2023' as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    order by 2 desc, 1 desc
    ;

    with hlo as (select name, year, category_name, country, club_name, nationality
    from
    participations p
    join fighters f on f.fighter_id = p.fighter_id
    join categories c on p.category_id = c.category_id
    join clubs cl on cl.club_id = f.club_id
    where year == 2024)
    select category_name as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    group by category_name
    union
    select 'Unique for 2024' as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
    from hlo
    order by 2 desc, 1 desc
    ;
