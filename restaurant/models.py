from restaurant import db, login_manager
from restaurant import bcrypt
from flask_login import UserMixin

#used for logging in users
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#USER DATABASE
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(length = 30), nullable = False, unique = True)
    email_address = db.Column(db.String(length = 50), nullable = False, unique = True)
    password_hash = db.Column(db.String(length = 60), nullable = False)
    tables = db.relationship('Table', backref = 'reserved_user', lazy = True) # relationship with 'Table'
    items = db.relationship('Item', backref = 'ordered_user', lazy = True) # relationship with 'Item'

    @property
    def password(self):
        return self.password
    
    #hashes the user's password
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    #verifies if the entered password in sign in form matches the user's password in the database
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
        
#TABLE RESERVATION DATABASE
class Table(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    table = db.Column(db.Integer(), nullable = False)
    time = db.Column(db.String(length = 20), nullable = False)
    date = db.Column(db.String(length = 20), nullable = False)
    accomodation = db.Column(db.Integer(), nullable = False)
    #suggestion: you might want to change 'owner' to 'reservee'
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))  #used to store info regarding user's reserved table

    #function for assigning ownership to the user's order or reserved table
    def assign_ownership(self, user):
        self.owner = user.id 
        db.session.commit()
        
# table3 = Table(table = 3, time = "10:00-10:00 am", date = "23/10/21", accomodation = 4)
# table4 = Table(table = 4, time = "11:00-10:00 am", date = "23/10/21", accomodation = 4)

#MENU DATABASE
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(length = 30), nullable = False)
    description = db.Column(db.String(length = 50), nullable = False)
    price = db.Column(db.Integer(), nullable = False)
    #suggestion: you might want to change 'owner' to 'orderer'/ 'customer'
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))  #used to store info regarding user's ordered item
    source = db.Column(db.String(length = 30), nullable = False)

#item1 = Item( name = "Barbecue Salad", description = "Delicious Dish", price = 200 )
#item2 = Item( name = "Salad with Fish", description = "Delicious Dish", price = 150 )
#item3 = Item( name = "Spinach Salad", description ="Delicious Dish" "Delicious Dish", price = 100 )
#item1 = Item( name = "", description = "", price = )
#item1 = Item( name = "", description = "", price = )

