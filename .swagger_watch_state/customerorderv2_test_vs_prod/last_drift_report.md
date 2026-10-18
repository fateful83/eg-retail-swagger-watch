# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-18T14:56:28Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fbeb86631ec50fa2b79020184c80783c3674a41e93092aaa01025fdacf92d576`
- PROD hash: `f0606696ce081b1c29722a92c7f2db62cc1da169e5cc5e3e5a8794497e411f20`

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
