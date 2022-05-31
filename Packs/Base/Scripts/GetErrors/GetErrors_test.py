from GetErrors import get_errors


ERROR_ENTRY_1 = [{'Contents': 'This is the error message 1', 'Type': 4}]
ERROR_ENTRY_2 = [{'Contents': 'This is the error message 2', 'Type': 4}]
STD_ENTRY = [{'Contents': 'This is the standard message', 'Type': 0}]
ERROR_ENTRIES = [
    ERROR_ENTRY_1,
    ERROR_ENTRY_2,
    STD_ENTRY
]

WITHOUT_ERROR_ENTRIES = [
    STD_ENTRY,
    STD_ENTRY,
    STD_ENTRY
]


def test_get_errors_with_error_entries():
    """
    Given:
        - Entries data

    When:
        - One or more of the entries' types are error type

    Then:
        - Verify the error entries' contents are returned
    """
    error_messages = get_errors(ERROR_ENTRIES)
    assert len(error_messages) == 2
    assert error_messages[0] == 'This is the error message 1'
    assert error_messages[1] == 'This is the error message 2'


def test_get_errors_without_error_entries():
    """
    Given:
        - Entries data

    When:
        - None of the entries' types are error type

    Then:
        - Verify that no error messages are returned
    """
    error_messages = get_errors(WITHOUT_ERROR_ENTRIES)
    assert len(error_messages) == 0
