from typing import Optional

from pydantic import BaseModel


class SSignboardItem(BaseModel):
    id: int
    title: Optional[str]
    file: str
    height: int
    width: int

    class Config:
        orm_mode = True


class SSignboard(BaseModel):
    id: int
    title: Optional[str]
    access_token: str
    items: list[SSignboardItem]

    class Config:
        orm_mode = True
