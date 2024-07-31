import pandas
from sqlalchemy import create_engine

def ingest(db_path, file_path):
    df = pandas.read_json(file_path)
    df.rename(columns={'id': 'external_id'}, inplace=True)
    df['rating'] = None

    engine = create_engine("sqlite:///" + db_path, echo=False)
    return df.to_sql(name='song', con=engine, if_exists='append', index=False)
