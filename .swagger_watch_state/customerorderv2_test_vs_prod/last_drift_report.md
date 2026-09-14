# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-14T17:05:42Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `5a00c34bd4e749ee64e473e1c5d12bb78a027e9231a78890d85c27b08965a09b`
- PROD hash: `5272d23bff775eed4c40614c011cbb5d77d043455efc5a321032b5a311826de4`

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
