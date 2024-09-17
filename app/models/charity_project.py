from sqlalchemy import Column, String, Text

from app.core.db import Base
from app.models.base import DateMixin, InvestmentMixin
from app.constants import MAX_LENGTH_FOR_NAME


class CharityProject(InvestmentMixin, DateMixin, Base):
    name = Column(String(MAX_LENGTH_FOR_NAME), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return (
            f'Благотворительный проект {self.name}: {self.description}'
        )
