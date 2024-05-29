import base64
import glob
import gzip
import os
import argparse

from proto.import_all_protos import *
from software.thunderscope.replay.replay_constants import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script for debugging replay files"
    )
    parser.add_argument(
        "--replay_dir",
        action="store",
        help=f"Folder containing the .{REPLAY_FILE_EXTENSION} files",
        required=True,
        type=os.path.abspath,
    )
    args = parser.parse_args()

    # Load up all replay files in the log folder
    replay_files = glob.glob(args.replay_dir + f"/*.{REPLAY_FILE_EXTENSION}")

    # Sort the files by their chunk index
    def __sort_replay_chunks(file_path: str):
        head, tail = os.path.split(file_path)
        replay_index, _ = tail.split(".")
        return int(replay_index)


    sorted_chunks = sorted(replay_files, key=__sort_replay_chunks)

    print(f"Found {len(sorted_chunks)} replay files in {args.replay_dir}")

    total_line_num = 0
    for replay_file_name in sorted_chunks:
        print(f"Replaying {replay_file_name}...")
        with gzip.open(replay_file_name, "rb") as replay_file:
            line = replay_file.readline()
            line_num = 0
            while line is not None:
                try:
                    timestamp, protobuf_type, data = line.split(
                        bytes(REPLAY_METADATA_DELIMETER, encoding="utf-8")
                    )
                except ValueError:
                    raise ValueError(f"Unable to split line {line_num} of replay file {replay_file_name}. Line: {line}")

                try:
                    # The format of the protobuf type is:
                    # package.proto_class (e.g. TbotsProto.Primitive)
                    proto_class = eval(str(protobuf_type.split(b".")[-1], encoding="utf-8"))
                except NameError:
                    raise TypeError(f"Unknown proto type in replay: '{protobuf_type}'")

                # Deserialize protobuf
                proto = proto_class.FromString(base64.b64decode(data[len("b"): -len("\n")]))

                #######################################
                # Do something with the protobuf here #
                #######################################
                print(f"{line_num}: {float(timestamp)}: {protobuf_type} - {proto=}")

                line = replay_file.readline()
                line_num += 1

            total_line_num += line_num

    print(f"Replayed {total_line_num} log lines and found no errors.")
