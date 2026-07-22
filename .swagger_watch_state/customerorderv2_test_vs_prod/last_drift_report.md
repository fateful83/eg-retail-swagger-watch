# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-22T13:13:10Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e04687bba969b8773d712579c16e9a2d9555770edd6c088d9e01855771b819c7`
- PROD hash: `acb072cf1b8ddf8a11134b38f8e12d1ee67ca9e95fe2d99fae9cb15769b43299`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 1

## Only in TEST
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Only in PROD
- None

## Different in TEST and PROD
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
