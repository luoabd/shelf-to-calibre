from bs4 import BeautifulSoup
import requests


class ParseShelf:
    # 30 entries per page
    shelf_url = "https://www.goodreads.com/review/list/34511932-abd?order=d&ref=nav_mybooks&shelf=to-read&sort=date_added&per_page=30"

    def __init__(self):
        self.soup = self.get_shelf_page(self.shelf_url)

    def parse_latest_entry(self):
        latest_entry = self.soup.find_all(class_="title")[1]
        latest_entry_cleaned = latest_entry.find('a')["title"]
        return latest_entry_cleaned

    def get_shelf_page(self, shelf_url):
        shelf_page = requests.get(shelf_url)
        soup = BeautifulSoup(shelf_page.text, "lxml")
        return soup

    def parse_full_shelf(self):
        self.iter = 1
        while True:
            all_entries = self.soup.find_all(class_="title")
            # 1st entry is the table's heading
            for entry in all_entries[1:]:
                print(entry.find('a')["title"])

            # If next page link is inactive, stop
            if self.soup.find('a', {"rel": "next"}) is None:
                break

            self.iter += 1
            page_indicator = "&page=" + str(self.iter)
            new_shelf_url = self.shelf_url + page_indicator
            self.soup = self.get_shelf_page(new_shelf_url)
