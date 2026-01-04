from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select
from app.models.user import User
from app.models.store import Store
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class system():
    #services for authentication
    async def check_user_email(self, session: async_sessionmaker[AsyncSession], email: str, id: str, user: User):
            statement = select(User).where(User.email == email, User.id != id)
            result = await session.execute(statement)
            return result.scalar_one_or_none()

    #store
    async def check_store_code(self, session: async_sessionmaker[AsyncSession], code_shop : str):
            statement = select(Store).where(Store.store_code == code_shop)
            result = await session.execute(statement)
            return result.scalar_one_or_none()

    #User
    async def register(self, async_session: async_sessionmaker[AsyncSession], user: User):
        async with async_session() as session:
            check_email = await self.check_user_email(session, user)
            if check_email:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already registered",
                )
            
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def login_user(self, async_session, username: str, password: str):
        async with async_session() as session:
            result = await session.execute(
                select(User).where(User.username == username)
            )
            user = result.scalars().first()

            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found",
                )

            if user.code_shop:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Unauthorized access for cashiers",
                )

            if not pwd_context.verify(password, user.hashed_password):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect password or username ",
                )

            return {
                "id": user.id,
                "username": user.username,
                "role": user.role
            }
        
    async def update_user(self, async_session: async_sessionmaker[AsyncSession], user_id: str):
        pass

    async def delete_user(self, async_session: async_sessionmaker[AsyncSession], user_id: str):
        pass
    
    #Cashier
    async def cashier_register(self, async_session: async_sessionmaker[AsyncSession], user: User):
        async with async_session() as session:
            store_code = await self.check_store_code(session, user.code_shop)

            if not store_code:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Store not found",
                )
            
            #if user.email == store_code.email:
            #    raise HTTPException(
            #        status_code=status.HTTP_400_BAD_REQUEST,
            #        detail="Cannot register cashier with store owner's email",
            #    ) 
            
            check_cashier_email = await self.check_user_email(session, user.email, user.id, user)
            if check_cashier_email:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already registered",
                )
            
            session.add(user)
            await session.commit()
            await session.refresh(user)
            return user

    async def cashier_login(self, async_session: async_sessionmaker[AsyncSession], user: User):
        async with async_session() as session:
            store_code = await self.check_store_code(session, user.code_shop)
            if not store_code:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Store not found",
                )
            
            result = await session.execute(
                select(User).where(User.username == user.username and User.code_shop == user.code_shop)
            )

            cashier = result.scalars().first()
            if not cashier:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Cashier not found",
                )
            
            if not pwd_context.verify(user.hashed_password, cashier.hashed_password):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect password or username ",
                )
            
    async def cashier_update(self, async_session: async_sessionmaker[AsyncSession], user_id: str):
        pass

    async def cashier_delete(self, async_session: async_sessionmaker[AsyncSession], user_id: str):
        pass