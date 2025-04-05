# 8.​ Use Python’s uuid module to generate a random device ID.
import uuid

# uuid4 generated from random number, not inlcuded the time and MAC address like uuid1
id = uuid.uuid4()
print("Generated UUID 4: ", id)
