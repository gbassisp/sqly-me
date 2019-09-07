from sqlalchemy import create_engine

def create_db(file_name, data, header):
    try:
        db = create_engine('sqlite:///{}.db'.format(file_name))
        data.to_sql(header, db, if_exists='append')
        print('DB created')
    except Exception as e:
        print('Could not create DB. Encountered {}'.format(e))
    return None