from dataclasses import dataclass
from fastapi import FastAPI

@dataclass
class User:
  username: str

class StartUserOnboarding:
  def __init__(self, user_repository):
    self._user_repository = user_repository

  def execute(self, username):
    user = User(username = username)
    self._user_repository.add(user)

class InMemoryUserRepository:
  def __init__(self):
    self._users = []

  def add(self, user): self._users.append(user)
  def get_by_username(self, username): return next(user for user in self._users if user.username == username)
  
class SQLiteUserRepository:
  def __init__(self, config):
    self._config = config

  def add(self, user): print(f"Running some SQL statements for insert DATABASE_PATH")
  def get_by_username(self, username): print(f"Running some SQL statements for fetch from {self._config.DATABASE_PATH}")

  def test_user_is_added_to_repository():
    username = "john@doe.com"
    repository = InMemoryUserRepository()    
    use_case = StartUserOnboarding(user_repository = repository)
    use_case.execute(username)
    assert repository.get_by_username(username).username

class ApplicationConfig:
  DATABASE_PATH = "db"

app = FastAPI()

@app.post("/users/start-onboarding", status_code = 202)
def start_user_onboarding(username : str):
  StartUserOnboarding(SQLiteUserRepository(ApplicationConfig())).execute(username)
  return "OK"