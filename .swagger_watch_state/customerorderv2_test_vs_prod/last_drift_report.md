# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-12T19:43:04Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `641b2b4436cc2306749165cdd3544bd727a2bf4adb9f80ae8b813a866841381d`
- PROD hash: `96b4bac75a3840afaf0f839aa86f5e06e98326f1373fb950ee9528063e7fccdc`

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
