# TEST vs PROD drift detected: POS API

- Time: 2026-06-09T19:51:02Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `7179ee1bf992e6d83af18e9c8bef72116076b4d5b5227a7c42c5580ead4ba253`
- PROD hash: `5b5d1483b15eb20f0063af5458787fffb5c1709285ec5b976eb449fb954842fc`

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
