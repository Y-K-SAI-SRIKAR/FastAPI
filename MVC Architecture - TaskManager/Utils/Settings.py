from pydantic_settings import SettingsConfigDict
from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",extra='ignore')
    SECURITY_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int

settings = Settings()
    