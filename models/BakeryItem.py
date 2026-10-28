
from extensions import db

class BakeryItem(db.Model):
    BakeryItemID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(150))
    Category = db.Column(db.String(50))
    description = db.Column(db.String(255))
    price = db.Column(db.Float(precision=2))
    quantity = db.Column(db.Integer, default=20)
    available = db.Column(db.Boolean, default=True)
    image_url = db.Column(db.String(255))
    
    
    
    def __repr__(self):
        return f"<BakeryItem {self.Name} ({self.Category} {self.price} {self.quantity} {self.available} {self.image_url})>"