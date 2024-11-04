from app.models.enumeration.gender import Gender
from app.models.enumeration.marital_status import MaritalStatus
from app.models.enumeration.religion import Religion
from app.models.enumeration.education_level import EducationLevel
from app.models.enumeration.family_type import FamilyType
from app.models.enumeration.dietary_preference import DietaryPreference
from app.models.enumeration.smoking_habit import SmokingHabit
from app.models.enumeration.drinking_habit import DrinkingHabit
from app.models.enumeration.nationality import Nationality
from app.models.enumeration.caste_community import CasteCommunity
from app.models.enumeration.language import Language
from app.models.enumeration.college import College
from app.models.enumeration.profession import Profession
from app.models.enumeration.family_values import FamilyValue
from app.models.enumeration.hobby import Hobby


from fastapi import APIRouter
from .generic import create_crud_router

gender_router =create_crud_router(model=Gender)
maritalstatus_router =create_crud_router(model=MaritalStatus)
religion_router =create_crud_router(model=Religion)
educationlevel_router =create_crud_router(model=EducationLevel)
familytype_router =create_crud_router(model=FamilyType)
dietarypreference_router =create_crud_router(model=DietaryPreference)
smokinghabit_router =create_crud_router(model=SmokingHabit)
drinkinghabit_router =create_crud_router(model=DrinkingHabit)
nationality_router =create_crud_router(model=Nationality)
castecommunity_router =create_crud_router(model=CasteCommunity)
language_router =create_crud_router(model=Language)
college_router =create_crud_router(model=College)
profession_router =create_crud_router(model=Profession)
familyvalue_router =create_crud_router(model=FamilyValue)
hobby_router =create_crud_router(model=Hobby)


router = APIRouter()

router.include_router(gender_router, prefix="/gender", tags=["Gender"])
router.include_router(maritalstatus_router, prefix="/marital-status", tags=["MaritalStatus"])
router.include_router(religion_router, prefix="/religions", tags=["Religions"])
router.include_router(educationlevel_router, prefix="/education-level", tags=["EducationLevel"])
router.include_router(familytype_router, prefix="/family-type", tags=["FamilyType"])
router.include_router(dietarypreference_router, prefix="/dietary-preference", tags=["DietaryPreference"])
router.include_router(smokinghabit_router, prefix="/smoking-habit", tags=["SmokingHabit"])
router.include_router(drinkinghabit_router, prefix="/drinking-habit", tags=["DrinkingHabit"])
router.include_router(nationality_router, prefix="/nationality", tags=["Nationality"])
router.include_router(castecommunity_router, prefix="/caste-community", tags=["CasteCommunity"])
router.include_router(language_router, prefix="/language", tags=["Language"])
router.include_router(college_router, prefix="/college", tags=["College"])
router.include_router(profession_router, prefix="/profession", tags=["Profession"])
router.include_router(familyvalue_router, prefix="/family-value", tags=["FamilyValue"])
router.include_router(hobby_router, prefix="/hobby", tags=["Hobby"])
