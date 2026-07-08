# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-08T19:00:03Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `57e7a3fc6b63dd4de3bd4d802ce86a2d9743dee700b8c5a96aa763ef6d526673`
- PROD hash: `052138b39897bfe3af21325d48939cfbaed6a4552795a7d4fdf72ce7866bb682`

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
