from sqlalchemy import Column, Integer, String, ForeignKey # importando os tipos do sqlalchemy
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base() # superclasse do sqlalchemy e que será herdada por todas as classes

class Aluno(Base):
    __tablename__ = 'aluno'
    
    id_aluno = Column(Integer, primary_key=True)
    nome_aluno = Column(String)
    endereco = relationship('Endereco', uselist=False) # uselist é o que define o relacionamento 1,1

    def __init__(self, nome): # não precisa do id já que é autoincrement
        self.nome_aluno = nome

    def __str__(self): # retorno do print de aluno
        return f'{self.id_aluno} {self.nome_aluno}'
    
class Endereco(Base):
    __tablename__ = 'endereco'

    id_endereco = Column(Integer, primary_key=True)
    rua = Column(String)
    id_aluno_fk = Column(Integer, ForeignKey('aluno.id_aluno'))
    aluno = relationship('Aluno')

    def __init__(self, rua):
        self.rua = rua

    def __str__(self):
        return f'{self.id_endereco} {self.rua}'