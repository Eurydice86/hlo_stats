import event
import fighter
import club

import sqlite3
import sql_helpers
import database

import uuid
import json


def hlo_list():
    hlos = {
        2014: 13,
        2015: 7,
        2016: 1,
        2017: 55,
        2018: 1224,
        2019: 1401,
        2020: 1581,
        2022: 1714,
        2023: 1794,        
        2024: 1983,
        2025: 2279,
    }
    return hlos


def do_the_things(year, cursor):

    fighters_list, rating_dicts = event.event(f"/events/details/{hlos[year]}/", year)
    clubs = []

    fighter_dicts = []
    club_dicts = []
    category_dicts = []
    participation_dicts = []

    for competition in fighters_list:
        category_id = uuid.uuid4()
        competition_name = competition[0]
        category_dict = {
            "category_id": category_id,
            "category_name": competition_name,
            "year": year,
            "event": "Helsinki Longsword Open",
        }
        category_dicts.append(category_dict)

        counter = 0
        competition_clubs = []

        for f in competition[1:]:
            fighter_details = fighter.fighter(f"/fighters/details/{f}/")
            participation_dict = {
                "category_id": category_id,
                "fighter_id": fighter_details["fighter_id"],
            }
            participation_dicts.append(participation_dict)
            fighter_dicts.append(fighter_details)

            if fighter_details["club_id"]:
                competition_clubs.append(fighter_details["club_id"])
            counter += 1
            print(
                f"Processing {counter} of {len(competition)-1} participants in {competition_name} at HLO {year}: {fighter_details["name"]}."
            )
        competition_clubs = list(set(competition_clubs))
        clubs += competition_clubs
    clubs = list(set(clubs))

    for c in clubs:
        counter += 1
        club_details = club.club(f"/clubs/details/{c}/")
        club_dicts.append(club_details)

    for f in fighter_dicts:
        cursor.execute(sql_helpers.insert("fighters", f))

    for c in club_dicts:
        cursor.execute(sql_helpers.insert("clubs", c))

    for c in category_dicts:
        cursor.execute(sql_helpers.insert("categories", c))

    for c in participation_dicts:
        cursor.execute(sql_helpers.insert("participations", c))

    for c in rating_dicts:
        cursor.execute(sql_helpers.insert("ratings", c))

    

if __name__ == "__main__":

    conn = sqlite3.connect("data/hlo.db")
    cursor = conn.cursor()
    database.initialise(cursor)

    hlos = hlo_list()
    # hlo = 2016
    # do_the_things(hlo, cursor)
    for hlo in hlos.keys():
        do_the_things(hlo, cursor)

    conn.commit()
    conn.close()
