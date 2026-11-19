# Titanic Data Workflow

AI Foundations (Edward Hickman)

DRAFT FOR STUDENT REVIEW — The required course APA template has not been provided. This preview is not module_summary.pdf and is not submission-ready.

## Overview

This project builds a reproducible descriptive data workflow for the Titanic passenger dataset distributed through Seaborn's example-data repository (Waskom, n.d.). It uses Python, NumPy, Pandas, Matplotlib, and Seaborn to audit data quality, apply reusable cleaning functions, and investigate recorded survival patterns. The dataset source is https://github.com/mwaskom/seaborn-data/blob/a29a0141d20e156043ec257a64c8de3b3a03fd6e/titanic.csv.

## Dataset Description

The frozen CSV contains 891 observations and 15 columns. Each row describes a passenger record in this educational subset, not a complete census of everyone aboard the Titanic. The analysis focuses on survived, pclass, sex, age, sibsp, parch, fare, and embarked. Survival is coded as zero or one, passenger class as one through three, age in years, and sex using the source's recorded female/male labels. The full input includes 177 missing ages, two missing embarkation labels, and 688 missing deck entries; the focused output contains eight original fields plus an age-missingness indicator.

## Workflow Description

Ingestion loads the local CSV with Pandas, displays the first rows, and checks its shape and SHA-256 fingerprint. The audit records column types, missingness, numerical ranges, and repeated attribute combinations. Three reusable functions normalize column names, clean categorical text and missing embarkation labels, and select and validate the focused analysis data. An EDA function returns numerical summaries, class and sex-by-class survival proportions, and an age-missingness comparison. The notebook then creates three labeled figures, exports its evidence tables, and ends with an interpretation of observed findings and limitations.

## Key Decisions and Assumptions

The notebook integrates the input data, executable transformations, numerical evidence, figures, and explanatory text so readers can follow the analysis rather than receiving disconnected final images. This choice applies Danchev's (2022) discussion of transparent, reproducible computational narratives. Dependency recording and version control follow Rule et al.'s (2019) recommendations for maintainable and rerunnable notebook analyses.

Column-name normalization changes zero names in this already normalized snapshot, and that zero is recorded rather than portrayed as a discovered data defect. Categorical cleaning makes whitespace and case handling consistent and labels the two missing embarkation values as unknown. This label is bookkeeping, not a claim to recover their true ports; embarkation is not used in the plotted survival comparisons. Numeric validation raises an error for unexpected invalid values instead of silently dropping or coercing records without notice.

All 177 missing ages remain missing. The histogram explicitly reports its 714 observed ages, while survival summaries retain all 891 records. This choice avoids inventing ages for an exploratory distribution and keeps the different analysis denominators explicit. Complete-case exclusion can introduce bias depending on the missing-data mechanism, and neither simple replacement nor complete-case analysis is universally valid (Sterne et al., 2009).

The 107 full-row attribute combinations that repeat earlier records are retained because this version has no passenger identifier. Identical attribute profiles alone do not prove that two records describe the same passenger. The focused analysis omits unused, redundant, or derived fields, including class and alive, which overlap with pclass and survived; missing deck values are not filled. No outliers are removed merely for being unusual.

Figure 1 shows the distribution of observed ages. Figure 2 compares class-specific survival proportions rather than survivor counts alone, because class sizes differ. Figure 3 compares the recorded female and male groups within each class to show variation hidden by class totals. Rate charts start at zero, use a shared percentage scale, and display sample sizes so readers can inspect the denominators.

## Results and Interpretation

The raw and focused datasets both contain 891 rows; zero rows were dropped. Overall, 342 of 891 records have survived=1 (38.38%). Figure 1 displays 714 observed ages, with a median of 28 years; the 177 missing ages represent 19.87% of records.

Figure 2 shows survival proportions of 62.96% in first class (136/216), 47.28% in second class (87/184), and 24.24% in third class (119/491). This dataset therefore shows a strong descriptive association between recorded class and survival, but the comparison alone cannot identify its causes.

Figure 3 shows higher observed female than male survival within every class: 96.81% versus 36.89% in first class, 92.11% versus 15.74% in second class, and 50.00% versus 13.54% in third class. These are recorded-group comparisons, not estimates of the independent causal effects of sex or class.

The missingness audit is consequential: observed survival is 40.62% among records with known ages (290/714) but 29.38% among records with missing ages (52/177). This difference warns against treating age-complete records as interchangeable with the full dataset; it does not establish why age values are missing.

## Responsible Practice: Bias and Data Quality

The analysis preserves all rows for survival comparisons and makes the narrower age-histogram denominator visible. Retaining an unknown embarkation label and an age-missingness flag does not correct selection bias; it makes the handling auditable. The missing-data mechanism cannot be inferred from these simple comparisons, and a future inferential analysis should evaluate its assumptions and consider sensitivity analyses rather than automatically choosing imputation (Sterne et al., 2009).

Historical recording practices and selection into this 891-row file limit generalization. The recorded binary sex field is not a measure of gender identity, and passenger class is not a complete description of socioeconomic circumstances. The notebook makes descriptive comparisons only and does not rank the value of human lives, infer individual behavior, or claim causal mechanisms. A next step would be to compare the subset with a documented manifest and investigate missingness and record identity using reliable source metadata.

AI assistance was used to help prepare code, checks, and this draft narrative. The learner must review, understand, and revise the submission, and should retain this acknowledgement or adapt it accurately to the assistance actually used. The report is tied to the executed notebook's saved outputs, not hypothetical analysis results.

## Reproducibility

The repository includes the immutable local CSV and its fingerprint, the executable data_workflow.ipynb notebook, exported figures and tables, automated checks, and requirements.txt generated by pip freeze from the actual Python 3.11 environment. The short README explains dependency installation and restarting the kernel before running every cell in order. Saved package versions and source integrity support the transparent workflow advocated by Danchev (2022); they do not guarantee identical behavior on every future operating system.

Git work uses the main branch and development/titanic-workflow branch, with separate genuine commits for data provenance and notebook setup, analysis code, and executed evidence and reporting. This supports inspection of changes rather than a fabricated history and implements the dependency-recording and version-control practices discussed by Rule et al. (2019). The development branch is proposed for review; the final report must still be placed in the course APA template.

## Future Integration Reflections

For machine-learning use, the workflow would define survival as the target, reserve a held-out test set before fitting transformations, and fit missing-value handling and encoders using training data only. It would also exclude outcome equivalents such as alive and review every field for information unavailable at the intended prediction time. Before neural-network training, numerical inputs would be scaled using training-only parameters, categorical values encoded, and class balance, small-sample overfitting, and subgroup errors checked against a simpler baseline. Agentic automation could rerun input-integrity checks, missingness audits, tests, notebook execution, and draft figure descriptions. Autonomous removal of repeated records, invention of missing ages, causal interpretations, or publication of unreviewed reports would be risky and should require human approval.

## Conclusion

The workflow shows substantial recorded survival differences across passenger classes and sex groups, while preserving the distinction between description and causation. Its most important data-quality lessons are that missing ages change the population represented by an age plot and that repeated attribute profiles are not sufficient evidence for deleting passenger records. Reusable functions, explicit denominators, preserved raw data, and a rerunnable notebook make the project a useful foundation for later AI work, subject to the stated historical and data-quality limitations.

## References

Danchev, V. (2022). Reproducible data science with Python: An open learning resource. Journal of Open Source Education, 5(56), 156. https://doi.org/10.21105/jose.00156

Rule, A., Birmingham, A., Zuniga, C., Altintas, I., Huang, S.-C., Knight, R., Moshiri, N., Nguyen, M. H., Rosenthal, S. B., Pérez, F., & Rose, P. W. (2019). Ten simple rules for writing and sharing computational analyses in Jupyter Notebooks. PLOS Computational Biology, 15(7), e1007007. https://doi.org/10.1371/journal.pcbi.1007007

Sterne, J. A. C., White, I. R., Carlin, J. B., Spratt, M., Royston, P., Kenward, M. G., Wood, A. M., & Carpenter, J. R. (2009). Multiple imputation for missing data in epidemiological and clinical research: Potential and pitfalls. BMJ, 338, b2393. https://doi.org/10.1136/bmj.b2393

Waskom, M. (n.d.). Titanic [Data set]. In seaborn-data. GitHub. https://github.com/mwaskom/seaborn-data/blob/a29a0141d20e156043ec257a64c8de3b3a03fd6e/titanic.csv
