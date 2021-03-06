from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from connection import Base


class Projection(Base):
    __tablename__ = 'projection'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey('movie.id'))
    type = Column(String)
    date = Column(String)
    time = Column(String)

    movie = relationship("Movie", backref='projections')

    def __str__(self):
        return '[{}] - {} {} ({})'.format(self.id, self.date, self.time, self.type)

    def __repr__(self):
        return self.__str__()
