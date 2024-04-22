from typing import Annotated

from fastapi import APIRouter, Depends

from fastapi.security import  HTTPBasic, HTTPBasicCredentials
router = APIRouter(prefix="/auth", tags=["Demo Auth"])
security = HTTPBasic()
@router.get("/auth/")
def auth_credenrials(
        credentials:Annotated[HTTPBasicCredentials,Depends(security)],
):
    return {
        "message" : "hehe",
        "username" : credentials.username,
        "password" : credentials.password,
    }
