"""
create_user.py
-------------
A convenience script to create a user.
"""

from getpass import getpass
from sqlmodel import SQLModel, Session, create_engine
import models as md
from auth import get_password_hash


engine = create_engine(
    "sqlite:///todos.db",
    connect_args={"check_same_thread": False},  # Needed for SQLite
    echo=True  # Log generated SQL
)


if __name__ == "__main__":
    print("Creating tables (if necessary)")
    SQLModel.metadata.create_all(engine)

    print("--------")

    print("This script will create a user and save it in the database.")

    username = input("Please enter username\n")
    pwd = getpass("Please enter password\n")

    with Session(engine) as session:
        user = md.User(username=username, password_hash=get_password_hash(pwd))
        session.add(user)
        session.commit()
