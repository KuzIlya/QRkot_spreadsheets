from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donation import donation_crud
from app.models import CharityProject, User
from app.schemas.donation import DonationCreate, DonationDB, DonationRead
from app.utils.investing import investing

router = APIRouter()


@router.get(
    '/',
    response_model=list[DonationDB],
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True,
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
):
    """
    Только для суперюзеров.

    Возвращает список всех пожертвований.
    """

    return await donation_crud.get_multi(session)


@router.post(
    '/',
    response_model=DonationRead,
    response_model_exclude_none=True,
)
async def create_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """Создание пожертвования."""

    new_donation = await donation_crud.create(donation, session, user)
    await investing(new_donation, CharityProject, session)

    return new_donation


@router.get(
    '/my',
    response_model=list[DonationRead],
    response_model_exclude_none=True,
)
async def get_user_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user),
):
    """Вернуть список пожертвований пользователя."""

    return await donation_crud.get_donations_by_user(
        user, session
    )
