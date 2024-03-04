import unittest
from tournament_payout_generator import TournamentPayoutGenerator


class UnitTests(unittest.TestCase):

    @staticmethod
    def test_generate_payout_structure():
        player_counts = range(32, 129)
        entry_fees = [10, 15, 20]

        for p in player_counts:
            for e in entry_fees:
                TournamentPayoutGenerator(player_count=p, entry_fee=e).generate_tournament_payout_structure()
