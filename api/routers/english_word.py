from fastapi import APIRouter
import api.schemas.english_word as english_word_schema
from api.wordsapi import definition_response, synonyms_response

router = APIRouter()


@router.get("/english_word/{word}", response_model=english_word_schema.EnglishWord)
async def get_word_info(word: str):
# パスから受け取る
    return (english_word_schema.EnglishWord(word=word),
            english_word_schema.EnglishWord(definition=definition_response),
            english_word_schema.EnglishWord(synonyms=synonyms_response))

    # return {
    #             "word": english_word_schema.EnglishWord(word=word),
    #             "definition": "definition",
    #             "synonyms": "synonyms"
    #         }
