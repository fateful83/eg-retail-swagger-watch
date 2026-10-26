# DEV vs TEST drift detected: POS API

- Time: 2026-10-26T17:41:46Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `ce3cc0b4ae848714eac844feb3b13f92b69fca93290028d1e6df1a540b4ec802`
- TEST hash: `5c960cb2e374dd0ba2f28f7ee2d77a861f524e86d3ee8916f96e6172b7d63a56`

## Summary
- Only in DEV: 3
- Only in TEST: 0
- Present in both but different: 0

## Only in DEV
- GET /api/UserService/PingHealth
- POST /api/UserService/Authenticate
- POST /api/UserService/CheckUserExists

## Only in TEST
- None

## Different in DEV and TEST
- None
