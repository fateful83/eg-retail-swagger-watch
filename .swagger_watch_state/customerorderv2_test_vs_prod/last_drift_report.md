# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-04T10:00:38Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6367578f2a0c21c5ff1d38d0c023acdb5902c5b49457c8c9c1a9d166fe38b20a`
- PROD hash: `d515f98d7bb19906e26c174eac2287720fcf0f65a9c33349e077217ebf91746a`

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
