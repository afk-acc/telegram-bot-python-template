from repository.base import Base
from database.database import async_session_maker
from sqlalchemy import Column, String, ForeignKey, select, Integer
from sqlalchemy.orm import joinedload

from sqlalchemy.orm import relationship


class Role(Base):
    name = Column(String, nullable=False)
    users = relationship("User", back_populates="role")

    def __str__(self):
        return f"{self.name}"


class User(Base):
    phone = Column(String(length=20), nullable=False)
    user_id = Column(String(length=20), nullable=True)
    role_id = Column(ForeignKey("roles.id", ondelete="cascade"))
    role = relationship("Role", back_populates="users")

    def __str__(self):
        return f"{self.id}. {self.phone}: {self.role}"

    @classmethod
    async def find_one_or_none(cls, filter):
        async with async_session_maker() as session:
            query = select(cls).options(joinedload(cls.role)).filter(filter)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls, filter=None):
        async with async_session_maker() as session:
            if filter is not None:
                query = select(cls).filter(filter).options(joinedload(cls.role))
            else:
                query = select(cls).options(joinedload(cls.role))
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def paginate(cls, page: int, limit: int, filter=None):
        async with async_session_maker() as session:
            if filter is not None:
                query = select(cls).filter(filter).limit(limit).offset((page - 1) * limit).options(joinedload(
                    cls.role))
            else:
                query = select(cls).limit(limit).offset((page - 1) * limit).options(joinedload(
                    cls.role))
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with (async_session_maker() as session):
            query = select(cls).filter_by(id=model_id).options(joinedload(cls.role))
            result = await session.execute(query)
            result = result.unique().scalar()
            return result
