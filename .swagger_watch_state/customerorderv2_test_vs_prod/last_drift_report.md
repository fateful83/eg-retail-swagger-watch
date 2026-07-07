# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-07T19:28:14Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ba199e3bbf3794acd2a05bff820c0b752dee4d17f0aed6d3e2b6bbeea3e68557`
- PROD hash: `2f826976759b0595eb55dbc660891000477d801007a000790be184aa7c7983d2`

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
