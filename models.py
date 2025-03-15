from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# create the base class for declarative models
Base = declarative_base()
# Create SQLite database engine
engine = create_engine('sqlite://health_predictions.db', echo=True)
# create a sessionmaker factory bound to our database
Session = sessionmaker(bind=engine)


class HealthData(Base):
    __tablename__ = "health_data"

    # Primary Key as unique identifier
    id = Column(Integer, primary_key=True, index=True)

    # User Inputs
    sleep_hours = Column(Float)
    exercise_hours = Column(Float)
    stress_levevl = Column(Integer)
    social_activity = Column(Integer)
    work_hours = Column(Float)
    screen_time = Column(Float)

    # Model Prediction Output
    prediction = Column(String)

    # Timestamp for tracking when the prediction was made
    timestamp = Column(DateTime, default=datetime.utc)


# Create all defined tables in the database
Base.metadata.create_all(bind=engine)


def get_db():
    """
    Database session generator
    Yields a database session and ensures it's closed after use
    Used as a dependency in FastAPI endpoints
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 