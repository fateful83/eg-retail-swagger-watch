# TEST vs PROD drift detected: POS API

- Time: 2026-06-05T14:15:00Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4416d21d74134715eae514dc90613b9c4f62132a473992216631874157d2e7dd`
- PROD hash: `d27456ca9be80f5baafd115ae782fa6cc6971d44996e71da0cd160eab77be380`

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
