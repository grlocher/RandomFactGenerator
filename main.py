from fastapi import FastAPI
from pydantic import BaseModel


# Fact class
class Fact(BaseModel):
    id: int
    fact: str


app = FastAPI()

# Small list of facts
facts = [
    Fact(id=0, fact='The Detroit Lions have won four National Football League championships'),
    Fact(id=1, fact='The Detroit Lions hold an annual Thanksgiving Day game'),
    Fact(id=2, fact='This is our year')]


# Return all the facts in the list
@app.get('/fact')
async def get_all_facts():
    return facts


# Return a specific fact from the list based on id
@app.get('/fact/{id}')
async def get_fact_by_id(id: int):
    for fact in facts:
        if fact.id == id:
            return fact
    return f'Fact {id} not available'


# Add your own fact via an API post
@app.post('/fact')
async def add_fact(fact: Fact):
    facts.append(fact)
    return fact
