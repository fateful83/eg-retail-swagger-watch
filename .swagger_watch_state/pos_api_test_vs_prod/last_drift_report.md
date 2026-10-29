# TEST vs PROD drift detected: POS API

- Time: 2026-10-29T11:50:44Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `773c37bde80eb5c9ed17d284d98f42da13153380e4a4e2e54f24523639c4b084`
- PROD hash: `a89b82a03cfc1f0eada42166b4df1d8f56bd4b8d4afcfd619a9a6ad4f505d7df`

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
