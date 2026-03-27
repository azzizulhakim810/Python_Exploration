from pydantic import BaseModel

class User(BaseModel):
  id: int
  name: str
  is_active: bool


input_data = {
  'id': "25", # Behind the scene, It automatically converts the string into a integer if possible, otherwise throws error
  # 'id': 25,
  'name': "Athlorr",
  'is_active': True
  }

user = User(**input_data)

print(user)