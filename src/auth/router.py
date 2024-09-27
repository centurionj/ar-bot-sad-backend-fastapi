from fastapi import APIRouter, HTTPException, status, Response

from src.auth.service import AuthService
from src.auth.schemas import SUserAuth, SUser
from src.auth.utils import get_password_hash, authenticate_user, create_access_token

router = APIRouter()


@router.post("/register", response_model=SUser)
async def register_user(user_data: SUserAuth):
    existing_user = await AuthService.get_by_filter(email=user_data.email)

    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    hashed_password = get_password_hash(user_data.password)
    await AuthService.create(email=user_data.email, password=hashed_password)

    return user_data


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    access_token = await create_access_token({'sub': str(user.id)})
    response.set_cookie('access_token', access_token, httponly=True)

    return {'access_token': access_token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie('access_token')


@router.get("/info", response_model=SUser)
async def get_user_info(user_id: int):
    user_info = await AuthService.get_by_id(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User does not exist")
    return user_info
