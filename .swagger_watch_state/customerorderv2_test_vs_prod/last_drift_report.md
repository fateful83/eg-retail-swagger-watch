# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-21T21:16:25Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `46d8a425208700d0a2fdb5ae7ef5a856a3a5c4a25fa3b457bd504ab958970b29`
- PROD hash: `26d1f0d38b368934b662b10871a8ef3a729cb3af552eb440f5f3edf272240661`

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
