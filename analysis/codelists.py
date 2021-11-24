from cohortextractor import (codelist, codelist_from_csv, combine_codelists)
ethnicity_codes = codelist_from_csv(
    "codelists/opensafely-ethnicity.csv",
    system="ctv3",
    column="Code",
    category_column="Grouping_6",
)

covid_codelist = codelist_from_csv(
    "codelists/opensafely-covid-identification.csv",
    system="icd10",
    column="icd10_code"
)

antidepressent_ssri_codes = codelist_from_csv(
  "codelists/opensafely-selective-serotonin-reuptake-inhibitors-dmd.csv",
  system = "snomed",
  column = "dmd_id",
)

antipsychotics_sec_gen = codelist_from_csv(
    "codelists/opensafely-second-generation-antipsychotics-excluding-long-acting-injections.csv",
    system="snomed",
    column="dmd_id",
    )

structured_medicine_review = codelist_from_csv(
  "codelists/opensafely-structured-medication-review-nhs-england.csv",
  system = "snomed",
  column = "code",
)

nhse_care_home_des_codes = codelist_from_csv(
    "codelists/opensafely-nhs-england-care-homes-residential-status-ctv3.csv", 
    system="ctv3", 
    column="code",
)

primis_codes = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-longres.csv", 
    system="snomed", 
    column="code",
)