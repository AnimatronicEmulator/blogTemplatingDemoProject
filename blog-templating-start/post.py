class Post:
    def __init__(self, json_data):
        self.data = json_data
        self.id = self.definer("id")
        self.title = self.definer("title")
        self.subtitle = self.definer("subtitle")
        self.body = self.definer("body")

    def definer(self, value_str):
        return self.data[value_str]
