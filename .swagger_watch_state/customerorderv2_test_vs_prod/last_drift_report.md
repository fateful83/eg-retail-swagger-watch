# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-29T11:50:32Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3f11b763ecca48b37abadb329e0acdcdfeb76095909b2f314fdf5d4ed417b78f`
- PROD hash: `fec8ad02236bcc2893e0bdeaac7bd98228eeeb979967b05b938ee74db8601764`

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
