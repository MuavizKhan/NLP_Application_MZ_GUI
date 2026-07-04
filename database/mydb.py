import json
import os


class Database:

    def __init__(self):
        # Determine the absolute directory path where this file resides
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(current_dir, "db.json")

        # Create the file with an empty dictionary if it doesn't exist yet
        if not os.path.exists(self.db_path):
            with open(self.db_path, "w") as wf:
                json.dump({}, wf)

    def add_data(self, name, email, password):
        with open(self.db_path, "r") as rf:
            database = json.load(rf)

        # Check if the email key already exists to prevent duplicates
        if email in database:
            return 0
        else:
            database[email] = [name, password]
            with open(self.db_path, "w") as wf:
                json.dump(database, wf, indent=4)
            return 1

    def search(self, email, password):
        with open(self.db_path, "r") as rf:
            database = json.load(rf)

        # Validate that the credentials match the records exactly
        if email in database:
            if database[email][1] == password:
                return 1
            else:
                return 0
        else:
            return 0