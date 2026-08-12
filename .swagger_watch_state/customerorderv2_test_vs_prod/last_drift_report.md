# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-12T18:42:25Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7e1b8f86e522aed58db358a26013c6ba46648bfbad63fa04f982b8aafa73a14d`
- PROD hash: `700c2cd381ba7bb9dbd55e8ce3c9eb00936082421baa7aa64250c77570d9790f`

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
