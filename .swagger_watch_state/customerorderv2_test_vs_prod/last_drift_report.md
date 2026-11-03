# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-11-03T13:03:57Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `87d66239bb07d4b05e376f7e53fb7842da84374bc445fac3a87b1b9deba13f47`
- PROD hash: `4ad4128c4a963629ec0da5538f467741b9d34465d0e270d23d56b86bb3bb0f0d`

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
