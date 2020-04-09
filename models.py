
from teleframework.models import *

class Offer(BaseModel):

    oid = pw.AutoField()

    user = pw.ForeignKeyField(User, backref='offers')

    sent = pw.BooleanField(default=False)

    class Meta:
        database = db
        db_table = 'offers'


class OfferArticle(BaseModel):

    oaid = pw.AutoField()

    offer = pw.ForeignKeyField(Offer, backref='articles')

    article = pw.TextField(null=True)

    quantity = pw.IntegerField(null=True)

    description = pw.TextField(null=True)

    class Meta:
        database = db
        db_table = 'offer_articles'


User.create_table()
Offer.create_table()
OfferArticle.create_table()

