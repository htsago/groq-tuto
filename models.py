from pydantic import BaseModel

class Question(BaseModel):
    query: str

class Response(BaseModel):
    answer: str

    def fetch_answer(self):
        return {
            "answer": self.answer
        }
