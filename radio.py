import copy


class Radio:
    def __init__(self, song_set, preference_set):
        self.song_set = song_set
        self.preference_set = preference_set
        self.classifier = None
        self.song_features = list(['title', 'artist', 'album', 'song_id'])
        self.important_feature = 'relevance_global_play'
        self.targets = None
        self.distance_matrix = None

    def get_preference_set(self):
        return self.preference_set

    def post_preference_set(self, preference_set):
        self.preference_set = preference_set

    def get_song_set(self):
        return self.song_set

    def post_classifier(self, new_classifier):
        self.classifier = new_classifier

    def get_classifier(self):
        return self.classifier

    def post_distance_matrix(self, new_distance_matrix):
        self.distance_matrix = new_distance_matrix

    def get_distance_matrix(self):
        return self.distance_matrix

    def get_song_features(self):
        return self.song_features

    def get_all_features(self):
        to_return = copy.copy(self.song_features)
        to_return.append(self.important_feature)
        return to_return

    def get_song(self, song_to_find):
        if song_to_find in self.song_set['song_id'].tolist():
            return str(song_to_find)
        else:
            return ''

    def get_song_position(self, song_to_find):
        song_ids = self.song_set['song_id'].tolist()
        if song_to_find in song_ids:
            return song_ids.index(song_to_find)
        else:
            return ''

    def get_important_feature(self):
        return self.important_feature

    def get_feature_weight(self):
        return self.classifier.feature_importances_
