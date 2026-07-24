# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-24T19:06:50Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `783ebdc45231741bd49947651a16a69c14df3fa501c44d65973ad253a59a9852`
- PROD hash: `1ee1846a37759c57cb8cd34ce0565ca09bad10c1ecd4b2a51910d47b6f2bf647`

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
