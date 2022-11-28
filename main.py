from libgen_api import LibgenSearch
from parse_shelf import ParseShelf
import os
import urllib.parse
import urllib.request

def download(book_title):
    filters = {"Language": "English", "File": "epub"}
    results = s.search_title_filtered(book_title, filters, exact_match=False)
    download_link = s.resolve_download_links(results[0])["GET"]
    filename = urllib.parse.unquote(download_link).rsplit('/', 1)[1]

    if not os.path.isfile(filename):
        urllib.request.urlretrieve(download_link, filename)
    # print(f"Downloaded {filename}")

s=LibgenSearch()
ps = ParseShelf()

book_title, book_author = ps.parse_latest_entry()
download(str(book_title+book_author))