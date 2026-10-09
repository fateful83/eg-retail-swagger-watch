# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-09T21:54:49Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `462fae9c0bc6a1c40802da908404c3d13d00136e0abf694bb5df175f4a2d018f`
- PROD hash: `bb4c3f4e751e4b6d96a9b531b6804067bfe7396e973082dc2e10dca72f3187ed`

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
