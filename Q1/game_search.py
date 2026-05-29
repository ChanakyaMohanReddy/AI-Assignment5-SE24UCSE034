import math
import random
from copy import deepcopy


# game setup
class TicTacToe:
    def __init__(self, board=None, player="X"):
        self.board = board if board else [" "] * 9
        self.player = player

    def available_actions(self):
        return [i for i in range(9) if self.board[i] == " "]

    def make_move(self, action):
        new_board = self.board[:]
        new_board[action] = self.player
        next_player = "O" if self.player == "X" else "X"
        return TicTacToe(new_board, next_player)

    def winner(self):
        win_lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for a, b, c in win_lines:
            if self.board[a] != " " and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]

        if " " not in self.board:
            return "Draw"

        return None

    def is_terminal(self):
        return self.winner() is not None

    def utility(self):
        result = self.winner()

        if result == "X":
            return 1
        if result == "O":
            return -1

        return 0

    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i], "|", self.board[i + 1], "|", self.board[i + 2])

            if i < 6:
                print("--+---+--")


# minimax logic
def minimax(state):
    if state.is_terminal():
        return state.utility(), None

    if state.player == "X":
        best_value = -math.inf
        best_action = None

        for action in state.available_actions():
            value, _ = minimax(state.make_move(action))

            if value > best_value:
                best_value = value
                best_action = action

        return best_value, best_action

    best_value = math.inf
    best_action = None

    for action in state.available_actions():
        value, _ = minimax(state.make_move(action))

        if value < best_value:
            best_value = value
            best_action = action

    return best_value, best_action


# alpha beta pruning
def alpha_beta(state, alpha=-math.inf, beta=math.inf):
    if state.is_terminal():
        return state.utility(), None

    if state.player == "X":
        best_value = -math.inf
        best_action = None

        for action in state.available_actions():
            value, _ = alpha_beta(state.make_move(action), alpha, beta)

            if value > best_value:
                best_value = value
                best_action = action

            alpha = max(alpha, best_value)

            if alpha >= beta:
                break

        return best_value, best_action

    best_value = math.inf
    best_action = None

    for action in state.available_actions():
        value, _ = alpha_beta(state.make_move(action), alpha, beta)

        if value < best_value:
            best_value = value
            best_action = action

        beta = min(beta, best_value)

        if alpha >= beta:
            break

    return best_value, best_action


# checking board score
def heuristic_score(state):
    result = state.winner()

    if result == "X":
        return 100

    if result == "O":
        return -100

    if result == "Draw":
        return 0

    win_lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    score = 0

    for a, b, c in win_lines:
        line = [state.board[a], state.board[b], state.board[c]]

        if line.count("X") == 2 and line.count(" ") == 1:
            score += 10

        elif line.count("X") == 1 and line.count(" ") == 2:
            score += 1

        if line.count("O") == 2 and line.count(" ") == 1:
            score -= 10

        elif line.count("O") == 1 and line.count(" ") == 2:
            score -= 1

    return score


# heuristic alpha beta
def heuristic_alpha_beta(state, depth, alpha=-math.inf, beta=math.inf):
    if state.is_terminal() or depth == 0:
        return heuristic_score(state), None

    if state.player == "X":
        best_value = -math.inf
        best_action = None

        for action in state.available_actions():
            value, _ = heuristic_alpha_beta(
                state.make_move(action), depth - 1, alpha, beta
            )

            if value > best_value:
                best_value = value
                best_action = action

            alpha = max(alpha, best_value)

            if alpha >= beta:
                break

        return best_value, best_action

    best_value = math.inf
    best_action = None

    for action in state.available_actions():
        value, _ = heuristic_alpha_beta(
            state.make_move(action), depth - 1, alpha, beta
        )

        if value < best_value:
            best_value = value
            best_action = action

        beta = min(beta, best_value)

        if alpha >= beta:
            break

    return best_value, best_action


# node for mcts
class MCTSNode:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.children = []
        self.visits = 0
        self.score = 0
        self.untried_actions = state.available_actions()

    def fully_expanded(self):
        return len(self.untried_actions) == 0

    def best_child(self):
        best_value = -math.inf
        best_node = None

        for child in self.children:
            exploitation = child.score / (child.visits + 1e-9)

            exploration = math.sqrt(
                math.log(self.visits + 1) / (child.visits + 1e-9)
            )

            uct_value = exploitation + 1.41 * exploration

            if uct_value > best_value:
                best_value = uct_value
                best_node = child

        return best_node


# random simulation
def random_playout(state):
    current_state = deepcopy(state)

    while not current_state.is_terminal():
        action = random.choice(current_state.available_actions())
        current_state = current_state.make_move(action)

    return current_state.utility()


# monte carlo tree search
def monte_carlo_tree_search(state, iterations=500):
    root = MCTSNode(state)

    for _ in range(iterations):
        node = root

        while not node.state.is_terminal() and node.fully_expanded():
            node = node.best_child()

        if not node.state.is_terminal() and node.untried_actions:
            action = random.choice(node.untried_actions)

            node.untried_actions.remove(action)

            new_state = node.state.make_move(action)

            child = MCTSNode(new_state, node, action)

            node.children.append(child)

            node = child

        result = random_playout(node.state)

        while node is not None:
            node.visits += 1

            if result == 0:
                node.score += 0.5

            elif state.player == "X" and result == 1:
                node.score += 1

            elif state.player == "O" and result == -1:
                node.score += 1

            node = node.parent

    if not root.children:
        return None

    return max(
        root.children,
        key=lambda child: child.score / child.visits
    ).action


# test cases
def run_test_case(board, player):
    state = TicTacToe(board, player)

    print("\nCurrent Board:")
    state.print_board()

    print("\nPlayer to move:", player)

    minimax_value, minimax_move = minimax(state)

    ab_value, ab_move = alpha_beta(state)

    hab_value, hab_move = heuristic_alpha_beta(state, depth=3)

    mcts_move = monte_carlo_tree_search(state, iterations=500)

    print("\nMinimax Move:", minimax_move, "Value:", minimax_value)

    print("Alpha-Beta Move:", ab_move, "Value:", ab_value)

    print(
        "Heuristic Alpha-Beta Move:",
        hab_move,
        "Heuristic Value:",
        hab_value
    )

    print("MCTS Move:", mcts_move)


# main function
if __name__ == "__main__":
    print("TASK 1: Game Search Algorithms using Tic-Tac-Toe")

    board1 = [
        "X", "X", " ",
        "O", "O", " ",
        " ", " ", " "
    ]

    run_test_case(board1, "X")

    board2 = [
        "X", "O", "X",
        " ", "O", " ",
        " ", " ", " "
    ]

    run_test_case(board2, "X")

    board3 = [
        "X", "O", "X",
        "O", "X", " ",
        " ", " ", "O"
    ]

    run_test_case(board3, "X")

    board4 = [
        "O", "O", " ",
        "X", "X", " ",
        " ", " ", " "
    ]

    run_test_case(board4, "O")
