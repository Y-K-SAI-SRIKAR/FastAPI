from pydantic import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env",extra='ignore')
    SECURITY_KEY : str
    ALGORITHM : str
    EXP_TIME : int

settings = Settings()
    