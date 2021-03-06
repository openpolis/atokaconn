# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](<http://keepachangelog.com/en/1.0.0/>)
and this project adheres to [Semantic Versioning](<http://semver.org/spec/v2.0.0.html>).

## [0.1.7]

### Fixed
- tests responses are mocked and do not have request attributes, so its existance is checked
  to avoid tests failures

## [0.1.6]
- empty results in get_response_from_ids returned as a dict, not a list

## [0.1.5]
- typer-cli added to dev-dependencies (helps generating docs)
- atokaconn.cli package contains source code for the cli

## [0.1.4] 
- allower_roles added as attribute to AtokaConn class

## [0.1.0] Initial release

### Added
- initial commit, documentation (README), license, metadata
- `get_people_from_atoka_ids`
- `get_people_from_tax_ids`
- `get_companies_from_atoka_ids`
- `get_companies_from_tax_ids`
- `get_roles_from_atoka_ids`
- tests