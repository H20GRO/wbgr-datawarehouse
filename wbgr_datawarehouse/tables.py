import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# SELECT 
# TABLE_CATALOG,
# TABLE_SCHEMA,
# TABLE_NAME, 
# COLUMN_NAME, 
# DATA_TYPE
# FROM INFORMATION_SCHEMA.COLUMNS 
# where TABLE_NAME = 'fact_meting' 

class dim_signaal(Base):
    """Table that contains all the tag information and metadata"""
    __tablename__ = "dim_signaal"
    dsg_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    dsg_tag = sqlalchemy.Column(sqlalchemy.String(200))
    dsg_name = sqlalchemy.Column(sqlalchemy.String(200))
    dsg_location = sqlalchemy.Column(sqlalchemy.String(200))
    dsg_omschrijving = sqlalchemy.Column(sqlalchemy.String(200))
    dsg_installatietype = sqlalchemy.Column(sqlalchemy.String(200))
    dsg_scanner = sqlalchemy.Column(sqlalchemy.String(200))
    dsg_installatiecode = sqlalchemy.Column(sqlalchemy.String(200))
    dsg_first_mw = sqlalchemy.Column(sqlalchemy.String(200))
    dsg_last_mw = sqlalchemy.Column(sqlalchemy.String(200))
    dwh_insert_date = sqlalchemy.Column(sqlalchemy.DateTime)
    SignaalOmschrijving = sqlalchemy.Column(sqlalchemy.String(200))
    ComponentTag = sqlalchemy.Column(sqlalchemy.String(200))
    ComponentNaam = sqlalchemy.Column(sqlalchemy.String(200))
    SignaalParameterCode = sqlalchemy.Column(sqlalchemy.String(200))
    SignaalParameterNaam = sqlalchemy.Column(sqlalchemy.String(200))
    SignaalParameterEenheid = sqlalchemy.Column(sqlalchemy.String(200))
    SignaalPresentatieEenheid = sqlalchemy.Column(sqlalchemy.String(200))
    ProcesOnderdeelTag = sqlalchemy.Column(sqlalchemy.String(200))
    ProcesOnderdeelNaam = sqlalchemy.Column(sqlalchemy.String(200))
    InstallatieNaam = sqlalchemy.Column(sqlalchemy.String(200))
    RapportageFrequentie = sqlalchemy.Column(sqlalchemy.String(200))
    locatie_naam = sqlalchemy.Column(sqlalchemy.String(200))
    Latitude = sqlalchemy.Column(sqlalchemy.DECIMAL)
    Longitude = sqlalchemy.Column(sqlalchemy.DECIMAL)
    ComponentDeel = sqlalchemy.Column(sqlalchemy.String(200))
    def __repr__(self) -> str:
        return f"{self.dsg_tag},{self.dsg_location},{self.dwh_insert_date}"  

class fact_meting(Base):
    """Raw measurements from  in DWH"""
    __tablename__ = "fact_meting"
    fmt_id = sqlalchemy.Column(sqlalchemy.BIGINT, primary_key=True)
    fmt_dsg_id = sqlalchemy.Column(sqlalchemy.INTEGER)
    fmt_ddt_id = sqlalchemy.Column(sqlalchemy.DATETIME)
    fmt_dtd_id = sqlalchemy.Column(sqlalchemy.TIME)
    fmt_dms_id = sqlalchemy.Column(sqlalchemy.SMALLINT)
    fmt_dvs_id = sqlalchemy.Column(sqlalchemy.SMALLINT)
    fmt_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    fmt_meetwaarde_status = sqlalchemy.Column(sqlalchemy.INTEGER)
    fmt_duur = sqlalchemy.Column(sqlalchemy.DECIMAL)
    dwh_insert_date = sqlalchemy.Column(sqlalchemy.DATETIME)
    PtimeStamp = sqlalchemy.Column(sqlalchemy.DATETIME)
    def __repr__(self) -> str:
        return f"{self.fmt_dsg_id},{self.fmt_meetwaarde},{self.PtimeStamp}"   

class fact_sensordata_dag(Base):
    """Day aggregates from DWH, only if they are calculated"""
    __tablename__ = "fact_sensordata_dag"
    dsg_id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    ddt_id = sqlalchemy.Column(sqlalchemy.DATETIME, primary_key=True)
    eerste_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    laatste_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    avg_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    min_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    max_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    delta_meetwaarde_periode = sqlalchemy.Column(sqlalchemy.FLOAT)
    sum_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    aantal_metingen = sqlalchemy.Column(sqlalchemy.INTEGER)
    dwh_insert_date = sqlalchemy.Column(sqlalchemy.DATETIME)
    def __repr__(self) -> str:
        return f"{self.dsg_id}, {self.ddt_id},avg: {self.avg_meetwaarde}"

class fact_sensordata_dag_val(Base):
    """Validatd day aggregates from DWH, only if they are calculated"""
    __tablename__ = "fact_sensordata_dag_val"
    dsg_id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    ddt_id = sqlalchemy.Column(sqlalchemy.DATETIME, primary_key=True)
    eerste_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    laatste_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    avg_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    min_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    max_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    delta_meetwaarde_periode = sqlalchemy.Column(sqlalchemy.FLOAT)
    sum_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    aantal_metingen = sqlalchemy.Column(sqlalchemy.INTEGER)
    dwh_insert_date = sqlalchemy.Column(sqlalchemy.DATETIME)
    aangepast = sqlalchemy.Column(sqlalchemy.INTEGER)
    def __repr__(self) -> str:
        return f"{self.dsg_id}, {self.ddt_id},avg: {self.avg_meetwaarde}"

class fact_sensordata_uur(Base):
    """Hour aggregates from DWH, only if they are calculated"""
    __tablename__ = "fact_sensordata_uur"
    dsg_id = sqlalchemy.Column(sqlalchemy.INTEGER,primary_key=True)
    ddt_id = sqlalchemy.Column(sqlalchemy.DATETIME,primary_key=True)
    periode = sqlalchemy.Column(sqlalchemy.DATETIME,primary_key=True)    
    eerste_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    laatste_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    avg_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    min_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    max_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    delta_meetwaarde_periode = sqlalchemy.Column(sqlalchemy.FLOAT)
    sum_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    aantal_metingen = sqlalchemy.Column(sqlalchemy.INTEGER)
    dwh_insert_date = sqlalchemy.Column(sqlalchemy.DATETIME)
    def __repr__(self) -> str:
        return f"{self.dsg_id}, {self.ddt_id}, avg: {self.avg_meetwaarde}"
        
class fact_sensordata_uur_val(Base):
    """Validated hour aggregates from DWH, only if they are calculated"""
    __tablename__ = "fact_sensordata_uur_val"
    dsg_id = sqlalchemy.Column(sqlalchemy.INTEGER,primary_key=True)
    ddt_id = sqlalchemy.Column(sqlalchemy.DATETIME,primary_key=True)
    periode = sqlalchemy.Column(sqlalchemy.DATETIME,primary_key=True)    
    eerste_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    laatste_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    avg_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    min_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    max_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    delta_meetwaarde_periode = sqlalchemy.Column(sqlalchemy.FLOAT)
    sum_meetwaarde = sqlalchemy.Column(sqlalchemy.FLOAT)
    aantal_metingen = sqlalchemy.Column(sqlalchemy.INTEGER)
    dwh_insert_date = sqlalchemy.Column(sqlalchemy.DATETIME)
    aangepast = sqlalchemy.Column(sqlalchemy.INTEGER)
    def __repr__(self) -> str:
        return f"{self.dsg_id}, {self.ddt_id}, avg: {self.avg_meetwaarde}"