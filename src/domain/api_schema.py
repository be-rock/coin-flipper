#from typing import List, Optional
#
#from pydantic import BaseModel
#
#
#class CoinFlipBase(BaseModel):
#    """"""
#
#class CoinFlip
#    pass
#
#
#class Item(ItemBase):
#    id: int
#    owner_id: int
#
#    class Config:
#        orm_mode = True
#
#
#class UserBase(BaseModel):
#    email: str
#
#
#class UserCreate(UserBase):
#    password: str
#
#
#class User(UserBase):
#    id: int
#    is_active: bool
#    items: List[Item] = []
#
#    class Config:
#        orm_mode = True