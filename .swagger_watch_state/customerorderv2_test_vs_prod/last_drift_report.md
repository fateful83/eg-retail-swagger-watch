# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-17T10:19:54Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `68bc11f5f960c36a60053c5c05ba782789632282ed44ddc5a0338d71e4af1b2e`
- PROD hash: `a12faae719c14f22a32767c4d91a2347dec3f5e810d34280e1a74a1a0803ed99`

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
