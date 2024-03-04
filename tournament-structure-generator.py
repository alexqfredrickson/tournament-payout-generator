import math

player_count = range(32, 65)
entry_fee = [10, 15, 20]

for e in entry_fee:
    for p in player_count:
        first_place, second_place, third_place, fourth_place, fifth_sixth_place = None,  None,  None,  None,  None

        total_payout = e * p

        structure_is_32_to_48_range = 32 <= p <= 47

        first_place_pct_32_to_48 = .35
        second_place_pct_32_to_48 = .20
        third_place_pct_32_to_48 = .15
        forth_place_pct_32_to_48 = .10
        fifth_sixth_pct_32_to_48 = .05

        first_place_pct_48_to_64 = .33
        second_place_pct_48_to_64 = .20
        third_place_pct_48_to_64 = .15
        forth_place_pct_48_to_64 = .12
        fifth_sixth_pct_48_to_64 = .06
        seventh_eighth_pct_48_to_64 = .04

        rebated_player_count = math.floor(p / 4) - (6 if structure_is_32_to_48_range else 8)

        (first_place_payout, second_place_payout, third_place_payout, fourth_place_payout,
         fifth_sixth_place_payout, seventh_eighth_place_payout) = 0, 0, 0, 0, 0, 0

        total_payout -= rebated_player_count * e

        if structure_is_32_to_48_range:
            first_place_payout = math.floor(total_payout * first_place_pct_32_to_48)
            second_place_payout = math.floor(total_payout * second_place_pct_32_to_48)
            third_place_payout = math.floor(total_payout * third_place_pct_32_to_48)
            fourth_place_payout = math.floor(total_payout * forth_place_pct_32_to_48)
            fifth_sixth_place_payout = math.floor(total_payout * fifth_sixth_pct_32_to_48)
        else:
            first_place_payout = math.floor(total_payout * first_place_pct_48_to_64)
            second_place_payout = math.floor(total_payout * second_place_pct_48_to_64)
            third_place_payout = math.floor(total_payout * third_place_pct_48_to_64)
            fourth_place_payout = math.floor(total_payout * forth_place_pct_48_to_64)
            fifth_sixth_place_payout = math.floor(total_payout * fifth_sixth_pct_48_to_64)
            seventh_eighth_place_payout = math.floor(total_payout * seventh_eighth_pct_48_to_64)

        total_payout = e * p

        # print(f"DEBUG | {p} | payouts thus far:")
        # adjust first place prize
        first_place_payout += ((total_payout - first_place_payout - second_place_payout - third_place_payout -
                               fourth_place_payout - fifth_sixth_place_payout * 2 -
                               (seventh_eighth_place_payout * 2 if not structure_is_32_to_48_range else 0)) -
                               (rebated_player_count * e))

        print(f"${e}\t{p}\t1st\t{first_place_payout}")
        print(f"${e}\t{p}\t2nd\t{second_place_payout}")
        print(f"${e}\t{p}\t3rd\t{third_place_payout}")
        print(f"${e}\t{p}\t4th\t{fourth_place_payout}")
        print(f"${e}\t{p}\t5th\t{fifth_sixth_place_payout}")
        print(f"${e}\t{p}\t6th\t{fifth_sixth_place_payout}")

        if structure_is_32_to_48_range:
            for x in range(7, 7 + rebated_player_count):
                print(f"${e}\t{p}\t{x}th\t{e}")
        else:
            print(f"${e}\t{p}\t7th\t{seventh_eighth_place_payout}")
            print(f"${e}\t{p}\t8th\t{seventh_eighth_place_payout}")

            for x in range(9, 9 + rebated_player_count):
                print(f"${e}\t{p}\t{x}th\t{e}")
