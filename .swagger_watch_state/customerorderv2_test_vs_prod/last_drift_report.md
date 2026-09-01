# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-01T15:36:31Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2863aa1cccd0476b4e786bc6646f93afb5cdeb3a96507d0df889b20cbb9f2cd7`
- PROD hash: `fae84caca88461d4ba5ab1420be79fe5fe87d9d4574ace91deb1097c11f6f0fc`

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
