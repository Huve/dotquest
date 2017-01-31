import uuid
import json

from dot_base import base_data

class Dot():
    """A dot."""
    def __init__(self, did=None):
        if did:
            self.did = did
            self.data = self.load_data(did)
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
        pass
    
    def get_data(self):
        """Returns the dot's data."""
        return self.data
        
    def save(self):
        """Saves the dot to the database."""
        with open("data/characters.json", "r") as database:
            all_data = json.loads(database.read())
        all_data_copy = all_data
        if len(all_data.keys()) < 3:
            with open("data/characters.json", "w") as database:
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
