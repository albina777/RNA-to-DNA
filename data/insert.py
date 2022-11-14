import db
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=db.engine)
session = Session()

a = db.DNA(1, 'A')
c = db.DNA(2, 'C')
g = db.DNA(3, 'G')
t = db.DNA(4, 'T')

session.add(a)
session.add(c)
session.add(g)
session.add(t)

a2 = db.RNA(1, 'A')
c2 = db.RNA(2, 'C')
g2 = db.RNA(3, 'G')
u = db.RNA(4, 'U')

session.add(a2)
session.add(c2)
session.add(g2)
session.add(u)

session.commit()
