# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-05T13:27:55Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `21fa3911f2cda44eaa8c367a49409115a280f2d0695cf4432efbb20c4f3c13ac`
- PROD hash: `5fb28f80f480525304ba925c3619191b8e2910c319e1fa707038c1cf71bfd491`

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
