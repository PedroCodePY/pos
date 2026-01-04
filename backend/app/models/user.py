from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "tbl_users"

    id: Mapped[str] = mapped_column(primary_key=True, unique=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(nullable=False)  # e.g., 'admin' or 'cashier'
    code_shop: Mapped[str] = mapped_column(unique=True)  # Only for cashiers
    date_created: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)
    date_updated: Mapped[datetime] = mapped_column(nullable=True, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username={self.username}, email={self.email}, role={self.role}), date_created={self.date_created}>"