# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-16T10:11:32Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `28eb3abb8325bea3ab4e6b70acf3df8656abf715b694bc1bcf89b5fe2f6a0d58`
- PROD hash: `df6cb111534d0f7bae91208e19ee5ea92e4a3be1dda0156edf970ad44ab0cd65`

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
