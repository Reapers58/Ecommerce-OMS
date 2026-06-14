from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: str
    mobile: str

    class Config:
        from_attributes = True