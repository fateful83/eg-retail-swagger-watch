# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-06T01:30:55Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2ace897188a86253c63845694c21582763e57440759e58442aaa9e61d56a9f2f`
- PROD hash: `6ec6c2ce2237f60a6f3cfdf37b1c5dbfa11bbc29d9b2e915bd31e049be7052e1`

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
