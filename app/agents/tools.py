from app.database.crud import (
    update_user_profile
)


def update_profile_tool(
    telegram_id,
    field,
    value
):

    success = update_user_profile(
        telegram_id,
        field,
        value
    )

    return success