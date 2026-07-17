# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-17T12:53:49Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `87966b216294447bc1f58cea3b43ab20bce8ceda8e4c5053627f5baa3935ded5`
- PROD hash: `4d072536d06981f145a00f92067d3cba2b15b442e5b32aa5cfe5dc035d19ab3a`

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
