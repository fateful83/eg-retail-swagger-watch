# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-08T03:05:43Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `db7d7b430594fcdb73c147685b5f14c4629b9fe49bf5e6b1fade72cc285327fd`
- PROD hash: `5abd77b38ee7d82829603479807edbe1d8109383b2e846fda3215e4bed80ce6b`

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
