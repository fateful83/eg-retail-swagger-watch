# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-29T17:38:16Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f6cc73ac7456d8051c18fd29aba5dfd7cebbb17baea7e553a3616c66dd40ce3a`
- PROD hash: `68cfb799b1929bf239e59c36bf14625dd51d99fadb30966fe0193a12e5e54286`

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
