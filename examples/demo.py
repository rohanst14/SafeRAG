from saferag import *
import json
print(json.dumps(answer("reactor pressure",{"manual":"reactor pressure rises","other":"ocean waves"}),indent=2))
