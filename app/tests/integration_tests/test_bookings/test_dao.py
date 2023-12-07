from app.bookings.dao import BookingDAO
from datetime import datetime
import pytest


@pytest.mark.parametrize(
    "user_id, room_id, date_from, date_to",
    [
        (2, 2, "2023-07-10", "2023-07-24"),
        (2, 3, "2023-03-11", "2023-03-23"),
        (1, 4, "2023-01-10", "2023-01-15"),
        (1, 4, "2023-10-15", "2023-10-27"),
    ],
)
async def test_booking_crud(user_id, room_id, date_from, date_to):
    new_booking = await BookingDAO.add(
        user_id=user_id,
        room_id=room_id,
        date_from=datetime.strptime(date_from, "%Y-%m-%d"),
        date_to=datetime.strptime(date_to, "%Y-%m-%d"),
    )

    assert new_booking["user_id"] == user_id
    assert new_booking["room_id"] == room_id

    new_booking = await BookingDAO.find_one_or_none(id=new_booking["id"])

    assert new_booking is not None

    await BookingDAO.delete(id=new_booking["id"], user_id=new_booking["user_id"])

    deleted_booking = await BookingDAO.find_one_or_none(id=new_booking["id"])
    assert deleted_booking is None
