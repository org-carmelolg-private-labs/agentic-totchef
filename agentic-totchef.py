from lib.core.tools import KindergartenTools, HomeKitchenTools
from lib.core.providers import OllamaUtils

user_prompt = "Dammi le ricette casalinghe a base di verdure?"
#user_prompt = "Dammi il menu di martedì della seconda settimana del nido"
# get available functions
_functions = {}
_functions.update(KindergartenTools.available_functions())
_functions.update(HomeKitchenTools.available_functions())
functions = _functions

stream = OllamaUtils.chat(user_prompt=user_prompt, tools=functions)
for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
