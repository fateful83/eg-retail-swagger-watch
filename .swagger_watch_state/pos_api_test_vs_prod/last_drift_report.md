# TEST vs PROD drift detected: POS API

- Time: 2026-06-05T19:25:17Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `af764774e576eab69fc0f2527ac500e73e32bd75c5af56072d16dd063da4a851`
- PROD hash: `62ade07c68b83bf2694ace20109f43763e1cf726e6db2d15fcd9902b52f55107`

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
