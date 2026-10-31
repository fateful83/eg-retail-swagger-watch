# TEST vs PROD drift detected: POS API

- Time: 2026-10-31T11:17:08Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0d2635bc1527b515dddb61a6cebc5672caa34661d4dfd1acafc7832ca3568457`
- PROD hash: `bec0250ed66fe920cf2e3c3a52f086f8dda7b50a3770f7158336c95317e0f943`

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
