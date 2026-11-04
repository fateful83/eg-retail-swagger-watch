# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-11-04T03:26:03Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1b171e82518023868b66aac3e2a09899f108e00d4979160cc8c509f99bb65371`
- PROD hash: `244096b5e6f4bddd138cb78e4b384577d4c85f9715282c0e237c20e716111a20`

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
