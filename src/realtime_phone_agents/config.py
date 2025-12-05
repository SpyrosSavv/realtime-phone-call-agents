from typing import ClassVar
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Groq Configuration
class GroqSettings(BaseModel):
    api_key: str = Field(default="", description="Groq API key")
    base_url: str = Field(default="https://api.groq.com", description="Groq base url")
    model: str = Field(default="openai/gpt-oss-20b", description="Groq model to use")



class Settings(BaseSettings):
    groq: GroqSettings = Field(default_factory=GroqSettings)

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_file=[".env"],
        env_file_encoding="utf-8",
        extra="ignore",
        env_nested_delimiter="__",
        case_sensitive=False,
        frozen=True,
    )

settings = Settings()