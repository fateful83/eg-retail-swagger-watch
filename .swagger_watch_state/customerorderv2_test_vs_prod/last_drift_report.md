# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-13T13:15:51Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `91ffb771d90a76085a53af2c052919f04f59b93ad7940ebbe3c42a17671c7c0b`
- PROD hash: `afe7d5932be2b16d5d2867df7c51406104a5b626c09e16598c010595815a06d3`

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
