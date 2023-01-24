from libgen_api import LibgenSearch
from parse_shelf import ParseShelf
import os
import urllib.parse
import requests

def download(book_title):
    download_path = f'{os.getcwd()}/downloads/'
    filters = {"Language": "English", "File": "epub"}
    results = s.search_title_filtered(book_title, filters, exact_match=False)
    download_link = s.resolve_download_links(results[0])["GET"]
    filename = urllib.parse.unquote(download_link).rsplit('/', 1)[1]

    if not os.path.isfile(f'{download_path}{filename}'):
        try:
            resp = requests.get(download_link)
            with open(f'{download_path}{filename}', "wb") as f:
                f.write(resp.content)
            print(f"Downloaded {filename}")
        except Exception as e:
            print(e)
    return

# TODO: Change to command line args
usage = "init"
s = LibgenSearch()
ps = ParseShelf()

if (usage == "init"):
    book_list = ps.parse_full_shelf()
    for book_title, book_author in book_list:
        try:
            download(str(book_title+' '+book_author))
        except IndexError:
            print(f"{book_title} by {book_author} is not available for download")
        except:
            print("Something went wrong")

elif (usage == "watch"):
    book_title, book_author = ps.parse_latest_entry()
    print(f"Latest entry is {book_title} by {book_author}")
    try:
        download(str(book_title+' '+book_author))
    except IndexError:
        print(f"{book_title} by {book_author} is not available for download")
    except:
        print("Something went wrong")
