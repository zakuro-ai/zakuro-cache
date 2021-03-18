
from zakuro_cache.decorators import zakuro_cache
from tqdm import tqdm
from datetime import datetime
import random


store ={}

import time

@zakuro_cache
def test():
    store[random.randrange(0, 3)] = datetime.now()
    # time.sleep(0.1)
    return 0

for _ in tqdm(range(1000000)):
    test()
print(store)