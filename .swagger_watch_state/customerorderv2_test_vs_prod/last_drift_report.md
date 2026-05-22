# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-22T14:06:15Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `1d676565200e1e628574d451e045f54006c4c3522a0a08a1ddb25847fe2a2f52`
- PROD hash: `42e9dc4f3b2cbca6be49275cf0419c9aace23e2f5636b540f1127126a162745d`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- GET /api/gateway/ServiceOrders/{storeNumber}

## Only in PROD
- None

## Different in TEST and PROD
- None
