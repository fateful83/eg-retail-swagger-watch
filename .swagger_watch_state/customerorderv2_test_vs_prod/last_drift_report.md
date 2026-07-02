# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-02T08:36:59Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0b74ee0f542f0a1b7526b4fdc7dda68c899fe5418d359985a90ca1a27012bde6`
- PROD hash: `043b564203b0f363ab41c7361308e19158e28af087e3fe0f2a11f9595ff4127d`

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
