# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-22T10:24:52Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `dc9409d21a034cd8448fb9f0970b288630c3cca0f01622d4d22372eaa610c67c`
- PROD hash: `5f418358950c6199939de45e9ff3e37babe72bf2ae34f4dafb5ad36250c210cf`

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
