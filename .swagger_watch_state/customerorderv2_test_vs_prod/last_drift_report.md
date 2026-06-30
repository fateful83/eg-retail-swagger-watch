# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-30T19:26:17Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a9df45762b2f3a7ac6d91d4b252fcc423adcfb530041b4c56cfa1d61ac069fdd`
- PROD hash: `e327d6a0268d49a1f8f3947101b9a5cd8668b9b443fc792dba5fcc2aee951377`

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
