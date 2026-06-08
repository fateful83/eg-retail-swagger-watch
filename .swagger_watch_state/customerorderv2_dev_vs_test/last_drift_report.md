# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-08T02:08:00Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `dec0a2fc6c7e7d40ca46278c1c519f38e0fca4d75b4b9c79483a9e0eba3621d6`
- TEST hash: `1cfb5f8debfb44923e2e62d0821e3c43c3c389dcbcc789f27a2261021b236acc`

## Summary
- Only in DEV: 1
- Only in TEST: 0
- Present in both but different: 0

## Only in DEV
- PATCH /api/gateway/ServiceOrders/{orderNumber}/order-status

## Only in TEST
- None

## Different in DEV and TEST
- None
