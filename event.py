import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import uuid

import json


def event(link, year):
    event_id = link.split("/")[-2]
    full_url = "https://hemaratings.com" + link
    page = requests.get(full_url)

    soup = BeautifulSoup(page.text, features="lxml")

    if soup.find("h1"):
        if soup.find("h1").text.strip() == "Service Unavailable":
            print(f"Event {link} not found!")
            return

    sp = soup.find("div", id="main")
    event_name = sp.find("h2").text.strip()

    metadata_div = sp.find("div", class_="row")
    metadata_table = metadata_div.find_all("td")

    metadata = []

    for m in metadata_table:
        metadata.append(m.text.strip())

    month_name = metadata[1].split(" ")[0].strip()

    date_object = datetime.strptime(month_name, "%B")
    month_number = date_object.month

    day = metadata[1].split(" ")[1].strip()
    date = f"{day}/{month_number}/{year}"
    country = metadata[3].strip()
    state = None
    city = None
    if len(metadata) < 10:
        city = metadata[5].strip()
    if len(metadata) == 10:
        state = metadata[5].strip()
        country = metadata[3].strip()
        city = metadata[7].strip()

    event_dict = {
        "event_id": event_id,
        "event_name": event_name,
        "date": date,
        "country": country,
        "state": state,
        "city": city,
    }

    tournaments = sp.find_all("div", {"id": re.compile("heading_tournament_*")})
    ratings = sp.find_all("div", {"id": re.compile("heading_rating_*")})

    all_fighters = []
    rating_dicts = []
    for t in tournaments:
        competition = t.find("span").text.strip()
        competition = competition.split(" - ")[0]
        competition_id = uuid.uuid4()
        competition_dict = {
            "competition_id": competition_id,
            "competition_name": competition,
            "event_id": int(event_id),
        }
        category_fighters = []

        category_table = t.find_next("table")
        rows = category_table.find_all("tr")
        rows = rows[1:]

        for r in rows:
            entries = r.find_all("td")
            stage = entries[0].text.strip()

            fighter_1 = entries[1]
            if fighter_1.find("a"):
                fighter_1_id = fighter_1.find("a")["href"].split("/")[-2]
            else:
                fighter_1_id = None
            fighter_2 = entries[2]
            if fighter_2.find("a"):
                fighter_2_id = fighter_2.find("a")["href"].split("/")[-2]
            else:
                fighter_2_id = None
            category_fighters.append(int(fighter_1_id))
            category_fighters.append(int(fighter_2_id))
        category_fighters = sorted(list(set(category_fighters)))
        category_fighters.insert(0, competition)
        all_fighters.append(category_fighters)

    for rt in ratings:
        rating = rt.find("span").text.strip().split(" - ")[0]

        rating_table = rt.find_next("table")
        rows = rating_table.find_all("tr")
        rows = rows[1:]

        for r in rows:
            entries = r.find_all("td")
            rank = entries[0].text.strip()
            rank_change = entries[1].text.strip()
            if rank_change == "":
                rank_change = "0"
            if entries[1].find("i", {"title": re.compile("Dropped*")}):
                rank_change = "-" + rank_change

            rank_before = int(rank) - int(rank_change)

            fighter = entries[2]
            if fighter.find("a"):
                fighter_id = fighter.find("a")["href"].split("/")[-2]
            else:
                fighter_id = None

            w_rating = float(entries[5].text.strip())
            change = entries[6].text.strip()
            if change == "":
                change = "0.0"
            if entries[6].find("i", {"title": re.compile("Rating decreased with *")}):
                change = "-" + change

            w_rating_before = float(w_rating) - float(change)

            rating_dict = {
                "fighter_id": int(fighter_id),
                "event_id": int(event_id),
                "category_name": rating,
                "rank": int(rank),
                "rank_before_event": int(rank_before),
                "weighted_rating": float(w_rating),
                "weighted_rating_before_event": float(w_rating_before),
                "date": date,
            }
            rating_dicts.append(rating_dict)

    return all_fighters, rating_dicts


if __name__ == "__main__":
    event("/events/details/1/", 2016)
    event("/events/details/1995/", 2024)
