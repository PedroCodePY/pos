from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from datetime import datetime

class Store(Base):
    __tablename__ = "tbl_stores"

    id: Mapped[str] = mapped_column(primary_key=True, unique=True)
    storename: Mapped[str] = mapped_column(unique=True, nullable=False)
    owner_id: Mapped[str] = mapped_column(nullable=False, unique=True)
    store_email: Mapped[str] = mapped_column(unique=True, nullable=False)
    store_code: Mapped[str] = mapped_column(unique=True, nullable=False)
    store_street: Mapped[str] = mapped_column(unique=True, nullable=False)
    store_country: Mapped[str] = mapped_column(nullable=False)
    store_phone_number: Mapped[str] = mapped_column(unique=True, nullable=False)
    store_logo: Mapped[str] = mapped_column(unique=True)
    date_created: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)
    date_updated: Mapped[datetime] = mapped_column(nullable=True, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username={self.username}, email={self.email}, role={self.role}), date_created={self.date_created}>"