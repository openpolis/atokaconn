from faker import Factory


faker = Factory.create("it_IT")  # a factory to create fake data for tests


def get_person_ok(tax_id=None, search_params=None):
    """Return a python dict simulating an ok response from ATOKA"""

    if search_params:
        family_name = search_params['family_name']
        given_name = search_params['given_name']
        birth_date = search_params['birth_date']
    else:
        family_name = faker.last_name_male()
        given_name = faker.first_name_male()
        birth_date = faker.date(pattern="%Y-%m-%d", end_datetime="-47y")

    gender = "M"
    name = "{0} {1}".format(given_name, family_name)

    if not tax_id:
        tax_id = faker.ssn()

    return {
        "items": [{
            "base": {
                "familyName": family_name,
                "givenName": given_name,
                "birthDate": birth_date,
                "birthPlace": {
                    "macroregion": "Centro",
                    "municipality": "Roma",
                    "province": "Roma",
                    "provinceCode": "RM",
                    "region": "Lazio",
                    "state": "Italia",
                    "stateCode": "IT"
                },
                "gender": gender,
                "taxId": tax_id
            },
            "country": "it",
            "id": faker.uuid4(),
            "name": name,
            "obfuscated": False,
        }],
        "meta": {"count": 1, "limit": 10, "offset": 0, "ordering": "birthDateDesc"}
    }


def get_void_response():
    return {
      "response": {},
      "meta": {
        "count": 0,
        "error": 0,
        "success": 0,
      }
    }


def get_person_multiple(tax_id=None, search_params=None):
    """Return a python dict simulating a response with multiple items from ATOKA"""

    if search_params:
        family_name = search_params['family_name']
        given_name = search_params['given_name']
        birth_date = search_params['birth_date']
    else:
        family_name = faker.last_name_male()
        given_name = faker.first_name_male()
        birth_date = faker.date(pattern="%Y-%m-%d", end_datetime="-47y")

    gender = "M"
    name = "{0} {1}".format(given_name, family_name)

    if not tax_id:
        tax_id = faker.ssn()

    return {
        "items": [
            {
                "base": {
                    "familyName": family_name,
                    "givenName": given_name,
                    "birthDate": birth_date,
                    "birthPlace": {
                        "macroregion": "Centro",
                        "municipality": "Roma",
                        "province": "Roma",
                        "provinceCode": "RM",
                        "region": "Lazio",
                        "state": "Italia",
                        "stateCode": "IT"
                    },
                    "gender": gender,
                    "taxId": tax_id
                },
                "country": "it",
                "id": faker.uuid4(),
                "name": name,
                "obfuscated": False,
            },
            {
                "base": {
                    "familyName": family_name + " Maria",
                    "givenName": given_name,
                    "birthDate": birth_date,
                    "birthPlace": {
                        "macroregion": "Centro",
                        "municipality": "Roma",
                        "province": "Roma",
                        "provinceCode": "RM",
                        "region": "Lazio",
                        "state": "Italia",
                        "stateCode": "IT"
                    },
                    "gender": gender,
                    "taxId": tax_id
                },
                "country": "it",
                "id": faker.uuid4(),
                "name": name,
                "obfuscated": False,
            }
        ],
        "meta": {"count": 2, "limit": 10, "offset": 0, "ordering": "birthDateDesc"}
    }


def get_companies(tax_ids):
    """Return a python dict simulating a single response from ATOKA"""

    return {
        "80002270660": {
            "meta": {
                "count": 1,
                "error": 0,
                "success": 1,
            },
            "responses": {
                "80002270660": {
                    "items": [
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "govCode": "c_a345",
                            "govType": "Comuni e loro Consorzi e Associazioni",
                            "inGroup": True,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Soggetto non iscritto al Registro Imprese"
                              }
                            ],
                            "legalName": "COMUNE DI L'AQUILA",
                            "registeredAddress": {
                              "fullAddress": "Via F. Filomusi Guelfi, 67100, L'Aquila (AQ)",
                              "lat": 42.35161,
                              "latlonPrecision": 0,
                              "lon": 13.38522,
                              "macroregion": "Sud",
                              "municipality": "L'Aquila",
                              "postcode": "67100",
                              "province": "L'Aquila",
                              "provinceCode": "AQ",
                              "region": "Abruzzo",
                              "state": "Italia",
                              "streetName": "Via F. Filomusi Guelfi"
                            },
                            "startup": False,
                            "taxId": "80002270660",
                            "vat": "00082410663"
                          },
                          "country": "it",
                          "fullAddress": "Via F. Filomusi Guelfi, 67100, L'Aquila (AQ)",
                          "id": "73d7b304a070",
                          "name": "COMUNE DI L'AQUILA",
                          "shares": {
                            "beneficialOwnerOf": [
                              {
                                "active": True,
                                "id": "18d7ed1a320c",
                                "legalName": "S.E.D. SERVIZI ELABORAZIONE DATI S.P.A. CON SOCIO UNICO",
                                "name": "S.E.D. SERVIZI ELABORAZIONE DATI S.P.A. CON SOCIO UNICO"
                              },
                              {
                                "active": False,
                                "id": "2e5e366bff42",
                                "legalName": "AQUILAMBIENTE S.P.A. IN LIQUIDAZIONE",
                                "name": "AQUILAMBIENTE S.P.A. IN LIQUIDAZIONE"
                              }
                            ],
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 274380.0,
                                "id": "18d7ed1a320c",
                                "lastUpdate": "2013-05-21",
                                "legalName": "S.E.D. SERVIZI ELABORAZIONE DATI S.P.A. CON SOCIO UNICO",
                                "name": "S.E.D. SERVIZI ELABORAZIONE DATI S.P.A. CON SOCIO UNICO",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 52677.9,
                                "id": "2e5e366bff42",
                                "lastUpdate": "2003-04-30",
                                "legalName": "AQUILAMBIENTE S.P.A. IN LIQUIDAZIONE",
                                "name": "AQUILAMBIENTE S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        }
                    ],
                    "meta": {
                        "count": 1,
                        "limit": 50,
                        "offset": 0,
                        "ordering": "atoka"
                    }
                }
            }
        },
        "02438750586": {
            "meta": {
                "count": 2,
                "error": 0,
                "success": 2,
            },
            "responses": {
                "02438750586": {
                    "items": [
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "govCode": "c_h501",
                            "govType": "Comuni e loro Consorzi e Associazioni",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Soggetto non iscritto al Registro Imprese"
                              }
                            ],
                            "legalName": "COMUNE DI ROMA",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 0,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Piazza Del Campidoglio, 1"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "02438750586"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "2e45d55f8c71",
                          "name": "COMUNE DI ROMA"
                        }
                      ],
                    "meta": {
                        "count": 2,
                        "limit": 50,
                        "offset": 0,
                        "ordering": "atoka"
                    }
                }
            }
        },
        "01234567890": {
            "meta": {
                "count": 62,
                "error": 0,
                "success": 50,
            },
            "responses": {
                "01234567890": {
                    "items": [
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "ateco": [
                              {
                                "code": "01.11.1",
                                "description": "Coltivazione di cereali (escluso il riso)",
                                "rootCode": "A"
                              }
                            ],
                            "cciaa": "RM",
                            "founded": "1977-06-14",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Ente"
                              }
                            ],
                            "legalName": "ROMA CAPITALE",
                            "nace": [
                              {
                                "code": "01.11",
                                "description": "Growing of cereals (except rice), leguminous crops and oil seeds",
                                "rootCode": "A"
                              }
                            ],
                            "rea": "1287276",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 90,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Del Campidoglio",
                              "streetNumber": "1",
                              "toponym": "Piazza"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "01057861005"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "ea623ae8c298",
                          "name": "ROMA CAPITALE",
                          "shares": {
                            "sharesOwned": [
                              {
                                "active": True,
                                "amount": 182436916.0,
                                "id": "6037483d168e",
                                "lastUpdate": "2011-10-20",
                                "legalName": "AZIENDA MUNICIPALE AMBIENTE S.P.A. "
                                "ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "name": "AZIENDA MUNICIPALE AMBIENTE S.P.A. ROMA IN FORMA ABBREVIATA \"AMA S.P.A\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 10000000.0,
                                "id": "8f1c4be03ec9",
                                "lastUpdate": "2010-02-18",
                                "legalName": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "name": "ROMA SERVIZI PER LA MOBILITA' S.R.L.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2822250.0,
                                "id": "667243935e25",
                                "lastUpdate": "2005-11-24",
                                "legalName": "ZETEMA PROGETTO CULTURA SRL",
                                "name": "ZETEMA PROGETTO CULTURA SRL",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2500000.0,
                                "id": "0b10d523f972",
                                "lastUpdate": "2012-04-16",
                                "legalName": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE DELLA CITTA' "
                                "DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "name": "SOCIETA' PER LA REALIZZAZIONE DELLE METROPOLITANE "
                                "DELLA CITTA' DI ROMA A R.L. IN FORMA "
                                "ABBREVIATA \"ROMA METROPOLITANE S.R.L.\"",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 2000000.0,
                                "id": "a32e98206f27",
                                "lastUpdate": "2012-02-16",
                                "legalName": "RISORSE PER ROMA S.P.A.",
                                "name": "RISORSE PER ROMA S.P.A.",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 300000.0,
                                "id": "8c8179a19251",
                                "lastUpdate": "2005-10-14",
                                "legalName": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "name": "SERVIZI AZIONISTA ROMA S.R.L. A SOCIO UNICO IN LIQUIDAZIONE",
                                "ratio": 1.0,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": True,
                                "amount": 560438430.84,
                                "id": "b3f933d6a2df",
                                "lastUpdate": "2014-12-18",
                                "legalName": "ACEA S.P.A.",
                                "name": "ACEA S.P.A.",
                                "ratio": 0.51,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 2530638.81,
                                "id": "b61bd1a3a245",
                                "lastUpdate": "2000-04-28",
                                "legalName": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "name": "AGENZIA ROMANA PER LA PREPARAZIONE DEL GIUBILEO - SOCIETA' PER AZIONI",
                                "ratio": 0.35,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 190000.0,
                                "id": "2f3a4fd465f6",
                                "lastUpdate": "2006-05-18",
                                "legalName": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "name": "\"AGENZIA REGIONALE PER LA PROMOZIONE "
                                "TURISTICA DI ROMA E DEL LAZI O S.P.A. IN "
                                "LIQUIDAZIONE\" IN FORMA ABBREVIATA \"AGENZIA DEL "
                                "TURISMO S.P.A. IN LIQ UIDAZIONE\"",
                                "ratio": 0.19,
                                "typeOfRight": "propriet\u00e0"
                              },
                              {
                                "active": False,
                                "amount": 155738.0,
                                "id": "f11054c630fa",
                                "lastUpdate": "2014-06-05",
                                "legalName": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "name": "CENTRO INGROSSO FIORI S.P.A. ED IN FORMA ABBREVIATA "
                                "C.I.F. S.P.A. IN LIQUIDAZIONE",
                                "ratio": 0.08869999999999999,
                                "typeOfRight": "propriet\u00e0"
                              }
                            ]
                          }
                        },
                        {
                          "active": True,
                          "base": {
                            "active": True,
                            "govCode": "c_h501",
                            "govType": "Comuni e loro Consorzi e Associazioni",
                            "inGroup": False,
                            "legalClass": "Altre Forme",
                            "legalForms": [
                              {
                                "level": 1,
                                "name": "Altre Forme"
                              },
                              {
                                "level": 2,
                                "name": "Soggetto non iscritto al Registro Imprese"
                              }
                            ],
                            "legalName": "COMUNE DI ROMA",
                            "registeredAddress": {
                              "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                              "lat": 41.89334748,
                              "latlonPrecision": 0,
                              "lon": 12.48289836,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00186",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Piazza Del Campidoglio, 1"
                            },
                            "startup": False,
                            "taxId": "02438750586",
                            "vat": "02438750586"
                          },
                          "country": "it",
                          "fullAddress": "Piazza Del Campidoglio, 1, 00186, Roma (RM)",
                          "id": "2e45d55f8c71",
                          "name": "COMUNE DI ROMA"
                        }
                      ],
                    "meta": {
                        "count": 62,
                        "limit": 50,
                        "offset": 0,
                        "ordering": "atoka"
                    }
                }
            }
        },
    }[tax_ids]


def get_companies_economics():
    """Return values as if required through a requests to an atoka endpoint, with economics package specified

    :return:
    """
    return {
        "meta": {
            "count": 2,
            "error": 0,
            "success": 2,
        },
        "responses": {
            "02241890223,09988761004": {
                "meta": {"count": 2, "limit": 10, "offset": 0, "ordering": "atoka"},
                "items": [
                    {
                        "active": True,
                        "base": {
                            "active": True,
                            "ateco": [
                                {
                                    "code": "62.01.00",
                                    "description": "Produzione di software non connesso all'edizione",
                                    "rootCode": "J"
                                }
                            ],
                            "cciaa": "TN", "founded": "2012-02-13", "inGroup": True,
                            "legalClass": "Societ\u00e0 Di Capitale",
                            "legalForms": [
                                {"level": 1, "name": "Societ\u00e0 Di Capitale"},
                                {"level": 2, "name": "Societ\u00e0 A Responsabilit\u00e0 Limitata"}
                            ],
                            "legalName": "SPAZIODATI S.R.L.",
                            "nace": [
                                {"code": "62.01", "description": "Computer programming activities", "rootCode": "J"}
                            ],
                            "rea": "210089",
                            "registeredAddress": {
                                "fullAddress": "Via Adriano Olivetti, 13, 38122, Trento (TN)",
                                "lat": 46.06248902, "latlonPrecision": 60, "lon": 11.10780205,
                                "macroregion": "Nord-est", "municipality": "Trento", "postcode": "38122",
                                "province": "Trento", "provinceCode": "TN",
                                "region": "Trentino-Alto Adige/S\u00fcdtirol", "state": "Italia",
                                "streetName": "Adriano Olivetti", "streetNumber": "13", "toponym": "Via"
                            },
                            "startup": False,
                            "taxId": "02241890223",
                            "vat": "02241890223"
                        },
                        "country": "it",
                        "economics": {
                            "balanceSheets": [
                                {"capitalStock": 22000, "currency": "EUR",
                                 "date": "2017-12-31",
                                 "latest": True,
                                 "revenue": 2778000, "revenueTrend": 0.8120999999999999, "year": 2017},
                                {"capitalStock": 22000, "currency": "EUR",
                                 "date": "2016-12-31",
                                 "revenue": 1533000, "revenueTrend": 2.3254, "year": 2016},
                                {"capitalStock": 18000, "currency": "EUR",
                                 "date": "2015-12-31",
                                 "revenue": 461000, "revenueTrend": 0.8970999999999999, "year": 2015},
                                {"capitalStock": 15000, "currency": "EUR",
                                 "date": "2014-12-31",
                                 "revenue": 243000,
                                 "revenueTrend": 0.7868, "year": 2014},
                                {"capitalStock": 12000, "currency": "EUR",
                                 "date": "2013-12-31",
                                 "revenue": 136000,
                                 "revenueTrend": 0.7436, "year": 2013},
                                {"capitalStock": 11000, "currency": "EUR",
                                 "date": "2012-12-31",
                                 "revenue": 65000, "year": 2012}
                             ],
                            "capitalStock": {"value": 21638},
                            "employees": [
                                {"date": "2018-09-01", "latest": True, "value": 27, "year": 2018},
                                {"date": "2018-06-01", "latest": False, "value": 27, "year": 2018},
                                {"date": "2018-03-01", "latest": False, "value": 27, "year": 2018},
                                {"date": "2017-12-01", "latest": False, "value": 26, "year": 2017},
                                {"date": "2017-09-01", "latest": False, "value": 25, "year": 2017},
                                {"date": "2017-06-01", "latest": False, "value": 23, "year": 2017},
                                {"date": "2017-03-01", "latest": False, "value": 22, "year": 2017},
                                {"date": "2016-12-01", "latest": False, "value": 18, "year": 2016},
                                {"date": "2016-09-01", "latest": False, "value": 17, "year": 2016},
                                {"date": "2016-06-01", "latest": False, "value": 17, "year": 2016},
                                {"date": "2016-03-01", "latest": False, "value": 17, "year": 2016},
                                {"date": "2015-12-01", "latest": False, "value": 13, "year": 2015},
                                {"date": "2015-09-01", "latest": False, "value": 10, "year": 2015},
                                {"date": "2015-06-01", "latest": False, "value": 7, "year": 2015},
                                {"date": "2015-03-01", "latest": False, "value": 6, "year": 2015},
                                {"date": "2014-12-01", "latest": False, "value": 5, "year": 2014},
                                {"date": "2014-09-01", "latest": False, "value": 4, "year": 2014},
                                {"date": "2014-06-01", "latest": False, "value": 4, "year": 2014},
                                {"date": "2014-03-01", "latest": False, "value": 3, "year": 2014}
                            ],
                            "public": False
                        },
                        "fullAddress": "Via Adriano Olivetti, 13, 38122, Trento (TN)",
                        "id": "6da785b3adf2",
                        "name": "SPAZIODATI S.R.L."
                    },
                    {
                        "active": True,
                        "base": {
                            "active": True,
                            "ateco": [
                                {"code": "63.12.00", "description": "Portali web", "rootCode": "J"}
                            ],
                            "cciaa": "RM",
                            "founded": "2008-04-24",
                            "inGroup": False,
                            "legalClass": "Societ\u00e0 Di Capitale",
                            "legalForms": [
                                {"level": 1, "name": "Societ\u00e0 Di Capitale"},
                                {"level": 2, "name": "Societ\u00e0 A Responsabilit\u00e0 Limitata"}
                            ],
                            "legalName": "DEPP SRL",
                            "nace": [
                                {"code": "63.12", "description": "Web portals", "rootCode": "J"}
                            ],
                            "rea": "1201904",
                            "registeredAddress": {
                              "fullAddress": "Via "
                              "Merulana, 19, 00185, "
                              "Roma (RM)",
                              "lat": 41.89625,
                              "latlonPrecision": 90,
                              "lon": 12.49967,
                              "macroregion": "Centro",
                              "municipality": "Roma",
                              "postcode": "00185",
                              "province": "Roma",
                              "provinceCode": "RM",
                              "region": "Lazio",
                              "state": "Italia",
                              "streetName": "Merulana",
                              "streetNumber": "19",
                              "toponym": "Via"
                            },
                            "startup": False,
                            "taxId": "09988761004",
                            "vat": "09988761004"
                        },
                        "country": "it",
                        "economics": {
                            "balanceSheets": [
                                {"assets": 172000, "capitalStock": 10000, "costs": 442000, "currency": "EUR",
                                 "date": "2017-12-31",
                                 "ebitda": 25000, "latest": True, "mol": 29000, "netFinancialPosition": 7000,
                                 "production": 471000,
                                 "profit": 12000, "purchases": 0, "rawMaterialsVariation": 0, "revenue": 471000,
                                 "revenueTrend": 0.09789999999999999, "servicesAndTPGoodsCharges": 285000,
                                 "staffCosts": 157000, "year": 2017},
                                {"assets": 158000, "capitalStock": 10000, "costs": 389000, "currency": "EUR",
                                 "date": "2016-12-31",
                                 "ebitda": 31000, "latest": False, "mol": 40000, "netFinancialPosition": -28000,
                                 "production": 429000,
                                 "profit": 12000, "purchases": 0, "rawMaterialsVariation": 0, "revenue": 429000,
                                 "revenueTrend": 0.0239,
                                 "servicesAndTPGoodsCharges": 253000, "staffCosts": 136000, "year": 2016},
                                {"assets": 114000, "capitalStock": 10000, "costs": 422000, "currency": "EUR",
                                 "date": "2015-12-31",
                                 "ebitda": -10000, "latest": False, "mol": -3000, "netFinancialPosition": -33000,
                                 "production": 419000,
                                 "profit": 18000, "purchases": 0, "rawMaterialsVariation": 0, "revenue": 419000,
                                 "revenueTrend": 0.3176,
                                 "servicesAndTPGoodsCharges": 311000, "staffCosts": 111000, "year": 2015},
                                {"assets": 101000, "capitalStock": 10000, "costs": 289000, "currency": "EUR",
                                 "date": "2014-12-31",
                                 "ebitda": 23000, "latest": False, "mol": 29000, "netFinancialPosition": -13000,
                                 "production": 318000,
                                 "profit": 19000, "purchases": 0, "rawMaterialsVariation": 0, "revenue": 318000,
                                 "revenueTrend": 0.2927,
                                 "servicesAndTPGoodsCharges": 234000, "staffCosts": 55000, "year": 2014},
                                {"assets": 90000, "capitalStock": 10000, "costs": 295000, "currency": "EUR",
                                 "date": "2013-12-31",
                                 "ebitda": -55000, "latest": False, "mol": -49000, "netFinancialPosition": -38000,
                                 "production": 246000,
                                 "profit": 6000, "purchases": 0, "rawMaterialsVariation": 0, "revenue": 246000,
                                 "revenueTrend": -0.1119,
                                 "servicesAndTPGoodsCharges": 282000, "staffCosts": 13000, "year": 2013},
                                {"assets": 118000, "capitalStock": 10000, "costs": 253000, "currency": "EUR",
                                 "date": "2012-12-31",
                                 "ebitda": 20000, "latest": False, "mol": 24000, "netFinancialPosition": -12000,
                                 "production": 277000,
                                 "profit": 11000, "purchases": 0, "rawMaterialsVariation": 0, "revenue": 277000,
                                 "revenueTrend": 1.0368000000000002,
                                 "servicesAndTPGoodsCharges": 253000, "staffCosts": 0,
                                 "year": 2012},
                                {"assets": 53000, "capitalStock": 10000, "costs": 132000, "currency": "EUR",
                                 "date": "2011-12-31",
                                 "ebitda": 2000, "latest": False, "mol": 4000, "netFinancialPosition": -24000,
                                 "production": 136000,
                                 "profit": -3000, "purchases": 0, "rawMaterialsVariation": 0, "revenue": 136000,
                                 "revenueTrend": -0.049,
                                 "servicesAndTPGoodsCharges": 132000, "staffCosts": 0, "year": 2011},
                                {"assets": 72000, "capitalStock": 10000, "costs": 139000, "currency": "EUR",
                                 "date": "2010-12-31",
                                 "ebitda": 2000, "latest": False, "mol": 4000, "netFinancialPosition": -23000,
                                 "production": 143000,
                                 "profit": -1000, "purchases": 1000, "rawMaterialsVariation": 0, "revenue": 143000,
                                 "revenueTrend": 0.1,
                                 "servicesAndTPGoodsCharges": 138000, "staffCosts": 0, "year": 2010},
                                {"assets": 105000, "capitalStock": 10000, "costs": 129000, "currency": "EUR",
                                 "date": "2009-12-31",
                                 "ebitda": 3000, "latest": False, "mol": 5000, "netFinancialPosition": -6000,
                                 "production": 134000,
                                 "profit": 1000, "purchases": 0, "rawMaterialsVariation": 0, "revenue": 130000,
                                 "revenueTrend": 1.2807,
                                 "servicesAndTPGoodsCharges": 129000, "staffCosts": 0, "year": 2009},
                                {"assets": 41000, "capitalStock": 10000, "costs": 36000, "currency": "EUR",
                                 "date": "2008-12-31",
                                 "ebitda": 1000, "latest": False, "mol": 2000, "netFinancialPosition": -17000,
                                 "production": 38000, "profit": 0,
                                 "purchases": 0, "rawMaterialsVariation": 0, "revenue": 38000,
                                 "servicesAndTPGoodsCharges": 36000,
                                 "staffCosts": 0, "year": 2008}
                            ],
                            "capitalStock": {"value": 10000},
                            "employees": [
                                {"date": "2018-03-01", "latest": True, "value": 9, "year": 2018},
                                {"date": "2017-12-01", "latest": False, "value": 7, "year": 2017},
                                {"date": "2017-09-01", "latest": False, "value": 7, "year": 2017},
                                {"date": "2017-06-01", "latest": False, "value": 7, "year": 2017},
                                {"date": "2017-03-01", "latest": False, "value": 7, "year": 2017},
                                {"date": "2016-12-01", "latest": False, "value": 7, "year": 2016},
                                {"date": "2016-09-01", "latest": False, "value": 6, "year": 2016},
                                {"date": "2016-06-01", "latest": False, "value": 6, "year": 2016},
                                {"date": "2016-03-01", "latest": False, "value": 7, "year": 2016},
                                {"date": "2015-12-01", "latest": False, "value": 5, "year": 2015},
                                {"date": "2015-09-01", "latest": False, "value": 4, "year": 2015},
                                {"date": "2015-06-01", "latest": False, "value": 4, "year": 2015}
                            ],
                            "public": False
                        },
                        "fullAddress": "Via Merulana, 19, 00185, Roma (RM)",
                        "id": "38e098baa0f9",
                        "name": "DEPP SRL"
                    }
                ]
            }
        }
    }
