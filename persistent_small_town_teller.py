# Declare a PersistenceUtils class with the following static methods:
#
# write_pickle
# load_pickle

import pickle

class PersistenceUtils:

    @staticmethod
    def write_pickle(obj):
        return pickle.dumps(obj)

    @staticmethod
    def load_pickle(obj):
        return pickle.loads(obj)