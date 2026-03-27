from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
  username: str

  # It validates only one field at a time
  @field_validator('username') # decorator
  def username_length(cls, v):
    if len(v) < 4:
      raise ValueError("Username must be at least 4 characters")
    return v
  

class SignupData(BaseModel):
  password: str
  confirm_password: str

  # It can access all field values at the same time
  @model_validator(mode='after') # decorator - after means, it starts working after all validation
  def password_match(cls, values):
    if values.password != values.confirm_password:
      raise ValueError("Password don't match")
    return values
  
