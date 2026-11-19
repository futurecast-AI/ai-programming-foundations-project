# AI Programming Foundations

**AI Foundations (Edward Hickman)**

This project builds a reproducible, descriptive workflow for the Titanic passenger
dataset using Python, NumPy, Pandas, Matplotlib, and Seaborn. It audits data quality,
applies reusable cleaning functions, and explores recorded survival patterns with
three labeled figures. No machine-learning model is trained.

## Dataset

The local `titanic.csv` contains 891 rows and 15 columns from
[Seaborn's Titanic dataset](https://github.com/mwaskom/seaborn-data/blob/a29a0141d20e156043ec257a64c8de3b3a03fd6e/titanic.csv).

## Run

Use Python 3.11:

```bash
python -m venv .venv
source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook data_workflow.ipynb
```

In Jupyter, select **Restart Kernel and Run All Cells**. Keep `titanic.csv`
beside the notebook. For a command-line execution:

```bash
jupyter nbconvert --execute --to notebook --inplace data_workflow.ipynb
```

The dependency file is generated from the project environment using:

```bash
pip freeze > requirements.txt
```

Run the checks with `python -m pytest tests -q`. Figures and machine-readable
results are written to `outputs/`.

## Submission status

The report's final `module_summary.pdf` must use the course-provided APA template.
That template has not yet been supplied; draft report material is not a final
submission. The development branch preserves the work for review.
