# TEST vs PROD drift detected: POS API

- Time: 2026-06-07T19:01:00Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fc2c50161d021ed9de515b737a5d4a90c4d53b1c68e19664b8f7b202172ed749`
- PROD hash: `dd7a81fd71a97a6050877c107bd9c27dd210f76258c11169b1ada4c386c4a81f`

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
