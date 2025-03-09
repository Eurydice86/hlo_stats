.mode table

/*
with latest_plus_any_hlo as (
with hlo as (select f.fighter_id, name, year, category_name, country, club_name, nationality
from
participations p
join fighters f on f.fighter_id = p.fighter_id
join categories c on p.category_id = c.category_id
join clubs cl on cl.club_id = f.club_id)

select fighter_id, name, category_name, country, club_name, nationality from hlo
where year != 2024

intersect

select fighter_id, name, category_name, country, club_name, nationality from hlo
where year = 2024)

select * from latest_plus_any_hlo
order by fighter_id
;



with last_2_hlos as (
with hlo as (select f.fighter_id, name, year, category_name, country, club_name, nationality
from
participations p
join fighters f on f.fighter_id = p.fighter_id
join categories c on p.category_id = c.category_id
join clubs cl on cl.club_id = f.club_id)

select fighter_id, name, category_name, country, club_name, nationality from hlo
where year = 2023

intersect

select fighter_id, name, category_name, country, club_name, nationality from hlo
where year = 2024)

select * from last_2_hlos
order by fighter_id
;

*/

with hlo22 as(
with hlo as (select distinct f.fighter_id, name, year, category_name, country, club_name, nationality
from
participations p
join fighters f on f.fighter_id = p.fighter_id
join categories c on p.category_id = c.category_id
join clubs cl on cl.club_id = f.club_id)

select fighter_id, name from hlo
where year = 2022),


hlo23 as(
with hlo as (select distinct f.fighter_id, name, year, category_name, country, club_name, nationality
from
participations p
join fighters f on f.fighter_id = p.fighter_id
join categories c on p.category_id = c.category_id
join clubs cl on cl.club_id = f.club_id)

select fighter_id, name from hlo
where year = 2023)

select distinct hlo23.fighter_id, hlo23.name from hlo23
left join hlo22
on hlo23.fighter_id = hlo22.fighter_id
where hlo22.fighter_id is not null 
