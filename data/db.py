from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.testing import db

engine = create_engine("sqlite:///quantori.db", echo=True)
Base = declarative_base()


class DNA(Base):
    __tablename__ = "DNA_bases"

    id = Column(Integer, primary_key=True)
    dna_bases = Column(String(30))

    def __init__(self, id, dna_bases):
        self.id = id
        self.dna_bases = dna_bases

    child = relationship("RNA", back_populates="parent", uselist=False)


class RNA(Base):
    _tablename__ = "RNA_bases"

    id = Column(Integer, primary_key=True)
    rna_bases = Column(String(30))
    dna_id = Column(Integer, ForeignKey("dna.id"))

    def __init__(self, id_, rna_bases):
        self.id = id_
        self.dna_bases = rna_bases


class amino_acids(Base):
    _tablename__ = "amino_acids"

    id_ = Column(Integer, primary_key=True)
    rna_id = Column(Integer, ForeignKey("rna.id"))

    def __init__(self, id_):
        self.id = id_


Base.metadata.create_all(engine)
