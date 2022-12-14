from msilib.sequence import tables
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL 
from sqlalchemy.orm import sessionmaker,Session,Query
from .tables import *

class QueryExtensions(Query):
    """"Extends the SqlAlchemy Query class """
    def to_df(self) -> pd.DataFrame:
        return pd.read_sql_query(sql = self.statement, con = self.session.connection())

class db:
    """The db connection to WBGR Datawarehouse.
        Use get_session after creation to create a query """
    def __init__(self, driver_name='mssql',server_name = "srv-dwh-003", database_name = "wbgr_datamart" ) -> None:
       
        connection_url = URL.create(
            driver_name,
            host=server_name,
            database=database_name,
            query={
                "driver": "ODBC Driver 17 for SQL Server",
            },)
        self.engine = create_engine(connection_url,echo=True)#echo = True for loggin the queries
        self.session_maker = sessionmaker(bind = self.engine)       

    def get_session(self, cls=QueryExtensions) -> Session:  #possible to extend the Session class to return the extended QueryExtensionsClass 
        """Return a session to build a query."""
        with self.session_maker(query_cls=cls) as session:
            return session

if __name__ == '__main__':
    _db = db()
    
    session =_db.get_session()    
    df:pd.DataFrame = session \
             .query(dim_signaal) \
             .filter(dim_signaal.dsg_location == 'PDP')\
             .to_df()
    
    print(df['dsg_id'])            
    
    
    df_vals = session.query(fact_sensordata_uur)\
                .filter(fact_sensordata_uur.ddt_id.between('2022-05-01', '2022-05-12')) \
                .filter(fact_sensordata_uur.dsg_id.in_(df['dsg_id'].values[1:50].tolist()))\
                .to_df()
    print(df_vals.head(n=4)) 
    print(df_vals.size) 
    print(df_vals.groupby('dsg_id').max()) 
    


