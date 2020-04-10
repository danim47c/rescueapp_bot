
token_url = 'https://login.salesforce.com/services/oauth2/token?grant_type=password&client_id=3MVG9wEVwV0C9ejCCh0zY_0PN_gyc4yX8CRvov1jfcSXqjIMYlb67v6i1oVPTjH.9Rhc8lRbpaxvVRT4FjOpg&client_secret=264491B8AA0CC4066707EFEFDF76386D7B393B7991D40D75CE325A63CE9D7D03&username=dani@rescueapp.es&password=Corona2020'

endpoint = 'https://rescueapp.my.salesforce.com/services/data/v20.0/sobjects/typeform__c/'

from teleframework.shortcuts import BaseContext, Offer

from requests import get as get_url, post as post_url
from json import dumps as json_dumps

def post_payload(payload: dict):

  resp = post_url(token_url)

  token = resp.json()['access_token']

  headers = {
    'contentType': 'application/json',
    'Authorization': 'Bearer ' + token
  }

  return post_url(
    url=endpoint,
    data=json_dumps(payload),
    headers=headers
  )


def post_offer(offer: Offer):

  for article in offer.articles:
    
    post_payload(
      {
        'Tipo__c': article.tipo,
        'Cantidad__c': article.cantidad,
        'Detalles__c': article.descripcion,

        'Tipo_contacto__c': offer.quien,
        'Tel_fono__c': offer.telefono,
        'Email__c': offer.email,
        'Estado__c': offer.ciudad,
        'Direcci_n__c': offer.calle,
      }
    )