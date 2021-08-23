from cohortextractor import StudyDefinition, patients, codelist, codelist_from_csv  # NOQA


study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },

 population = patients.satisfying(
     """
        care_home_type = "PS" OR care_home_type = "PN" OR care_home_type = "PC"
        """,

care_home_type=patients.care_home_status_as_of(
    "2020-02-01",
    categorised_as={
        "PC":
        """
          IsPotentialCareHome
          AND LocationDoesNotRequireNursing='Y'
          AND LocationRequiresNursing='N'
        """,
        "PN":
        """
          IsPotentialCareHome
          AND LocationDoesNotRequireNursing='N'
          AND LocationRequiresNursing='Y'
        """,
        "PS": "IsPotentialCareHome",
        "PR": "NOT IsPotentialCareHome",
        "": "DEFAULT",
    },
    return_expectations={
        "rate": "universal",
        "category": {"ratios": {"PC": 0.05, "PN": 0.05, "PS": 0.05, "PR": 0.84, "": 0.01},},
    },
),


)
