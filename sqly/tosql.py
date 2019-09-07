from sqlalchemy import create_engine
import pandas as pd

def create_db(file_name, data, header):
    try:
        db = create_engine('sqlite:///{}.db'.format(file_name))
        data.to_sql(header, db, if_exists='append')
        print('DB created')
        df = pd.read_sql_query('SELECT * FROM {} LIMIT 3'.format(header),db)
        df.head()
    except Exception as e:
        print('Could not create DB. Encountered {}'.format(e))
    return None