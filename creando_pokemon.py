import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL del archivo CSV
url = "Pokemon.csv"

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(url)

# Configuración de la base de datos MySQL
user = "root"
password = ""
host = "localhost"
port = "3306"
database = "pokemon"

Base = declarative_base()

# Crear una conexión a la base de datos MySQL
engine = create_engine(f'mysql://{user}:{password}@{host}/{database}')

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Obtener tipos únicos de Pokémon
tipos_distintos = df["Type 1"].unique()

Session = sessionmaker(bind=engine)
session = Session()

for tipo in tipos_distintos:
    tipo_lower = tipo.lower()
    
    tipo_pokemon_df = df[df["Type 1"] == tipo]
    
    class DynamicType(Base):
        __tablename__ = tipo_lower
        
        id = Column(Integer, primary_key=True)
        nombre = Column(String(255))  # Especificar la longitud de la columna
    
    DynamicType.__table__.create(bind=engine, checkfirst=True)
    
    # Cargar los datos en la tabla
    for index, row in tipo_pokemon_df.iterrows():
        tipo_pokemon = DynamicType(nombre=row['Name'])
        session.add(tipo_pokemon)

session.commit()
