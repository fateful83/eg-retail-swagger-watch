# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-18T07:21:35Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b825903bad54cb12ba6d68f387ef4a6332c96bc6552b2c03448ce7c267693dd0`
- PROD hash: `08d5921c170dd127e4f488de898a5a63d155ae22e82796fc5c4307fc45974cbf`

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
