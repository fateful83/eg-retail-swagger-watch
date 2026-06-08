# TEST vs PROD drift detected: POS API

- Time: 2026-06-08T19:55:21Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8da14d529ed06f592a46b9ff6bb3dc1eba56e13473fa4ccab7a5d7df490cf3db`
- PROD hash: `31dd29e6adc915ef18d209f4019257a5c44a16be010d367128c432a45fb3dce4`

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
