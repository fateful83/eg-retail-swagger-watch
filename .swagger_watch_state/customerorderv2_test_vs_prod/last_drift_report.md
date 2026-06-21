# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-06-21T09:30:42Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `34d6202d16acaaf6a5c2ba895fecf09d66c3ceee0302269f0d8cc9e01e4c6864`
- PROD hash: `4241164b26692bff6f8fdd8cd7f3238c7f9a1cf2d99b32774842856454dbec6f`

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
