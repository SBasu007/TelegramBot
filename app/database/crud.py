from .db import SessionLocal
from .models import UserProfile


# ---------------- GET USER ---------------- #

def get_user_by_telegram_id(telegram_id):

    db = SessionLocal()

    try:

        user = db.query(UserProfile).filter(
            UserProfile.telegram_id == str(telegram_id)
        ).first()

        return user

    finally:

        db.close()


# ---------------- CREATE USER ---------------- #

def create_user(
    telegram_id,
    name=None,
    age=None,
    sex=None,
    phone_number=None
):

    db = SessionLocal()

    try:

        new_user = UserProfile(

            telegram_id=str(telegram_id),

            name=name,

            age=age,

            sex=sex,

            phone_number=phone_number,

            profile_completed=False
        )

        db.add(new_user)

        db.commit()

        db.refresh(new_user)

        return new_user

    except Exception as e:

        db.rollback()

        print("CREATE USER ERROR:", e)

        return None

    finally:

        db.close()


# ---------------- UPDATE PROFILE FIELD ---------------- #

def update_user_profile(
    telegram_id,
    field,
    value
):

    db = SessionLocal()

    try:

        user = db.query(UserProfile).filter(
            UserProfile.telegram_id == str(telegram_id)
        ).first()

        if not user:

            return False

        # Allowed fields only
        allowed_fields = [
            "name",
            "age",
            "sex",
            "phone_number"
        ]

        if field not in allowed_fields:

            return False

        setattr(user, field, value)

        db.commit()

        return True

    except Exception as e:

        db.rollback()

        print("UPDATE ERROR:", e)

        return False

    finally:

        db.close()


# ---------------- COMPLETE PROFILE ---------------- #

def complete_profile(telegram_id):

    db = SessionLocal()

    try:

        user = db.query(UserProfile).filter(
            UserProfile.telegram_id == str(telegram_id)
        ).first()

        if not user:

            return False

        user.profile_completed = True

        db.commit()

        return True

    except Exception as e:

        db.rollback()

        print("COMPLETE PROFILE ERROR:", e)

        return False

    finally:

        db.close()


# ---------------- GET PROFILE DATA ---------------- #

def get_profile_data(telegram_id):

    db = SessionLocal()

    try:

        user = db.query(UserProfile).filter(
            UserProfile.telegram_id == str(telegram_id)
        ).first()

        if not user:

            return None

        return {
            "telegram_id": user.telegram_id,
            "name": user.name,
            "age": user.age,
            "sex": user.sex,
            "phone_number": user.phone_number,
            "profile_completed": user.profile_completed
        }

    finally:

        db.close()