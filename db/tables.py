import os.path

schema_path = os.path.join(os.path.dirname(__file__), 'schema')


class Dict(object):
    table_name = u'Dict'
    hashkey = 'id'

