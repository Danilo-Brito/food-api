from pydantic import BaseModel
from models.models import Foods
from typing import List


class FoodsSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    id: int = 1
    image: str = "https://img.spoonacular.com/recipes/9040-556x370.jpg"
    name: str = "Pizza"
    quantity: int = 3
    calories: float = 452.5


class FoodViewSchema(BaseModel):
    id: int = 1
    image: str = "https://img.spoonacular.com/recipes/9040-556x370.jpg"
    name: str = "Pizza"
    quantity: int = 3
    calories: float = 452.5


class FoodDeleteSchema(BaseModel):
    """ Retorna uma representação do produto seguindo o schema definido em
        FoodViewSchema.
    """
    name: str = "Pizza"


class FoodUpdateSchema(BaseModel):
    id: int = 1
    quantity: int = 3


class CaloriesSchema(BaseModel):
    total: float = 1234.6


def show_foods(foodList: List[Foods]):
    """ Retorna uma representação do produto seguindo o schema definido em
        FoodViewSchema.
    """

    result = []
    for foods in foodList:
        result.append({
            "id": foods.id,
            "image": foods.image,
            "name": foods.name,
            "quantity": foods.quantity,
            "calories": foods.calories
        })

    return {"foods": result}


def show_total(total):
    return {"total": total}
