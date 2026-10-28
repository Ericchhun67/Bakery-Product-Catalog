from app import create_app
from extensions import db
from models.BakeryItem import BakeryItem
from seed.seed_data import (
    bakery_items,
    bread_items,
    cookie_items,
    cakes_and_tart_items,
    seasonal_items
)

app = create_app()


with app.app_context():
    db.create_all()
    
    all_items = (
        bakery_items
        + bread_items
        + cookie_items
        + cakes_and_tart_items
        + seasonal_items
    )
    for item in all_items:
        bakery_items_existing = BakeryItem.query.filter_by(Name=item['Name']).first()
        if not bakery_items_existing:
            new_item = BakeryItem(**item)
            db.session.add(new_item)
        if bakery_items_existing:
            bakery_items_existing.image_url = item['image_url']
            
        db.session.commit()

            
    print("baked item added in database")
    