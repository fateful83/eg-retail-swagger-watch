# TEST vs PROD drift detected: ItemService

- Time: 2026-11-09T03:06:25Z
- Severity: breaking
- TEST Swagger URL: https://itemservice.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://itemservice.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a1877a1f177c17284a9c75c1ccae4ab05cfe981b83665ad6530ce83b9e50315f`
- PROD hash: `8376fb7312c08810d261e77335819ddccaf311a869c5a85a6b1bd3b36f7a5823`

## Summary
- Only in TEST: 0
- Only in PROD: 20
- Present in both but different: 0

## Only in TEST
- None

## Only in PROD
- DELETE /api/Collections/{id}
- DELETE /api/ServiceLevels/{id}
- GET /api/Collections
- GET /api/Collections/{id}
- GET /api/MarketingExclusivities
- GET /api/MarketingExclusivities/{id}
- GET /api/ServiceLevels
- GET /api/ServiceLevels/{id}
- POST /api/Collections
- POST /api/Collections/{id}/ToggleIsActive
- POST /api/Collections/{id}/ToggleIsDefault
- POST /api/MarketingExclusivities
- POST /api/MarketingExclusivities/{id}/ToggleIsActive
- POST /api/MarketingExclusivities/{id}/ToggleIsDefault
- POST /api/ServiceLevels
- POST /api/ServiceLevels/{id}/ToggleIsActive
- POST /api/ServiceLevels/{id}/ToggleIsDefault
- PUT /api/Collections/{id}
- PUT /api/MarketingExclusivities/{id}
- PUT /api/ServiceLevels/{id}

## Different in TEST and PROD
- None
