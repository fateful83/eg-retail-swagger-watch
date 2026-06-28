# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-28T18:57:31Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9bf0d43ceecc606f997a33b15a9773940b2b427eb4a6ec35b1bfea7882c84df3`
- PROD hash: `ca2cea789158a0b2398a8edfe46d4d7ea2464f047fae47b4aa49ad9dfc83ae50`

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
