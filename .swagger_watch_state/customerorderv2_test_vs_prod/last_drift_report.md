# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-11-02T13:58:29Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f148c67f19c751d698aa2c3f1b60e8a73e5329ab5e78e28a31b2fa04ddb46ecb`
- PROD hash: `3545f292b72c04e3e58a63dc61997ca40afb256bb4e7b6bf793e8f4dd795d0c8`

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
