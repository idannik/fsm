import unittest

from fsm import State, FSM

CONNECTION_STATES = [
    State('LISTENING', {'connect': 'CONNECTED',
                        'error': 'LISTENING'
                        }),
    State('CONNECTED', {
        'accept': 'ACCEPTED',
        'close': 'CLOSED'
    }),
    State('ACCEPTED', {'close': 'CLOSED',
                       'read': 'READING',
                       'write': 'WRITING'}),
    State('READING', {'read': 'READING',
                      'close': 'CLOSED',
                      'write': 'WRITING'}),
    State('WRITING', {'read': 'READING',
                      'close': 'CLOSED',
                      'write': 'WRITING'}),
    State('CLOSED', {}, default_event='LISTENING'),
    State('ERROR', {}, default_event='ERROR')
]


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.fsm = FSM(CONNECTION_STATES, start='LISTENING')


    def test_connect_accept_close(self):
        assert self.fsm.get_state_by_events(['connect', 'accept', 'read', 'close']) == 'CLOSED'

    def test_read_before_connect_raise_error(self):
        assert self.fsm.get_state_by_events(['read', 'connect', 'accept', 'read', 'close']) == 'ERROR'

    def test_read_read_read(self):
        assert self.fsm.get_state_by_events(['connect', 'accept', 'read', 'read', 'read']) == 'READING'

    def test_write_write_write(self):
        assert self.fsm.get_state_by_events(['connect', 'accept', 'write', 'write', 'write']) == 'WRITING'

if __name__ == '__main__':
    unittest.main()
