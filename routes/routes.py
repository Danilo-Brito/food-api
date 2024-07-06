from flask import redirect
from food import app, db, home_tag, food_tag
from models.models import Foods
from schemas import FoodsSchema, ErrorSchema, show_foods
from schemas.foods import FoodViewSchema, FoodDeleteSchema, CaloriesSchema, show_total, FoodUpdateSchema
from sqlalchemy.exc import IntegrityError
from urllib.parse import unquote


@app.get('/', tags=[home_tag])
def home():
    """
    Redireciona para openapi
    """
    return redirect('/openapi')


@app.get('/foods', tags=[food_tag], responses={"200": FoodsSchema, "404": ErrorSchema})
def index():
    """
    Busca e retorna todos os alimentos cadastrados
    """
    foods = db.session.query(Foods).all()
    return show_foods(foods), 200


@app.post('/create', tags=[food_tag], responses={"200": FoodViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def create(form: FoodsSchema):
    """
    Adiciona um novo alimento ao banco de dados
    """

    new_food = Foods(
        image=form.image,
        name=form.name,
        quantity=form.quantity,
        calories=form.calories
    )

    try:
        db.session.add(new_food)
        db.session.commit()
        return show_foods(new_food), 200

    except IntegrityError as e:
        error_message = "Alimento já está cadastrado!"
        return {"message": error_message}, 409

    except Exception as e:
        error_message = f"Não foi possível salvar o alimento. Error:${e}"
        return {"message": error_message}, 400


@app.delete('/delete', tags=[food_tag], responses={"200": FoodsSchema, "404": ErrorSchema})
def delete(query: FoodDeleteSchema):
    """
    Deleta um alimento do banco.
    :param query: Food ID
    :return: Item deletado
    """

    food_name = unquote(unquote(query.name))
    print(food_name)
    count = db.session.query(Foods).filter(Foods.name == food_name).delete()
    db.session.commit()
    if count:
        return {"message": "Alimento removido", "nome": food_name}
    else:
        error_msg = "Alimento não encontrado"
        return {"message": error_msg}, 404


@app.put('/update', tags=[food_tag], responses={"200": FoodsSchema, "404": ErrorSchema})
def update(form: FoodUpdateSchema):
    """
    Adiciona a nova quantidade no banco de dados.
    """

    food_update = db.session.query(Foods).filter(Foods.id == form.id)
    food_update.update(
        {
            "quantity": form.quantity
        }
    )
    db.session.commit()
    if food_update:
        return {"message": "Alimento atualizado"}, 200
    else:
        error_msg = "Alimento não encontrado"
        return {"message": error_msg}, 404


@app.get('/calories', tags=[food_tag], responses={"200": CaloriesSchema, "404": ErrorSchema})
def calories():
    """
    Busca e retorna o total de calorias
    """
    foods = db.session.query(Foods).all()
    total = 0.0

    for item in foods:
        result = item.quantity * item.calories
        total += result

    format_num = "{:.2f}".format(total)
    return show_total(format_num), 200
