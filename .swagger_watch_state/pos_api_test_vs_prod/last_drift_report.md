# TEST vs PROD drift detected: POS API

- Time: 2026-11-01T12:06:55Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `96463f61310682fec015fb1308fc3e6f0728232d3b65c94aca2786c24f095291`
- PROD hash: `c627e2b476d2c12fdf04b57d5248d64248d87b832a6647c79abac2ddaa53a5e0`

## Summary
- Only in TEST: 3
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- GET /api/UserService/PingHealth
- POST /api/UserService/Authenticate
- POST /api/UserService/CheckUserExists

## Only in PROD
- None

## Different in TEST and PROD
- None
