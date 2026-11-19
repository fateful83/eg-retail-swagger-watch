# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-19T14:45:13Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `0cf471f7d0432d6c7339246cfd1103b875543d5c945aa082fe5b434c09c706e9`
- TEST hash: `d40ed121346251797b56fa6c71a5d97fd155700b353d4f4a5dad299d660a1690`

## Summary
- Only in DEV: 1
- Only in TEST: 0
- Present in both but different: 1

## Only in DEV
- POST /api/gateway/Orders/search

## Only in TEST
- None

## Different in DEV and TEST
- GET /api/gateway/Orders
