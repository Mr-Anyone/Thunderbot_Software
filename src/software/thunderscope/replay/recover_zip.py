import random
from software.thunderscope.replay.proto_logger import ProtoLogger
import base64
from software.thunderscope.replay.replay_constants import *
from software.thunderscope.replay.proto_player import ProtoPlayer
import gzip
import os
import shutil

#def mkdir(path):
#    shutil.rmtree(path)
#
#    try:
#        os.mkdir(path)
#    except Exception as e:
#        pass
#
#def has_timestamp_in_message(message):
#    try:
#        if message.time_sent.epoch_timestamp_seconds > 1611235119:
#            return True
#        return False
#    except Exception:
#        return False
#
#def recover_protobufs(path_to_recover, export_path):
#    print("I am going to recover {}".format(path_to_recover))
#    mkdir(export_path)
#
#    messages_that_has_timestamp = []
#
#    for file in os.listdir(path_to_recover):
#        path_to_file = os.path.join(path_to_recover, file)
#        #ProtoLogger.create_log_entry(, 10)
#        entries = ProtoPlayer.load_replay_chunk(path_to_file)
#        for entry in entries:
#            _, _, message = ProtoPlayer.unpack_log_entry(entry)
#
#            if has_timestamp_in_message(message):
#                messages_that_has_timestamp.append(message)
#
#    print("There are {} messages in the list".format(len(messages_that_has_timestamp)))
#    sorted(messages_that_has_timestamp, key=lambda x: x.time_sent.epoch_timestamp_seconds)
#
#    # write file to export path
#    smallest_timestamp = messages_that_has_timestamp[0].time_sent.epoch_timestamp_seconds
#    with gzip.open(os.path.join(export_path, "0.replay"), "wb") as f:
#        for message in messages_that_has_timestamp:
#            current_time = message.time_sent.epoch_timestamp_seconds - smallest_timestamp
#            log_entry = ProtoLogger.create_log_entry(message, current_time)
#            
#            f.write(bytes(log_entry, encoding='utf-8'))


def create_invalid_log_entries(proto, current_time, frequency=0.1):
    some_value = random.random()

    # remove some delimeter
    if some_value < frequency/2: 
        # intentionally corrupt some entries 
        serialized_proto = base64.b64encode(proto.SerializeToString())
        log_entry = (
            f"{current_time}"
            + f"{proto.DESCRIPTOR.full_name}{REPLAY_METADATA_DELIMETER}"
            + f"{serialized_proto}\n"
        )
        return log_entry
    # create invalid/corrupt data
    elif some_value < frequency:
        # intentionally corrupt some entries 
        serialized_proto = base64.b64encode(proto.SerializeToString())
        log_entry = (
            f"{current_time}{REPLAY_METADATA_DELIMETER}"
            + f"{proto.DESCRIPTOR.full_name}inserting some random dataa so that proto player would fail!{REPLAY_METADATA_DELIMETER}"
            + f"{serialized_proto} this is some random line aswell\n"
        )
        return log_entry

    # intentionally corrupt some entries 
    serialized_proto = base64.b64encode(proto.SerializeToString())
    log_entry = (
        f"{current_time}{REPLAY_METADATA_DELIMETER}"
        + f"{proto.DESCRIPTOR.full_name}{REPLAY_METADATA_DELIMETER}"
        + f"{serialized_proto}\n"
    )
    return log_entry
    
if __name__ == "__main__":
    path_to_recover = "/tmp/tbots/blue/proto_2024_05_27_060158"
    save_path = "/tmp/save"
    os.makedirs(save_path, exist_ok=True)

    sorted_chunks = sorted(os.listdir(path_to_recover))
    count = 0 
    for file in sorted_chunks:
        path_to_file = os.path.join(path_to_recover, file)
        print(f"Writing file: {path_to_file}")
        chunks = ProtoPlayer.load_replay_chunk(path_to_file)

        with gzip.open(os.path.join(save_path, f"{count}.replay"), "wb") as log_file:
            for log_entries in chunks:
                timestamp, proto_class, message = ProtoPlayer.unpack_log_entry(log_entries)
                log_entries = create_invalid_log_entries(message, timestamp)
                log_file.write(bytes(log_entries, encoding='utf-8'))
            count += 1

    #recover_protobufs(path_to_recover, export_path)

