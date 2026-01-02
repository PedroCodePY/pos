from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from datetime import datetime

class Transaction(Base):
    __tablename__ = "tbl_transactions"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(nullable=False)
    product_id: Mapped[int] = mapped_column(nullable=False)
    product_name: Mapped[str] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    total_price: Mapped[float] = mapped_column(nullable=False)
    timestamp: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)
    transaction_code: Mapped[str] = mapped_column(nullable=False, unique=True)

    def __repr__(self) -> str:
        return f"<Transaction(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, product_name={self.product_name}, quantity={self.quantity}, total_price={self.total_price}, timestamp={self.timestamp}, transaction_code={self.transaction_code})>"