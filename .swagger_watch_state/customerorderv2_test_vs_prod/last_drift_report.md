# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-13T07:05:11Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `6049a64309d9fc143d3edb8fe606111ab10e658949e2640e9f305e1a42b060ba`
- PROD hash: `849d22be79a577ce541921539bb93a560149aa1c5346623630ef334a90e05b2a`

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
