from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select
from starlette.middleware.sessions import SessionMiddleware

from app.models import Product
from app.db import engine, create_db_and_tables, populate_sample_products, get_db

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    populate_sample_products()

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    with Session(engine) as session:
        products = session.exec(select(Product)).all()
    cart_ids = request.session.get("cart", [])
    return templates.TemplateResponse("index.html", {
        "request": request,
        "products": products,
        "cart_ids": cart_ids
    })

@app.post("/cart/add/{product_id}", response_class=HTMLResponse)
def add_to_cart(request: Request, product_id: int):
    cart = request.session.get("cart", [])
    if product_id not in cart:
        cart.append(product_id)
        request.session["cart"] = cart
    return f"<button disabled>追加済み</button>"

@app.post("/cart/clear", response_class=HTMLResponse)
def clear_cart(request: Request):
    request.session["cart"] = []
    return templates.TemplateResponse("cart.html", {"request": request, "products": []})

@app.post("/cart/remove/{product_id}")
async def remove_from_cart(request: Request, product_id: int):
    cart = request.session.get("cart", [])
    if product_id in cart:
        cart.remove(product_id)
        request.session["cart"] = cart
    return RedirectResponse(url="/cart", status_code=303)

@app.post("/cart/checkout")
async def checkout(request: Request):
    request.session["cart"] = []
    return templates.TemplateResponse("checkout.html", {"request": request})

@app.get("/cart", response_class=HTMLResponse)
async def view_cart(request: Request):
    cart_ids = request.session.get("cart", [])
    products = []
    total_price = 0
    if cart_ids:
        with Session(engine) as session:
            products = session.exec(select(Product).where(Product.id.in_(cart_ids))).all()
            total_price = sum(product.price for product in products)
    return templates.TemplateResponse("cart.html", {
        "request": request,
        "products": products,
        "total_price": total_price
    })
