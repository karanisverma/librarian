import mock

from librarian.lib import squery as mod

MOD = mod.__name__


def test_normalize_url():
    """ URLs with backslashes should be converted to forward slashes """
    p = r'C:\Temp\foo.sqlite'
    assert mod.normurl(p) == 'C:/Temp/foo.sqlite'


def test_normalize_url_with_forw_slashes():
    """ Forward slashes should be intact """
    p = '/foo/bar/baz.sqlite'
    assert mod.normurl(p) == '/foo/bar/baz.sqlite'


def test_row_factory():
    """ Factory should create a dict out of a row """
    # XXX: This must be tested in integration test, because it is a subclass
    # of ``sqlite3.Row``, which is written in C and not very friendly to mock
    # objects.
    pass


@mock.patch(MOD + '.sqlite3')
def test_db_connect(sqlite3):
    mod.Database.connect('foo.db')
    sqlite3.connect.assert_called_once_with(
        'foo.db', detect_types=sqlite3.PARSE_DECLTYPES)


@mock.patch(MOD + '.sqlite3')
def test_db_uses_dbdict(sqlite3):
    """ The database will use a dbdict_factory for all rows """
    conn = mod.Database.connect('foo.db')
    assert conn.row_factory == mod.Row


@mock.patch(MOD + '.sqlite3')
def test_db_isolation(sqlite3):
    """ Isolation level should be None to allow translaction control """
    conn = mod.Database.connect('foo.db')
    assert conn.isolation_level is None


@mock.patch(MOD + '.sqlite3')
def test_db_wal(sqlite3):
    """ journal_mode=WAL pragma is executed upon connection """
    cursor = sqlite3.connect().cursor()
    mod.Database.connect('foo.db')
    cursor.execute.assert_called_once_with('PRAGMA journal_mode=WAL')


@mock.patch(MOD + '.sqlite3')
def test_init_db_with_connection(*ignored):
    """ Database object is initialized with a connection """
    conn = mock.Mock()
    db = mod.Database(conn)
    assert db.conn == conn


@mock.patch(MOD + '.sqlite3')
def test_get_cursor(*ignored):
    """ Obtaining curor should return connection's cursor object """
    db = mod.Database(mock.Mock())
    cur = db.cursor
    assert cur == db.conn.cursor.return_value


@mock.patch(MOD + '.sqlite3')
def test_get_curor_only_retrieved_once(sqlite3):
    """ Cursor is only retrieved once """
    db = mod.Database(mock.Mock())
    db.cursor
    db.cursor
    assert db.conn.cursor.call_count == 1


@mock.patch(MOD + '.sqlite3')
def test_convert_sqlbuilder_class_to_repr(*ignored):
    """ When sqlbuilder object is passed as query, it's converted to repr """
    from sqlobject import sqlbuilder
    db = mod.Database(mock.Mock())
    select = mock.Mock(spec=sqlbuilder.Select)
    sql = db._convert_query(select)
    assert sql == select.__sqlrepr__.return_value


@mock.patch(MOD + '.sqlite3')
def test_convert_string_query(*ignored):
    """ When raw SQL sting is passed, it's not conveted """
    s = 'foobar'
    db = mod.Database(mock.Mock())
    sql = db._convert_query(s)
    assert s is sql


@mock.patch(MOD + '.sqlite3')
def test_query(sqlite3):
    """ query() should execute a database query """
    db = mod.Database(mock.Mock())
    db.query('SELECT * FROM foo;')
    db.cursor.execute.assert_called_once_with('SELECT * FROM foo;', {})


@mock.patch(MOD + '.sqlite3')
@mock.patch.object(mod.Database, '_convert_query')
def test_query_converts(*ignored):
    """ Querying will convert the query """
    db = mod.Database(mock.Mock())
    qry = mock.Mock()
    db.query(qry)
    db._convert_query.assert_called_once_with(qry)
    db.cursor.execute.assert_called_once_with(db._convert_query(), {})


@mock.patch(MOD + '.sqlite3')
def test_query_params(sqlite3):
    """ Query converts positional arguments to params list """
    db = mod.Database(mock.Mock())
    db.query('SELECT * FROM foo WHERE bar = ?;', 12)
    db.cursor.execute.assert_called_once_with(
        'SELECT * FROM foo WHERE bar = ?;', (12,))


@mock.patch(MOD + '.sqlite3')
def test_query_keyword_params(sqlite3):
    """ Query converts keyword params into dict """
    db = mod.Database(mock.Mock())
    db.query('SELECT * FROM foo WHERE bar = :bar;', bar=12)
    db.cursor.execute.assert_called_once_with(
        'SELECT * FROM foo WHERE bar = :bar;', {'bar': 12})


@mock.patch(MOD + '.sqlite3')
def test_execute_alias(sqlite3):
    """ Instace has execute() alias for cursor.execute() """
    db = mod.Database(mock.Mock())
    db.execute('SELECT * FROM foo WHERE bar = ?;', (12,))
    db.cursor.execute.assert_called_once_with(
        'SELECT * FROM foo WHERE bar = ?;', (12,))


@mock.patch(MOD + '.sqlite3')
def test_executemany_alias(sqlite3):
    """ Instance has executemany() alias for cursor.executemany() """
    db = mod.Database(mock.Mock())
    db.executemany('INSERT INTO foo VALUES (?, ?);', [(1, 2), (3, 4)])
    db.cursor.executemany.assert_called_once_with(
        'INSERT INTO foo VALUES (?, ?);', [(1, 2), (3, 4)])


@mock.patch(MOD + '.sqlite3')
def test_executescript_alias(sqlite3):
    """ Instace has executescript() alias for cursor.executescript() """
    db = mod.Database(mock.Mock())
    db.executescript('SELECT * FROM foo;')
    db.cursor.executescript.assert_called_once_with('SELECT * FROM foo;')


@mock.patch(MOD + '.sqlite3')
def test_commit_alias(sqlite3):
    """ Instance has commit() alias for connection.commit() """
    db = mod.Database(mock.Mock())
    db.commit()
    assert db.conn.commit.called


@mock.patch(MOD + '.sqlite3')
def test_rollback_alias(sqlite3):
    """ Instance has rollback() alias for connection.rollback() """
    db = mod.Database(mock.Mock())
    db.rollback()
    assert db.conn.rollback.called


@mock.patch(MOD + '.sqlite3')
def test_refresh_table_stats(*ignored):
    """ Instance can call ANALYZE """
    db = mod.Database(mock.Mock())
    db.refresh_table_stats()
    db.cursor.execute.assert_called_once_with('ANALYZE sqlite_master;')


@mock.patch(MOD + '.sqlite3')
def test_acquire_lock(*ignored):
    """ Instance has a method for acquiring exclusive lock """
    db = mod.Database(mock.Mock())
    db.acquire_lock()
    assert db.conn.interrupt.called
    db.cursor.execute.assert_called_once_with('BEGIN EXCLUSIVE')


@mock.patch(MOD + '.sqlite3')
def test_results(*ignored):
    """ Results property gives access to cursor.fetchall() results """
    db = mod.Database(mock.Mock())
    res = db.results
    assert db.cursor.fetchall.called
    assert res == db.cursor.fetchall.return_value


@mock.patch(MOD + '.sqlite3')
def test_result(*ignored):
    """ Result property gives access to cursor.fetchone() resutls """
    db = mod.Database(mock.Mock())
    res = db.result
    assert db.cursor.fetchone.called
    assert res == db.cursor.fetchone.return_value


@mock.patch(MOD + '.sqlite3')
def test_transaction(*ignored):
    """ Instance has a transaction context manager """
    db = mod.Database(mock.Mock())
    with db.transaction() as cur:
        db.cursor.execute.assert_called_once_with('BEGIN')
        assert cur == db.cursor
    assert db.conn.commit.called


@mock.patch(MOD + '.sqlite3')
def transaction_rollback(*ignored):
    """ Transactions rolls back on exception """
    db = mod.Database(mock.Mock())
    try:
        with db.transaction():
            raise RuntimeError()
        assert False, 'Expected to raise'
    except RuntimeError:
        assert db.conn.rollback.called


@mock.patch(MOD + '.sqlite3')
def test_transaction_silent_rollback(*ignored):
    """ Transaction silently rolled back if silent flag is passed """
    db = mod.Database(mock.Mock())
    try:
        with db.transaction(silent=True):
            raise RuntimeError()
        assert db.conn.rollback.called
    except RuntimeError:
        assert False, 'Expected not to raise'
