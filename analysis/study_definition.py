
# STUDY DEFINITION FOR BASELINE CHARACTERISTICS 

# Import necessary functions

from cohortextractor import (
    StudyDefinition,
    patients,
    codelist_from_csv,
    codelist,
    filter_codes_by_category,
    combine_codelists,
    Measure
)

# Import codelists

from codelists import *


study = StudyDefinition(
    default_expectations={
        "date": {"earliest": "1900-01-01", "latest": "today"},
        "rate": "uniform",
        "incidence": 0.5,
    },
    # select the study population
    index_date="2020-01-01",
    
    population=patients.satisfying(
        """
        (age >= 65 AND age < 120) AND 
        is_registered_with_tpp AND 
        (sex = "M" OR sex = "F") AND 
        (care_home_type = "PC" OR care_home_type = "PN" OR care_home_type = "PS" OR care_home_type = "U") 
        """,
        is_registered_with_tpp=patients.registered_as_of(
          "index_date"
        ),
    ),
    

    
    # HOUSEHOLD INFORMATION
    ## care home status 
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
            "U": "DEFAULT",
        },
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"PC": 0.05, "PN": 0.05, "PS": 0.05, "PR": 0.84, "U": 0.01},},
        },
    ),
    
        ### testing positive (SGSS or primary care)
    first_pos_test_sgss=patients.with_test_result_in_sgss(
       pathogen="SARS-CoV-2",
       test_result="positive",
       on_or_before="index_date",
       returning="binary_flag",
       return_expectations = {"incidence": 0.02}
    ),
        
        ### Admission to hospital for covid
    covid_admission_date=patients.admitted_to_hospital(
        returning= "binary_flag" ,  # defaults to "binary_flag"
        with_these_diagnoses=covid_codelist,  # optional
        on_or_before="index_date",
        find_first_match_in_period=True,
        return_expectations = {"incidence": 0.02}
   ),

    
    antidepressent_ssri = patients.with_these_medications(
      antidepressent_ssri_codes,
      returning = "binary_flag",
      find_first_match_in_period = True,
      between = ["index_date", "index_date - 3 months"],
      return_expectations = {"incidence": 0.2}
    ),    
    
    
    
        # DEMOGRAPHICS  
    ## age 
    age=patients.age_as_of(
        "index_date",
        return_expectations={
            "rate": "universal",
            "int": {"distribution": "population_ages"},
        },
    ),
        ## age groups 
    ageband_narrow = patients.categorised_as(
        {   
            "0": "DEFAULT",
            "65-74": """ age >=  65 AND age < 75""",
            "75-79": """ age >=  75 AND age < 80""",
            "80-84": """ age >=  80 AND age < 85""",
            "85-89": """ age >=  85 AND age < 90""",
            "90+": """ age >=  90 AND age < 120""",
        },
        return_expectations={
            "rate":"universal",
            "category": {"ratios": {"65-74": 0.4, "75-79": 0.2, "80-84":0.2, "85-89":0.1, "90+":0.1 }}
        },
    ),
        ## sex 
    sex=patients.sex(
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"M": 0.49, "F": 0.51}},
        }
    ),
        ## self-reported ethnicity 

        ## index of multiple deprivation, estimate of SES based on patient post code 
	imd=patients.categorised_as(
        {
            "0": "DEFAULT",
            "1": """index_of_multiple_deprivation >=1 AND index_of_multiple_deprivation < 32844*1/5""",
            "2": """index_of_multiple_deprivation >= 32844*1/5 AND index_of_multiple_deprivation < 32844*2/5""",
            "3": """index_of_multiple_deprivation >= 32844*2/5 AND index_of_multiple_deprivation < 32844*3/5""",
            "4": """index_of_multiple_deprivation >= 32844*3/5 AND index_of_multiple_deprivation < 32844*4/5""",
            "5": """index_of_multiple_deprivation >= 32844*4/5 AND index_of_multiple_deprivation < 32844""",
        },
        index_of_multiple_deprivation=patients.address_as_of(
            "index_date",
            returning="index_of_multiple_deprivation",
            round_to_nearest=100,
        ),
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "0": 0.05,
                    "1": 0.19,
                    "2": 0.19,
                    "3": 0.19,
                    "4": 0.19,
                    "5": 0.19,
                }
            },
        },
    ),
        # GEOGRAPHICAL VARIABLES 
    ## grouped region of the practice
    region=patients.registered_practice_as_of(
        "index_date",
        returning="nuts1_region_name",
        return_expectations={
            "rate": "universal",
            "category": {
                "ratios": {
                    "North East": 0.1,
                    "North West": 0.1,
                    "Yorkshire and the Humber": 0.1,
                    "East Midlands": 0.1,
                    "West Midlands": 0.1,
                    "East of England": 0.1,
                    "London": 0.2,
                    "South East": 0.2,
                },
            },
        },
    ),
    
        ## middle layer super output area (msoa) - nhs administrative region 
    msoa=patients.registered_practice_as_of(
        "index_date",
        returning="msoa_code",
        return_expectations={
            "rate": "universal",
            "category": {"ratios": {"E02000001": 0.5, "E02000002": 0.5}},
        },
    ),
    
        ## structured medicine review
    smr=patients.with_these_clinical_events(
        structured_medicine_review,
        on_or_before="index_date",
        return_first_date_in_period=True,
        include_month=True,
    ),
    )
    
    
measures = [


    # antidepressent
    Measure(
        id="prescribing_rate_all",
        numerator="antidepressent_ssri",
        denominator="population",
        group_by = ["care_home_type"],
    ),
    # antidepressent age
    Measure(
        id="prescribing_rate_age",
        numerator="antidepressent_ssri",
        denominator="population",
        group_by = ["ageband_narrow","care_home_type"],
    ),
    # antidepressent region
    Measure(
        id="prescribing_rate_region",
        numerator="antidepressent_ssri",
        denominator="population",
        group_by = ["region","care_home_type"],
    )
    
    ]