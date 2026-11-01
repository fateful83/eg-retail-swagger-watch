# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-11-01T21:24:34Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `878243656a8973d1cb2836c758353e3bf08e81c934697a47469170cbf0929d41`
- PROD hash: `c386b71c4ba607b952c883b860e78ccf6a815060b34bed685c70e64cf0fe00f9`

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
