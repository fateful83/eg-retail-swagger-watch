# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-29T02:50:06Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4eaa06d1be859dcf1b217649ec5e2def7221996f36841b1ce326b115b1ff3e83`
- PROD hash: `02897f60ef51775a27f48d5a1aaff5f8c31dcffb91ea59c7e120073eb7909b01`

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
