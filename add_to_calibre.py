from decouple import config
import os

CALIBRE_USERNAME = config('USER')
CALIBRE_PASSWORD = config('PASSWORD')

# Add all books in the current directory
os.system(f'calibredb --with-library http://localhost:8080/ add *.epub --username {CALIBRE_USERNAME} --password {CALIBRE_PASSWORD}')