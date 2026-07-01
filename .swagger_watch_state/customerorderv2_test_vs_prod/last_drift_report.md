# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-01T13:58:36Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5a1ef5b9bc209ceb776d0b58eaf10ae3b469d5f58a53530e7eaf80040e75ced8`
- PROD hash: `444d432446d8f8943a60a779c04ee0af5d8e9ac35b0c119ff8273daa19e96bd9`

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
