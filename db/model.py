from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

# Create base class for ORM models
Base = declarative_base()

class Note(Base):
    __tablename__ = 'notes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(350), nullable=False)
    time = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Note(id={self.id}, content='{self.content[:20]}...', time={self.time})>"
    
    def to_dict(self):
            return {
                "id": self.id,
                "content": self.content,
                "time": self.time.isoformat() if self.time else None
            }