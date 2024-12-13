.mode table
/*
.headers on
.mode csv
.output data.csv
*/
/*
with here_before as ( 
select *
from
participations p
join fighters f on f.fighter_id = p.fighter_id
join categories c on p.category_id = c.category_id
join clubs cl on cl.club_id = f.club_id
where year != '2024'
)

select distinct(f.name), h.club_name, h.nationality, h.country
from
fighters f join here_before h on f.fighter_id = h.fighter_id
order by h.club_name
;
*/

/*
with hlo24 as (select name
from
participations p
join fighters f on f.fighter_id = p.fighter_id
join categories c on p.category_id = c.category_id
join clubs cl on cl.club_id = f.club_id
where year == '2024'),

hlo23 as (select name
from
participations p
join fighters f on f.fighter_id = p.fighter_id
join categories c on p.category_id = c.category_id
join clubs cl on cl.club_id = f.club_id
where year == '2023')
select count(distinct hlo23.name) from hlo23 join hlo24 on hlo23.name = hlo24.name 
;
*/

/*
select name, club_name, category_name, count(year)
from
participations p
join fighters f on f.fighter_id = p.fighter_id
join categories c on p.category_id = c.category_id
join clubs cl on cl.club_id = f.club_id
group by name, category_name
order by 3, 4;
*/

/*
select name, club_name, category_name, year
from
participations p
join fighters f on f.fighter_id = p.fighter_id
join categories c on p.category_id = c.category_id
join clubs cl on cl.club_id = f.club_id
where name like 'Sebastian Wil%'

;
*/

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
;
