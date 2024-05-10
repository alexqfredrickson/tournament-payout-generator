import math


class TournamentPayoutGenerator:
    def __init__(self, player_count, entry_fee):
        self.player_count = player_count
        self.entry_fee = entry_fee
        self.total_payout = self.entry_fee * self.player_count
        self.round_payouts_to_nearest_five = True

        self.payout_percentages = self._get_payout_percentages()
        self.payout_values = self._get_payout_values()

    def _get_payout_percentages(self):
        if 1 <= self.player_count <= 15:
            return [1]
        elif 16 <= self.player_count <= 23:
            return [.50, .30, .15, .05]
        elif 24 <= self.player_count <= 31:
            return [.35, .20, .15, .10, .05, .05]
        elif 32 <= self.player_count <= 47:
            return [.35, .20, .15, .10, .05, .05]
        elif 48 <= self.player_count <= 63:
            return [.33, .20, .15, .12, .06, .06, .04, .04]
        elif 64 <= self.player_count <= 128:
            return [.30, .20, .14, .10, .05, .05, .04, .04, .02, .02, .02, .02]

    def _get_payout_values(self):
        payout_values = []

        for p in self.payout_percentages:
            payout_values.append(math.floor(self.total_payout * p))

        if self.round_payouts_to_nearest_five:
            for i in range(len(payout_values)):
                while payout_values[i] % 5 != 0:
                    payout_values[i] += 1

        provisional_sum_of_payout_values = sum(payout_values)
        remainder = self.total_payout - provisional_sum_of_payout_values
        payout_values[0] += remainder

        return payout_values

    def print_payouts(self):

        if self.total_payout != sum(self.payout_values):
            print(f"ERROR: total payout ({self.total_payout}) differs from payout value sums ({sum(self.payout_values)}).")

        with open("./results.csv", 'a+') as results_file:
            for i in range(1, len(self.payout_values) + 1):
                if i == 1:
                    num_suffix = "st"
                elif i == 2:
                    num_suffix = "nd"
                elif i == 3:
                    num_suffix = "rd"
                else:
                    num_suffix = "th"

                results_file.write(
                    f"${self.entry_fee}\t{self.player_count}\t{i}{num_suffix}\t${self.payout_values[i-1]}\n"
                )

