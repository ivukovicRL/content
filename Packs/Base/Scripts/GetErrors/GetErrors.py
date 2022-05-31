import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401


def get_errors(entries):
    """
        entries should be a list of demisto entries

        :type entries: ``list``
        :param entries: multiples entries of results of demisto.executeCommand()

        :return: Error message extracted from the demisto.executeCommand() result
        :rtype: ``string``
    """
    error_messages = []
    for entry in entries:
        assert len(entry) == 1
        entry_details = entry[0]
        is_error_entry = type(entry_details) == dict and entry_details['Type'] == entryTypes['error']
        if is_error_entry:
            error_messages.append(entry_details['Contents'])

    return error_messages


def main():
    try:
        args = demisto.args()
        entry_ids = args.get('entry_id')
        entries = [demisto.executeCommand('getEntry', {'id': entry_id}) for entry_id in entry_ids]
        error_messages = get_errors(entries)
        return_results(CommandResults(
            readable_output='\n'.join(error_messages),
            outputs_prefix='ErrorEntries',
            outputs=error_messages,
            raw_response=error_messages,
        ))
    except Exception as e:
        demisto.error(traceback.format_exc())
        return_error(f'Failed to fetch errors for the given entry id(s). Problem: {str(e)}')


if __name__ in ('__main__', '__builtin__', 'builtins'):
    main()
