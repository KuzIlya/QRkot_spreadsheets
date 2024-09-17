from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer

from app.constants import DEFAULT_INVESTED_AMOUNT


class DateMixin:
    create_date = Column(DateTime, nullable=False, default=datetime.now)
    close_date = Column(DateTime, default=None)


class InvestmentMixin:
    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(
        Integer,
        nullable=False,
        default=DEFAULT_INVESTED_AMOUNT,
    )
    fully_invested = Column(Boolean, nullable=False, default=False)
