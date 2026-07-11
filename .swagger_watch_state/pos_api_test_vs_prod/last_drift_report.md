# TEST vs PROD drift detected: POS API

- Time: 2026-07-11T01:15:20Z
- Severity: breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fcb4d56cc7c378cbae50765eb8d30f75210e37b92811a955d571853a6ea8679d`
- PROD hash: `56c233576dcecf291e9c6f43833247d57bf4f208c166298ffeec3d3c5a06b605`

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
