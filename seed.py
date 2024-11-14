from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

channy = Pet(name="Chandler", 
             species="Cat", 
             photo_url="https://i.postimg.cc/QMyGCVHW/channy.png", 
             age=6, 
             notes="Adorable and perfect", 
             available=False)

lady = Pet(name="Lady", 
             species="Dog", 
             photo_url="https://i.postimg.cc/kGxXKKvT/A997-B7-C3-7-EC0-4-ED0-976-B-1-F4-CABE0-AC2-D-1-201-a.jpg", 
             age=13, 
             notes="Docile and kind", 
             available=True)

sissy = Pet(name="Sissy", 
             species="Cat", 
             photo_url="https://i.postimg.cc/7ZtW4LF6/34-E64-BD5-3216-4691-851-F-58-D4469-C3-BCD.avif", 
             age=2, 
             notes="Very Sassy. Loves salmon flavored treats", 
             available=True)

diesel = Pet(name="Diesel",
             species="Dog", 
             age=8, 
             notes="Very good boy", 
             available=True)

georgia = Pet(name="Georgia", 
             species="Cat", 
             photo_url="https://i.postimg.cc/BvJLsxK5/IMG-9751.jpg", 
             notes="Fat and sassy", 
             available=True)

db.session.add_all([channy, lady, sissy, diesel, georgia])
db.session.commit()