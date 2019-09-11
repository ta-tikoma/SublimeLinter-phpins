from SublimeLinter.lint import Linter, WARNING


class Phpins(Linter):
    cmd = ('phpins', '-f', '${file_on_disk}')
    regex = (
        r'((?P<error>ERROR)|(?P<warning>WARNING)):(?P<filename>.+):(?P<line>\d+):(?P<col>\d+)'
        r'.*:(?P<message>.+)$'
    )
    on_stderr = None  # handle stderr via regex
    # default_type = WARNING
    tempfile_suffix = 'php'
    defaults = {
        'selector': 'source.php, text.html.basic',
    }