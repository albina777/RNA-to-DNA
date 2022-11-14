import db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.engine)
session = Session()

for s in session.query(db.DNA).all():
    print(s.id, s.dna_bases)

for i in session.query(db.RNA).all():
    print(i.id_, i.rna_bases)
