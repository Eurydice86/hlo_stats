.mode table

with hlo as (select f.fighter_id, name, year, category_name, country, club_name, nationality
from
participations p
join fighters f on f.fighter_id = p.fighter_id
join categories c on p.category_id = c.category_id
join clubs cl on cl.club_id = f.club_id)

select fighter_id, name, country, club_name, nationality from hlo
where year != 2024

intersect

select fighter_id, name, country, club_name, nationality from hlo
where year = 2024
;

with hlo as (select f.fighter_id, name, year, category_name, country, club_name, nationality
from
participations p
join fighters f on f.fighter_id = p.fighter_id
join categories c on p.category_id = c.category_id
join clubs cl on cl.club_id = f.club_id)

select fighter_id, name, country, club_name, nationality from hlo
where year = 2023

intersect

select fighter_id, name, country, club_name, nationality from hlo
where year = 2024
;

with hlo as (select name, year, category_name, country, club_name, nationality
from
participations p
join fighters f on f.fighter_id = p.fighter_id
join categories c on p.category_id = c.category_id
join clubs cl on cl.club_id = f.club_id
where year == 2024 )
select category_name as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
from hlo
group by category_name
union
select 'Unique for 2024' as 'Competition', count(distinct name) as 'Participants', count(distinct club_name) as 'Clubs', count(distinct nationality) as 'Nationalities'
from hlo
order by 2 desc, 1 desc
;
