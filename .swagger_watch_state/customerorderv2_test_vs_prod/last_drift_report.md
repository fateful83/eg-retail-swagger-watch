# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-28T21:56:09Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0e551e1bc47e39845d03831a8244fb42bb5a23538e80d64a76eb110575b03ac9`
- PROD hash: `a1d003a2390e8d2bfe41f8cbc8b506d14f84eaed4e11637168b8b364ec90b85b`

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
