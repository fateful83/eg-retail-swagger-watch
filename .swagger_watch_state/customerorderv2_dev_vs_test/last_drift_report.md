# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-11-25T16:12:52Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `a55e448bfef25a805ec7c779cbe844e47b52827c8c6302d09a800573f300f6af`
- TEST hash: `ecf994f4f77c7fad505205b162c92c9cb7dee55b3d6b9556a0566478c3c7695a`

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
