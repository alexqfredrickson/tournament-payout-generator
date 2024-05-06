import math


class TournamentPayoutGenerator:
    def __init__(self, player_count, entry_fee):
        self.player_count = player_count
        self.entry_fee = entry_fee

    def generate_tournament_payout_structure(self):

        first_place_payout, second_place_payout, third_place_payout, fourth_place_payout, \
        fifth_place_payout, sixth_place_payout, seventh_place_payout, eighth_place_payout, \
        ninth_place_payout, tenth_place_payout, eleventh_place_payout, twelth_place_payout = \
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

        first_place_payout_pct, second_place_payout_pct, third_place_payout_pct, fourth_place_payout_pct, \
        fifth_place_payout_pct, sixth_place_payout_pct, seventh_place_payout_pct, eighth_place_payout_pct, \
        ninth_place_payout_pct, tenth_place_payout_pct, eleventh_place_payout_pct, twelth_place_payout_pct = \
            None, None, None, None, None, None, None, None, None, None, None, None

        total_payout = self.entry_fee * self.player_count

        player_count_16_23 = 16 <= self.player_count <= 23
        player_count_24_31 = 24 <= self.player_count <= 31
        player_count_32_47 = 32 <= self.player_count <= 47
        player_count_48_63 = 48 <= self.player_count <= 63
        player_count_64_128 = 64 <= self.player_count <= 128

        # get base payout percents
        if player_count_16_23:
            first_place_payout_pct = .50
            second_place_payout_pct = .30
            third_place_payout_pct = .15
            fourth_place_payout_pct = .05
            fifth_place_payout_pct = None
            sixth_place_payout_pct = None
            seventh_place_payout_pct = None
            eighth_place_payout_pct = None
            ninth_place_payout_pct = None
            tenth_place_payout_pct = None
            eleventh_place_payout_pct = None
            twelth_place_payout_pct = None

        elif player_count_24_31:
            first_place_payout_pct = .35
            second_place_payout_pct = .20
            third_place_payout_pct = .15
            fourth_place_payout_pct = .10
            fifth_place_payout_pct = .05
            sixth_place_payout_pct = .05
            seventh_place_payout_pct = None
            eighth_place_payout_pct = None
            ninth_place_payout_pct = None
            tenth_place_payout_pct = None
            eleventh_place_payout_pct = None
            twelth_place_payout_pct = None

        elif player_count_32_47:
            first_place_payout_pct = .35
            second_place_payout_pct = .20
            third_place_payout_pct = .15
            fourth_place_payout_pct = .10
            fifth_place_payout_pct = .05
            sixth_place_payout_pct = .05
            seventh_place_payout_pct = None
            eighth_place_payout_pct = None
            ninth_place_payout_pct = None
            tenth_place_payout_pct = None
            eleventh_place_payout_pct = None
            twelth_place_payout_pct = None

        elif player_count_48_63:
            first_place_payout_pct = .33
            second_place_payout_pct = .20
            third_place_payout_pct = .15
            fourth_place_payout_pct = .12
            fifth_place_payout_pct = .06
            sixth_place_payout_pct = .06
            seventh_place_payout_pct = .04
            eighth_place_payout_pct = .04
            ninth_place_payout_pct = None
            tenth_place_payout_pct = None
            eleventh_place_payout_pct = None
            twelth_place_payout_pct = None

        elif player_count_64_128:
            first_place_payout_pct = .30
            second_place_payout_pct = .20
            third_place_payout_pct = .14
            fourth_place_payout_pct = .10
            fifth_place_payout_pct = .05
            sixth_place_payout_pct = .05
            seventh_place_payout_pct = .04
            eighth_place_payout_pct = .04
            ninth_place_payout_pct = .02
            tenth_place_payout_pct = .02
            eleventh_place_payout_pct = .02
            twelth_place_payout_pct = .02

        # determine rebated players based on player count
        rebated_player_count = 0

        if player_count_16_23:
            rebated_player_count = 0
        elif player_count_24_31:
            rebated_player_count = 0
        elif player_count_32_47:
            rebated_player_count = 2  # 7, 8
        elif player_count_48_63:
            rebated_player_count = 4  # 9, 10, 11, 12
        elif player_count_64_128:
            rebated_player_count = 4  # 13, 14, 15, 16

        # set aside some rebates (temporarily) and determine payouts
        # payouts are predicated on % of total payout sans rebated player entry fees
        total_payout -= self.entry_fee * rebated_player_count

        if player_count_16_23:
            first_place_payout = math.floor(total_payout * first_place_payout_pct)
            second_place_payout = math.floor(total_payout * second_place_payout_pct)
            third_place_payout = math.floor(total_payout * third_place_payout_pct)
            fourth_place_payout = math.floor(total_payout * fourth_place_payout_pct)

        elif player_count_24_31:
            first_place_payout = math.floor(total_payout * first_place_payout_pct)
            second_place_payout = math.floor(total_payout * second_place_payout_pct)
            third_place_payout = math.floor(total_payout * third_place_payout_pct)
            fourth_place_payout = math.floor(total_payout * fourth_place_payout_pct)
            fifth_place_payout = math.floor(total_payout * fifth_place_payout_pct)
            sixth_place_payout = math.floor(total_payout * sixth_place_payout_pct)

        elif player_count_32_47:
            first_place_payout = math.floor(total_payout * first_place_payout_pct)
            second_place_payout = math.floor(total_payout * second_place_payout_pct)
            third_place_payout = math.floor(total_payout * third_place_payout_pct)
            fourth_place_payout = math.floor(total_payout * fourth_place_payout_pct)
            fifth_place_payout = math.floor(total_payout * fifth_place_payout_pct)
            sixth_place_payout = math.floor(total_payout * sixth_place_payout_pct)

        elif player_count_48_63:
            first_place_payout = math.floor(total_payout * first_place_payout_pct)
            second_place_payout = math.floor(total_payout * second_place_payout_pct)
            third_place_payout = math.floor(total_payout * third_place_payout_pct)
            fourth_place_payout = math.floor(total_payout * fourth_place_payout_pct)
            fifth_place_payout = math.floor(total_payout * fifth_place_payout_pct)
            sixth_place_payout = math.floor(total_payout * sixth_place_payout_pct)
            seventh_place_payout = math.floor(total_payout * seventh_place_payout_pct)
            eighth_place_payout = math.floor(total_payout * eighth_place_payout_pct)

        elif player_count_64_128:
            first_place_payout = math.floor(total_payout * first_place_payout_pct)
            second_place_payout = math.floor(total_payout * second_place_payout_pct)
            third_place_payout = math.floor(total_payout * third_place_payout_pct)
            fourth_place_payout = math.floor(total_payout * fourth_place_payout_pct)
            fifth_place_payout = math.floor(total_payout * fifth_place_payout_pct)
            sixth_place_payout = math.floor(total_payout * sixth_place_payout_pct)
            seventh_place_payout = math.floor(total_payout * seventh_place_payout_pct)
            eighth_place_payout = math.floor(total_payout * eighth_place_payout_pct)
            ninth_place_payout = math.floor(total_payout * ninth_place_payout_pct)
            tenth_place_payout = math.floor(total_payout * tenth_place_payout_pct)
            eleventh_place_payout = math.floor(total_payout * eleventh_place_payout_pct)
            twelth_place_payout = math.floor(total_payout * twelth_place_payout_pct)

        # reset total payout
        total_payout = self.entry_fee * self.player_count

        # we floored everything, so add the remainder vs. total payout back to first place to make it more juicy
        first_place_payout += \
            total_payout - (first_place_payout + second_place_payout + third_place_payout + fourth_place_payout +
                            fifth_place_payout + sixth_place_payout + seventh_place_payout + eighth_place_payout +
                            ninth_place_payout + tenth_place_payout + eleventh_place_payout + twelth_place_payout +
                            (rebated_player_count * self.entry_fee))

        # round everything up to $5 increments; take it away from first place :*(
        while second_place_payout % 5 != 0:
            first_place_payout -= 1
            second_place_payout += 1

        while third_place_payout % 5 != 0:
            first_place_payout -= 1
            third_place_payout += 1

        while fourth_place_payout % 5 != 0:
            first_place_payout -= 1
            fourth_place_payout += 1

        while fifth_place_payout % 5 != 0:
            first_place_payout -= 1
            fifth_place_payout += 1

        while sixth_place_payout % 5 != 0:
            first_place_payout -= 1
            sixth_place_payout += 1

        while seventh_place_payout % 5 != 0:
            first_place_payout -= 1
            seventh_place_payout += 1

        while eighth_place_payout % 5 != 0:
            first_place_payout -= 1
            eighth_place_payout += 1

        while ninth_place_payout % 5 != 0:
            first_place_payout -= 1
            ninth_place_payout += 1

        while tenth_place_payout % 5 != 0:
            first_place_payout -= 1
            tenth_place_payout += 1

        while eleventh_place_payout % 5 != 0:
            first_place_payout -= 1
            eleventh_place_payout += 1

        while twelth_place_payout % 5 != 0:
            first_place_payout -= 1
            twelth_place_payout += 1

        with open("./results.csv", 'a+') as results_file:
            results_file.write(f"${self.entry_fee}\t{self.player_count}\t1st\t${first_place_payout}\n")
            results_file.write(f"${self.entry_fee}\t{self.player_count}\t2nd\t${second_place_payout}\n")
            results_file.write(f"${self.entry_fee}\t{self.player_count}\t3rd\t${third_place_payout}\n")
            results_file.write(f"${self.entry_fee}\t{self.player_count}\t4th\t${fourth_place_payout}\n")

            if player_count_24_31:
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t5th\t${fifth_place_payout}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t6th\t${sixth_place_payout}\n")

            elif player_count_32_47:
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t5th\t${fifth_place_payout}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t6th\t${sixth_place_payout}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t7th\t${self.entry_fee}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t8th\t${self.entry_fee}\n")

            elif player_count_48_63:
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t5th\t${fifth_place_payout}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t6th\t${sixth_place_payout}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t7th\t${seventh_place_payout}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t8th\t${eighth_place_payout}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t9th\t${self.entry_fee}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t10th\t${self.entry_fee}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t11th\t${self.entry_fee}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t12th\t${self.entry_fee}\n")

            elif player_count_64_128:
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t5th\t${fifth_place_payout}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t6th\t${sixth_place_payout}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t7th\t${seventh_place_payout}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t8th\t${eighth_place_payout}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t9th\t${ninth_place_payout}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t10th\t${tenth_place_payout}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t11th\t${eleventh_place_payout}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t12th\t${twelth_place_payout}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t13th\t${self.entry_fee}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t14th\t${self.entry_fee}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t15th\t${self.entry_fee}\n")
                results_file.write(f"${self.entry_fee}\t{self.player_count}\t16th\t${self.entry_fee}\n")
