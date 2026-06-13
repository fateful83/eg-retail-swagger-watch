# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-13T19:02:30Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `caf5abc71fff7e5090c0561e891cffb78fdf2be1b82806045fa2dd8ce83d25b4`
- PROD hash: `a06c137cecd795e71a33dd607cf9de04d55f1033b571789f2e54b9f0d728195a`

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
