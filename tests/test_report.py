"""Check the template-based report and its submission filenames."""
from pathlib import Path
import json

from docx import Document
import pymupdf

ROOT = Path(__file__).resolve().parents[1]


def test_template_formatting_audit_and_document_geometry():
    """Check the recorded template comparison and retained page and type styles."""
    audit = json.loads((ROOT / "outputs" / "report_template_audit.json").read_text())
    assert all(audit[k] for k in [
        "styles_preserved", "section_geometry_preserved",
        "header_preserved", "footer_preserved",
    ])
    document = Document(ROOT / "module_summary.docx")
    section = document.sections[0]
    assert [getattr(section, f"{side}_margin").inches
            for side in ["top", "bottom", "left", "right"]] == [1, 1, 1, 1]
    assert document.styles["Heading 1"].font.name == "Arial"
    assert document.styles["Heading 1"].font.size.pt == 11
    assert document.styles["Heading 1"].paragraph_format.line_spacing == 2


def test_report_contains_required_sections_and_actual_results():
    """Require all rubric sections, measured figures, and no sample cover fields."""
    document = Document(ROOT / "module_summary.docx")
    text = "\n".join(p.text for p in document.paragraphs)
    for heading in [
        "Overview", "Dataset Description", "Workflow Description",
        "Key Decisions and Assumptions", "Results and Interpretation",
        "Responsible Practice: Bias and Data Quality", "Reproducibility",
        "Future Integration Reflections", "Conclusion", "References",
    ]:
        assert heading in text
    for measured in ["891", "177", "714", "62.96%", "47.28%", "24.24%"]:
        assert measured in text
    for placeholder in [
        "Title of Student Paper", "Student Name", "Clackamas Community College",
        "Instructor Name", "Assignment due date written",
    ]:
        assert placeholder not in text
    assert len(document.inline_shapes) == 3


def test_pdf_has_page_numbers_figures_and_final_references():
    """Verify PDF export has real content, all figure images, and references last."""
    with pymupdf.open(ROOT / "module_summary.pdf") as document:
        assert len(document) >= 5
        assert all(page.get_text().strip().splitlines()[0].strip() == str(i)
                   for i, page in enumerate(document, 1))
        assert sum(len(page.get_images()) for page in document) >= 3
        last = document[-1].get_text()
        assert "References" in last
        for doi in ["10.21105/jose.00156", "10.1371/journal.pcbi.1007007",
                    "10.1136/bmj.b2393"]:
            assert doi in last


def test_final_filenames_replace_superseded_drafts():
    """Prevent accidentally submitting the old draft report instead of the final file."""
    assert (ROOT / "module_summary.pdf").is_file()
    assert (ROOT / "module_summary.docx").is_file()
    assert not (ROOT / "module_summary_draft.pdf").exists()
    assert not (ROOT / "report_draft.md").exists()
