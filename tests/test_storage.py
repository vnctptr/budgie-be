from budgie.data import Storage

import pytest
import tempfile

# ==============================================================================
# Fixtures
# ==============================================================================

@pytest.fixture
def make_git_repo():
  with tempfile.TemporaryDirectory(prefix="budgie_tests") as d:
    #TODO: create git repository
    yield d

# ==============================================================================
# Tests
# ==============================================================================
