# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-11T20:03:59Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `4893b6f5e3ba7f5207689f8858b124d3d7605fe793a4b225dc5fb389214addff`
- TEST hash: `6abe28a348061a95147ea911fee37dad2fac82719f4e32eaf079a2059eecc26f`

## Summary
- Only in DEV: 1
- Only in TEST: 0
- Present in both but different: 1

## Only in DEV
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Only in TEST
- None

## Different in DEV and TEST
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
