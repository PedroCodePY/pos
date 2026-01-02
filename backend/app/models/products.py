from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "tbl_products"

    id: Mapped[str] = mapped_column(primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    in_stock: Mapped[int] = mapped_column(nullable=False)
    product_image: Mapped[str] = mapped_column(nullable=True)
    owner_id: Mapped[str] = mapped_column(nullable=False)
    owner: Mapped[str] = mapped_column(nullable=False)
    date_created: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)
    date_updated: Mapped[datetime] = mapped_column(nullable=True, onupdate=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Product(id={self.id}, name={self.name}, description={self.description}, price={self.price}, in_stock={self.in_stock}, product_image={self.product_image}, owner_id={self.owner_id}, owner={self.owner}, date_created={self.date_created}, date_updated={self.date_updated})>"