# TEST vs PROD drift detected: POS API

- Time: 2026-06-02T02:08:40Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `c480f3c0bbe882b8dbda1b9f39873f66c15bc7dab6c0cf83dfe1a55d3c1a309d`
- PROD hash: `1cdde831e56d303ea5bae85b50bfc7d56ea9668dfc31cb2de123aeebb0e46ef1`

## Summary
- Only in TEST: 2
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- POST /api/Payment/BeginKlarnaPayment
- POST /api/Payment/EndKlarnaPayment

## Only in PROD
- None

## Different in TEST and PROD
- None
