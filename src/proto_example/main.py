# import the acutal protobuf, in our code base the import_all_protos import all the protobuf
import os 
print(os.getcwd())
from proto_example.person_pb2 import Person

person = Person()
person.first_name = "Someone"
person.last_name = "Someone's Lastname"

print(f"their first name  is {person.first_name}")
print(f"their last name  is {person.last_name}")

# we cannot do this, uncomment and see
#print(f"their first name  is {person.first_name()}")

# an simple way think about this is that protoc generates a python file that is like the following
#class Person: 
# ....some_internal implementation... 
#    first_nme: str
#    last_name: str
