import uuid
import json

from dot_base import base_data

class Dot():
    """A dot."""
    def __init__(self, did=None):
        self.database_location = "data/characters.json"
        if did:
            self.did = did
            self.data = self.load()
        else:
            self.did = uuid.uuid4().hex
    
    def create_new(self, player_class, name):
        """Creates a new dot and saves the data.

        Args:
          player_class: class of the character.
          name: name of the character.
        """
        self.data = base_data[player_class]
        self.data['name'] = name

    def delete(self):
        """Deletes a dot from the database."""
        all_data = self.load_all()
        all_data_copy = all_data
        with open(self.database_location, "w") as database:
            try:
                del all_data[self.did]
                json.dump(all_data, database)
            except Exception as e:
                json.dump(all_data_copy, database)  

    def load(self):
        """Loads this dot's data."""
        with open("data/characters.json", "r") as database:
            all_data = json.loads(database.read())
        return all_data[self.did]
    
    def get_data(self):
        """Returns the dot's data."""
        return self.data

    def load_all(self):
        """Loads all the data in the database."""
        with open(self.database_location , "r") as database:
            all_data = json.loads(database.read())
        return all_data
        
    def save(self):
        """Saves the dot to the database."""
        all_data = self.load_all()
        all_data_copy = all_data
        if len(all_data.keys()) < 3:
            with open(self.database_location, "w") as database:
                try:
                    all_data[self.did] = self.data
                    json.dump(all_data, database)
                except Exception as e:
                    json.dump(all_data_copy, database)    
def main():
    dot = Dot()
    dot.create_new("tank", "Dlob Junior")
    dot.save()

if __name__ == "__main__":
    main()
