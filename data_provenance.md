# Dataset provenance

- Dataset: Titanic passenger data, Seaborn example-data version.
- Distributor: Michael Waskom / Seaborn data repository.
- Source: https://github.com/mwaskom/seaborn-data
- Frozen CSV:
  https://raw.githubusercontent.com/mwaskom/seaborn-data/a29a0141d20e156043ec257a64c8de3b3a03fd6e/titanic.csv
- Source file commit: `a29a0141d20e156043ec257a64c8de3b3a03fd6e`.
- SHA-256:
  `81787d320d7f7b03df935e91de8bd19e11d45c5bbcab86ef4d4a76dc91b7d4f2`.
- Recorded shape: 891 observations and 15 columns.
- Purpose: educational descriptive analysis, not a complete census of everyone
  aboard the Titanic.

The CSV is kept unchanged. It does not include passenger names or contact
information. Its repeated attribute combinations do not establish that records
are erroneous duplicates: this version has no passenger identifier.
Consult the upstream repository for dataset provenance and applicable reuse terms.

The analysis uses eight original fields: survived, pclass, sex, age, sibsp, parch,
fare, and embarked. Class and alive duplicate information already represented in
pclass and survived; several other fields are derived or not needed for the
chosen research question. Sparse deck information is audited but not imputed or
used. These choices are explained in the report.
