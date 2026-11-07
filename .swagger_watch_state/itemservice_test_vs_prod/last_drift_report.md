# TEST vs PROD drift detected: ItemService

- Time: 2026-11-07T03:19:48Z
- Severity: breaking
- TEST Swagger URL: https://itemservice.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://itemservice.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a1877a1f177c17284a9c75c1ccae4ab05cfe981b83665ad6530ce83b9e50315f`
- PROD hash: `433a2f731c525cc82775827fff2cb6e04fc76eb22d831a7770a4771bf174e76d`

## Summary
- Only in TEST: 0
- Only in PROD: 20
- Present in both but different: 30

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
- GET /api/Brands
- GET /api/Brands/{id}
- GET /api/ItemCategories
- GET /api/ItemCategories/{id}
- GET /api/ItemLists
- GET /api/NonsaleType
- GET /api/Nutritions
- GET /api/ProcurementRules
- GET /api/ProcurementRules/{id}
- GET /api/ReplenishmentCodes
- GET /api/ReplenishmentCodes/{id}
- GET /api/Sizes
- GET /api/Sizes/{id}
- POST /api/Brands
- POST /api/Colors/upsertByName
- POST /api/ItemCategories
- POST /api/ItemLists
- POST /api/NonsaleType
- POST /api/ProcurementRules
- POST /api/ReplenishmentCodes
- POST /api/Sizes
- POST /api/TradingUnits
- PUT /api/Brands/{id}
- PUT /api/ItemCategories/{id}
- PUT /api/ItemLists/{id}
- PUT /api/NonsaleType/{id}
- PUT /api/ProcurementRules/{id}
- PUT /api/ReplenishmentCodes/{id}
- PUT /api/Sizes/{id}
- PUT /api/TradingUnits/{id}
