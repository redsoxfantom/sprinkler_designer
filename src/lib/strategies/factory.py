from src.lib.strategies.randomstrategy import RandomStrategy
from src.lib.strategies.basestrategy import BaseStrategy


def createStrategy(strategyconfig, scorer, sprinklers):
    type = strategyconfig['type']
    data = strategyconfig['data']
    strategyswitch = {
        "RANDOM": RandomStrategy
    }

    strategy = strategyswitch.get(type, BaseStrategy)
    return strategy(data, scorer, sprinklers)