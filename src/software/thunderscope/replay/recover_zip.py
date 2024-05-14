from software.thunderscope.replay.proto_logger import ProtoLogger
from software.thunderscope.replay.proto_player import ProtoPlayer
import gzip
import os
import shutil

def mkdir(path):
    shutil.rmtree(path)

    try:
        os.mkdir(path)
    except Exception as e:
        pass

def has_timestamp_in_message(message):
    try:
        if message.time_sent.epoch_timestamp_seconds > 1611235119:
            return True
        return False
    except Exception:
        return False

def recover_protobufs(path_to_recover, export_path):
    print("I am going to recover {}".format(path_to_recover))
    mkdir(export_path)

    messages_that_has_timestamp = []

    for file in os.listdir(path_to_recover):
        path_to_file = os.path.join(path_to_recover, file)
        #ProtoLogger.create_log_entry(, 10)
        entries = ProtoPlayer.load_replay_chunk(path_to_file)
        for entry in entries:
            _, _, message = ProtoPlayer.unpack_log_entry(entry)

            if has_timestamp_in_message(message):
                messages_that_has_timestamp.append(message)

    print("There are {} messages in the list".format(len(messages_that_has_timestamp)))
    sorted(messages_that_has_timestamp, key=lambda x: x.time_sent.epoch_timestamp_seconds)

    # write file to export path
    smallest_timestamp = messages_that_has_timestamp[0].time_sent.epoch_timestamp_seconds
    with gzip.open(os.path.join(export_path, "0.replay"), "wb") as f:
        for message in messages_that_has_timestamp:
            current_time = message.time_sent.epoch_timestamp_seconds - smallest_timestamp
            log_entry = ProtoLogger.create_log_entry(message, current_time)
            
            f.write(bytes(log_entry, encoding='utf-8'))

if __name__ == "__main__":
    path_to_recover = "/tmp/test"
    export_path = "/tmp/export"

    recover_protobufs(path_to_recover, export_path)

