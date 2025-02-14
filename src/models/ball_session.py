# Uncomment when server is ready
# import uuid
# from datetime import datetime

# from sqlalchemy import Column, DateTime, Float, String
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()


# class BallSession(Base):
#     __tablename__ = "ball_session"

#     id = Column(String, primary_key=True, default=lambda: uuid.uuid4().hex)
#     user_id = Column(String, nullable=False)
#     public_raw_url = Column(String, nullable=False)
#     public_overlayed_url = Column(String, nullable=False)
#     speed = Column(Float, nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return f"<BallSession(user_id='{self.user_id}', public_raw_url='{self.public_raw_url}', public_overlayed_url='{self.public_overlayed_url}', speed='{self.speed}', created_at='{self.created_at}')>"
