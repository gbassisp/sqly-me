from sqlalchemy import create_engine

def create_db(file_name, data, header):
    try:
        db = create_engine('sqlite://{}'.format(file_name))
        data.to_sql(header, db, if_exists='append')
    except:
        print('Could not create DB')
    return None