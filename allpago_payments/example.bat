

curl https://test.oppwa.com/v1/checkouts \
 -d "entityId=8a8294174e918ca6014e9c6f5ae12a9c" \
 -d "amount=1.00" \
 -d "currency=BRL" \
 -d "paymentType=PA" \
 -d "merchantTransactionId=Order Number 123" \
 -d "customer.merchantCustomerId=12345678909" \
 -d "customer.givenName=Jose" \
 -d "customer.surname=da Silva" \
 -d "customer.email= info@provider.com" \
 -d "customer.ip=123.123.123.123" \
 -d "descriptor=123 Usage" \
 -d "billing.city=Sao Paulo" \
 -d "billing.country=BR" \
 -d "billing.state=SP" \
 -d "billing.street1=Rua Itapeva 547" \
 -d "billing.postcode=01332000" \
 -d "customParameters[product]=1 month membership" \
 -d "customParameters[merchant_website]=www.store.com" \
 -d "recurringType=INITIAL" \
 -d "testMode=EXTERNAL" \
 -H "Authorization: Bearer OGE4Mjk0MTcyODFiOGVlMzAxMjgyOTkwNjZmNTBjZGJ8ZGVtbw=="