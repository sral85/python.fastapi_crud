from sqlmodel import create_engine, Session

engine = create_engine(
    "sqlite:///todos.db",
    connect_args={"check_same_thread": False},  # Needed for SQLite
    echo=True  # Log generated SQL
)


def get_session():
    with Session(engine) as session:
        yield session
