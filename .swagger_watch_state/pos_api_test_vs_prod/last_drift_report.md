# TEST vs PROD drift detected: POS API

- Time: 2026-10-29T17:38:29Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `474ab7e9a9bdbf7c61da747c78643f512d33e71bfd7746c749a155ad3f8c70c2`
- PROD hash: `14b0ab7c60fa54a6b5179437edde7f32d3dceef695cbb4ef4376213cc5191f9f`

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
