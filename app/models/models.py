import mongoengine as me
import datetime

me.connect('webshopbot_db')


class Supplier(me.Document):
    name = me.StringField(required=True, min_length=2, max_length=256)


class Admin(me.Document):
    login = me.StringField(min_length=6, max_length=64, required=True, unique=True)
    password = me.StringField(min_length=8, max_length=128, required=True)
    email = me.EmailField()


class User(me.Document):
    telegram_id = me.IntField(primary_key=True)
    name = me.StringField(min_length=2, max_length=256)
    phone = me.StringField(min_length=8, max_length=12)
    address = me.StringField(min_length=4, max_length=128)


class Review(me.Document):
    rating = me.IntField(min_value=0, max_value=10)
    comment = me.StringField(min_length=1, max_length=256)
    product = me.ReferenceField('Product')
    user = me.ReferenceField(User)


class Category(me.Document):
    title = me.StringField(min_length=2, max_length=128, required=True)
    description = me.StringField(max_length=2048)


class Product(me.Document):
    title = me.StringField(min_length=2, max_length=128, required=True)
    description = me.StringField(max_length=2048)
    price = me.DecimalField(force_string=True, required=True, min_value=0)
    discount = me.IntField(min_value=0, max_value=100, default=0)
    in_stock = me.BooleanField(default=True)
    category = me.ReferenceField(Category)
    supplier = me.ReferenceField(Supplier)


class News(me.Document):
    title = me.StringField(min_length=2, max_length=256, required=True)
    body = me.StringField(min_length=2, max_length=4096, required=True)
    created = me.DateTimeField(default=datetime.datetime.now())

