import unittest
from main import TournamentPayoutGenerator


class UnitTests(unittest.TestCase):

    @staticmethod
    def test_generate_payout_structure():
        for entry_fee in [10, 15, 20]:
            for player_count in range(16, 129):
                TournamentPayoutGenerator(player_count, entry_fee).print_payouts()