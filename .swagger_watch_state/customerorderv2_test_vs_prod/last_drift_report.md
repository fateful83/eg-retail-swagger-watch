# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-12T14:26:01Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d70b1aac48acbe1bd87c51b76479d6029049552202f04d985c065f731fe3eac5`
- PROD hash: `e74161db21d14c9a79a838b35de333d22b09440019973970bcc089c3d99ae1f4`

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
