# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-02T01:31:25Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e915c8359ed64a385e6b4af645ee678aba2a6c289af34f52b3d5a3c96afb00ed`
- PROD hash: `bd89adec37ef4e22291ff6460ec055342a167902d9559a7bde6320867250afd8`

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
