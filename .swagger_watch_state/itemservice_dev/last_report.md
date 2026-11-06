# Swagger/OpenAPI change detected: ItemService [DEV]

- Time: 2026-11-06T13:17:50Z
- Fetch completed at: 2026-11-06T13:17:49Z
- Fetch duration ms: 2067
- Swagger URL: https://itemservice.egretail-dev.cloud/swagger/v1/swagger.json
- Previous hash: `8376fb7312c08810d261e77335819ddccaf311a869c5a85a6b1bd3b36f7a5823`
- Current hash: `3659a666b6eafd51649e4863093687e661c92c1e30286074603f47a310c9fed8`

## Summary
- Status: breaking
- Added operations: 0
- Removed operations: 20
- Changed operations: 30
- Breaking removed operations: 20
- Breaking changed operations: 30
- Non-breaking changed operations: 0

## Added
- None

## Removed
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

## Changed
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

## Breaking classification
- Removed operations: 20
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

- Breaking changed operations: 30
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

- Non-breaking changed operations: 0
- None
