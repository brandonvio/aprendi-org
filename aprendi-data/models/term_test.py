# test_term.py
from models.term import TermModel, TermRepo


def test_term_crud_operations():
    """
    This test will test the following:
    1. Save a term
    2. Retrieve a term
    3. Get all terms for an organization
    """
    # 1. Save a term
    term = TermModel(org_id="test_org_1", term_id="term_001", term_name="Fall 2023")
    saved_term = TermRepo.save(term)

    assert saved_term.term_id == "term_001"

    # 2. Retrieve a term
    fetched_term = TermRepo.get(org_id="test_org_1", id=saved_term.term_id)
    assert fetched_term.term_name == "Fall 2023"
    assert fetched_term.term_id == "term_001"

    # 3. Get all terms for an organization
    terms = TermRepo.get_all(org_id="test_org_1")
    assert len(terms) == 1
    assert terms[0].term_name == "Fall 2023"
    assert terms[0].term_id == "term_001"
