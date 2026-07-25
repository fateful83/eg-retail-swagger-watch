# TEST vs PROD drift detected: POS API

- Time: 2026-07-25T18:44:09Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `221c215484de4125e0ca747c4ade0db0df004caf7174398bacde4d6bb4c1c2b4`
- PROD hash: `de2cdf3436cc2160110b3e4f016ebf8eff841dfdd06538357a0038dcc9d6b0a4`

## Summary
- Only in TEST: 0
- Only in PROD: 7
- Present in both but different: 0

## Only in TEST
- None

## Only in PROD
- POST /api/Order/queue/Basic
- POST /api/Order/queue/Complete
- POST /api/Order/queue/Delivery
- POST /api/Order/queue/ItemTransaction
- POST /api/Order/queue/OrderPayments
- POST /api/Order/queue/Payment
- POST /api/Order/queue/Sale

## Different in TEST and PROD
- None
