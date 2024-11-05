from fastapi import APIRouter, Depends, HTTPException, status
from app.auth.injections import get_current_user
from app.models.user import User
from app.models.engagement import Engagement
from app.models.profile import Profile
from app.serializers.engagement import EngagementUserResponse, MatchedUserResponse
from peewee import fn, IntegrityError
from app.services.profile import get_user_age, get_profile_image_path
from uuid import UUID

router = APIRouter()


def profile_to_engagement_response(profile: Profile) -> EngagementUserResponse:
    return EngagementUserResponse(
        id=profile.user.id,
        name=profile.name,
        age=get_user_age(profile),
        height=profile.height,
        marital_status=profile.marital_status.id,
        nationality=profile.nationality.id,
        city=profile.city,
        religion=profile.religion.id,
        caste_community=profile.caste_community.id,
        mother_tongue=profile.mother_tongue.id,
        education_level=profile.education_level.id,
        job_title=profile.job_title.id,
        company_name=profile.company_name,
        annual_income=profile.annual_income,
        family_type=profile.family_type.id,
        fathers_occupation=profile.fathers_occupation.id,
        mothers_occupation=profile.mothers_occupation.id,
        siblings=profile.siblings,
        family_values=profile.family_values.id,
        dietary_preference=profile.dietary_preference.id,
        smoking_habit=profile.smoking_habit.id,
        drinking_habit=profile.drinking_habit.id,
        hobbies=profile.hobbies_interests or [],
        image=get_profile_image_path(profile),
        financial_info=profile.financial_info
    )


@router.get("/recommend", response_model=EngagementUserResponse)
async def get_random_unengaged_user(current_user: User = Depends(get_current_user)):
    # Get all users the current user has engaged with
    engaged_users = Engagement.select(Engagement.recipient).where(Engagement.initiator == current_user)

    # Check for current users preferences!!
    # Find a random user that the current user hasn't engaged with

    recommended_user = (
        User.select().where(User.id != current_user.id, User.id.not_in(engaged_users)).order_by(fn.Random()).first()
    )

    if not recommended_user:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No new users available for you!")

    recommended_user_profile = Profile.get(user=recommended_user)
    print(recommended_user_profile.id)
    print(recommended_user_profile.name)
    print(recommended_user_profile.height)
    print(recommended_user_profile.marital_status)
    print(recommended_user_profile.nationality)
    print(recommended_user_profile.city)
    print(recommended_user_profile.religion)
    print(recommended_user_profile.caste_community)
    print(recommended_user_profile.mother_tongue)
    print(recommended_user_profile.education_level)
    print(recommended_user_profile.job_title)
    print(recommended_user_profile.company_name)
    print(recommended_user_profile.annual_income)
    print(recommended_user_profile.annual_income)
    print(recommended_user_profile.family_type)
    print(recommended_user_profile.fathers_occupation)
    print(recommended_user_profile.mothers_occupation)
    print(recommended_user_profile.siblings)
    print(recommended_user_profile.family_values)
    print(recommended_user_profile.dietary_preference)
    print(recommended_user_profile.smoking_habit)
    print(recommended_user_profile.drinking_habit)
    print(recommended_user_profile.hobbies_interests)
    print(recommended_user_profile.image)
    print(recommended_user_profile.financial_info)

    return profile_to_engagement_response(recommended_user_profile)


@router.get("/matched-users", response_model=list[MatchedUserResponse])
async def get_matched_users(current_user: User = Depends(get_current_user)) -> list[MatchedUserResponse]:
    # Find users where both have liked each other
    matched_users = (
        User.select(User, Profile.name)
        .join(Engagement, on=(User.id == Engagement.recipient))
        .join(Profile, on=(User.id == Profile.user))
        .where(
            (Engagement.initiator == current_user)
            & (Engagement.action is True)
            & (
                Engagement.id.in_(
                    Engagement.select(Engagement.initiator).where(
                        (Engagement.recipient == current_user) & (Engagement.action is True)
                    )
                )
            )
        )
        .distinct()
    )

    matched_users_info = []
    for user in matched_users:
        profile = Profile.get(user=user)
        matched_users_info.append(
            MatchedUserResponse(id=user.id, name=profile.name, image=get_profile_image_path(profile))
        )

    return matched_users_info


@router.post("/engage/{user_id}")
async def engage_user(user_id: UUID, action: bool, current_user: User = Depends(get_current_user)):
    if user_id == current_user.id:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You cannot engage with yourself")

    target_user = User.get_or_none(User.id == user_id)
    if not target_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    try:
        engagement = Engagement.create(initiator=current_user, recipient=target_user, action=action)
    except IntegrityError: # User has already engaged with the target user (How's this possible?, Update the existing record)
        engagement = Engagement.get(initiator=current_user, recipient=target_user)
        engagement.action = action
        engagement.save()

    # Check if there's a mutual like
    mutual_like = Engagement.get_or_none(
        (Engagement.initiator == target_user)
        & (Engagement.recipient == current_user)
        & (Engagement.action is True)
    )

    if action is True and mutual_like:
        return {"message": "It's a match!", "mutual_match": True}

    else:
        return {"message": "Engagement recorded successfully"}
