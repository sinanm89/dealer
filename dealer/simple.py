from .base import SCMBackend


class Backend(SCMBackend):

    default_rev_filename = '.revision'

    def init_repo(self):
        from os import path as op

        try:
            assert op.exists(self.path)

            self._repo = self
            rev_file = self.path if op.isfile(self.path) else op.join(self.path, self.default_rev_filename)
            with open(rev_file) as f:
                self._revision = f.read().strip()
        except (AssertionError, IOError):
            raise TypeError('Invalid path.')

        return self._repo


simple = Backend()


# pymode:lint_ignore=W0201
