class Radio:
    def __init__(self, song_set, preference_set):
        self.song_set = song_set
        self.preference_set = preference_set
        self.weight = None
        self.features = None
        self.targets = None

    def get_preference_set(self):
        return self.preference_set

    def get_song_set(self):
        return self.song_set

    def post_preference_set(self, preference_set):
        self.preference_set = preference_set

    def post_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight
