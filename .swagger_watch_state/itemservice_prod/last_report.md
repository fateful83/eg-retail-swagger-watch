# Swagger/OpenAPI change detected: ItemService [PROD]

- Time: 2026-03-11T14:21:11Z
- Swagger URL: https://itemservice.egretail.cloud/swagger/v1/swagger.json
- Previous hash: `8eb10cad53ce0abb476923019730c46be0e2c942b387eac187226c9fe39c5583`
- Current hash: `f9c7e9608fc43adbe29e64dee2db20c086e35e6d61a6d3c1b58642916401afda`

## Summary
- Status: breaking
- Added operations: 0
- Removed operations: 0
- Changed operations: 48
- Breaking removed operations: 0
- Breaking changed operations: 42
- Non-breaking changed operations: 6

## Added
- None

## Removed
- None

## Changed
- GET /api/Brands
- GET /api/Brands/{id}
- GET /api/Collections
- GET /api/Collections/{id}
- GET /api/ItemCategories
- GET /api/ItemCategories/{id}
- GET /api/ItemLists
- GET /api/MarketingCodes
- GET /api/MarketingCodes/{id}
- GET /api/MarketingExclusivities
- GET /api/MarketingExclusivities/{id}
- GET /api/NonsaleType
- GET /api/Nutritions
- GET /api/ProcurementRules
- GET /api/ProcurementRules/{id}
- GET /api/ReplenishmentCodes
- GET /api/ReplenishmentCodes/{id}
- GET /api/Sizes
- GET /api/Sizes/{id}
- POST /api/Brands
- POST /api/Collections
- POST /api/Colors/upsertByName
- POST /api/Imports/{id}/filteredItemsCount
- POST /api/Imports/{id}/filteredItemsSimpleCount
- POST /api/Imports/{id}/import
- POST /api/Imports/{id}/reject
- POST /api/ItemCategories
- POST /api/ItemLists
- POST /api/MarketingCodes
- POST /api/MarketingExclusivities
- POST /api/NonsaleType
- POST /api/ProcurementRules
- POST /api/ReplenishmentCodes
- POST /api/Sizes
- POST /api/TradingUnits
- PUT /api/Brands/{id}
- PUT /api/Collections/{id}
- PUT /api/Concession/{id}/updateItemGroups
- PUT /api/ConcessionStores/{id}/updateStores
- PUT /api/ItemCategories/{id}
- PUT /api/ItemLists/{id}
- PUT /api/MarketingCodes/{id}
- PUT /api/MarketingExclusivities/{id}
- PUT /api/NonsaleType/{id}
- PUT /api/ProcurementRules/{id}
- PUT /api/ReplenishmentCodes/{id}
- PUT /api/Sizes/{id}
- PUT /api/TradingUnits/{id}

## Breaking classification
- Removed operations: 0
- None

- Breaking changed operations: 42
  - GET /api/Brands
  - GET /api/Brands/{id}
  - GET /api/Collections
  - GET /api/Collections/{id}
  - GET /api/ItemCategories
  - GET /api/ItemCategories/{id}
  - GET /api/ItemLists
  - GET /api/MarketingCodes
  - GET /api/MarketingCodes/{id}
  - GET /api/MarketingExclusivities
  - GET /api/MarketingExclusivities/{id}
  - GET /api/NonsaleType
  - GET /api/Nutritions
  - GET /api/ProcurementRules
  - GET /api/ProcurementRules/{id}
  - GET /api/ReplenishmentCodes
  - GET /api/ReplenishmentCodes/{id}
  - GET /api/Sizes
  - GET /api/Sizes/{id}
  - POST /api/Brands
  - POST /api/Collections
  - POST /api/Colors/upsertByName
  - POST /api/ItemCategories
  - POST /api/ItemLists
  - POST /api/MarketingCodes
  - POST /api/MarketingExclusivities
  - POST /api/NonsaleType
  - POST /api/ProcurementRules
  - POST /api/ReplenishmentCodes
  - POST /api/Sizes
  - POST /api/TradingUnits
  - PUT /api/Brands/{id}
  - PUT /api/Collections/{id}
  - PUT /api/ItemCategories/{id}
  - PUT /api/ItemLists/{id}
  - PUT /api/MarketingCodes/{id}
  - PUT /api/MarketingExclusivities/{id}
  - PUT /api/NonsaleType/{id}
  - PUT /api/ProcurementRules/{id}
  - PUT /api/ReplenishmentCodes/{id}
  - PUT /api/Sizes/{id}
  - PUT /api/TradingUnits/{id}

- Non-breaking changed operations: 6
  - POST /api/Imports/{id}/filteredItemsCount
  - POST /api/Imports/{id}/filteredItemsSimpleCount
  - POST /api/Imports/{id}/import
  - POST /api/Imports/{id}/reject
  - PUT /api/Concession/{id}/updateItemGroups
  - PUT /api/ConcessionStores/{id}/updateStores
