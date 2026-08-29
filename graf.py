import pickle
import matplotlib.pyplot as plt
import numpy as np


# -------------------------
# Last inn Q-tabellen
# -------------------------

with open("tabell.pkl", "rb") as f:
    qTable = pickle.load(f)


# Actions
action_names = {
    0: "S",   # Stand
    1: "H",   # Hit
    2: "D"    # Double
}


dealer_cards = list(range(2, 12))     # 2 ... 10, ess=11
player_sums = list(range(4, 22))      # 4 ... 21


# -------------------------
# Finn beste action
# -------------------------

def best_action(player_sum, dealer_card, soft):

    # Siden dealerSoft ikke egentlig er informasjon
    # spilleren trenger, antar vi False her.
    state = (
        player_sum,
        dealer_card,
        soft,
        False
    )

    if state not in qTable:
        return "-"

    qValues = qTable[state]

    # Hvis staten aldri egentlig har blitt lært
    if all(q == 0 for q in qValues):
        return "?"

    action = int(np.argmax(qValues))

    return action_names[action]


# -------------------------
# Lag tabell
# -------------------------

def create_chart(soft=False):

    table = []

    for player_sum in player_sums:

        row = []

        for dealer_card in dealer_cards:
            action = best_action(
                player_sum,
                dealer_card,
                soft
            )

            row.append(action)

        table.append(row)


    fig, ax = plt.subplots(figsize=(12, 10))

    ax.axis("off")


    dealer_labels = [
        "2", "3", "4", "5", "6",
        "7", "8", "9", "10", "A"
    ]

    row_labels = [
        str(x) for x in player_sums
    ]


    table_plot = ax.table(
        cellText=table,
        rowLabels=row_labels,
        colLabels=dealer_labels,
        cellLoc="center",
        loc="center"
    )


    table_plot.auto_set_font_size(False)
    table_plot.set_fontsize(15)
    table_plot.scale(1, 1.8)


    # Fargelegg actions
    for (row, col), cell in table_plot.get_celld().items():

        text = cell.get_text().get_text()

        if text == "H":
            cell.set_facecolor("lightgreen")

        elif text == "S":
            cell.set_facecolor("salmon")

        elif text == "D":
            cell.set_facecolor("gold")

        elif text == "?":
            cell.set_facecolor("lightgray")


    if soft:
        title = "Blackjack RL Strategy - Soft Hands"
    else:
        title = "Blackjack RL Strategy - Hard Hands"

    plt.title(
        title,
        fontsize=20,
        pad=20
    )

    plt.xlabel("Dealer upcard")

    plt.tight_layout()

    filename = "soft_strategy.png" if soft else "hard_strategy.png"

    plt.savefig(
        filename,
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()


# -------------------------
# Lag begge
# -------------------------

create_chart(soft=False)
create_chart(soft=True)