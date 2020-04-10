
from teleframework.models import *

class Offer(BaseModel):

    oid = pw.AutoField()

    user = pw.ForeignKeyField(User, backref='offers', on_delete='CASCADE')

    class Meta:
        database = db
        db_table = 'offers'

    quien = pw.TextField(null=True)
    nombre = pw.TextField(null=True)
    persona = pw.TextField(null=True)
    telefono = pw.IntegerField(null=True)
    email = pw.TextField(null=True)
    ciudad = pw.TextField(null=True)
    cp = pw.TextField(null=True)
    calle = pw.TextField(null=True)
    unirse = pw.BooleanField(null=True)

    finished = pw.BooleanField(default=False)



class OfferArticle(BaseModel):

    oaid = pw.AutoField()

    offer = pw.ForeignKeyField(Offer, backref='articles', on_delete='CASCADE')

    tipo = pw.TextField(null=True)

    cantidad = pw.IntegerField(null=True)

    descripcion = pw.TextField(null=True)

    class Meta:
        database = db
        db_table = 'offer_articles'


User.create_table()
Offer.create_table()
OfferArticle.create_table()

