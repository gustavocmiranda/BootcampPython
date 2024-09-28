from typing import Optional

from sqlmodel import Field, SQLModel, Session, create_engine

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

engine = create_engine("sqlite:///database.db", echo=True)

SQLModel.metadata.create_all(engine)

hero1 = Hero(id=1, name= "Deadpool", secret_name = "Dave Wilson")
hero2 = Hero(id=2, name= "Capitan America", secret_name = "Steve Rodgers")
hero3 = Hero(id=3, name= "Spider Man", secret_name = "Peter Parker", age=17)

with Session(engine) as session:
    session.add(hero1)
    session.add(hero2)
    session.add(hero3)
    session.commit()