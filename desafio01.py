from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    fornecedor = relationship("Fornecedor")


engine = create_engine('sqlite:///desafio.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


try:
    with Session() as session:
        fornecedores = [
            Fornecedor(nome="Fonecedor A", telefone="12345678", email="contato@gmail.com", endereco="Rua Tal 123"),
            Fornecedor(nome="Fonecedor B", telefone="12345678", email="contato2@gmail.com", endereco="Rua Tal 000"),
            Fornecedor(nome="Fonecedor C", telefone="12222678", email="contato3@gmail.com", endereco="Rua Tal 456"),
            Fornecedor(nome="Fonecedor D", telefone="12345428", email="contato4@gmail.com", endereco="Rua Tal 789"),
        ]

        session.add_all(fornecedores)
        session.commit()
except SQLAlchemyError as e:
    print(f'Erro ao inserir fornecedore: {e}')