# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-15T10:31:12Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `de3fc45fe3b98d87b545d1c36b53503a38f890167bd6b2bf3c2e9e1dec9ee116`
- PROD hash: `8d92d1d55a1de60e455049fded7b491dcb2bd7d82cb8913afbfb289f7b81277f`

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
