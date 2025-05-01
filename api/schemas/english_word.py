from typing import Optional

from pydantic import BaseModel, Field


class EnglishWord(BaseModel):
    word: Optional[str] = Field(None, example="book")
    definition: Optional[str] = Field(None, example="book")
    synonyms: Optional[str] = Field(None, example="read")
    