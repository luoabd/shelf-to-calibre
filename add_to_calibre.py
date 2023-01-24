from decouple import config
import os

CALIBRE_USERNAME = config('USER')
CALIBRE_PASSWORD = config('PASSWORD')

class AddToCalibre:
    def __init__(self):
        self.command = f'calibredb --with-library http://localhost:8080/ --username {CALIBRE_USERNAME} --password {CALIBRE_PASSWORD}'
    def import_all(self):
        os.system(f'{self.command} add downloads/*.epub')
    def import_book(self, filename):
        os.system(f'{self.command} add "downloads/{filename}"')
