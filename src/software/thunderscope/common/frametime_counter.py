import time
import collections
import statistics


class FrameTimeCounter:
    """FrameTimeCounter is basically just a list that stores the time difference
    between each consecutive function call.

    From that, it calculates the frametime of each function call, i.e. the time
    between each function call.
    """

    def __init__(self, save_to_file=False, path_to_file="/tmp/fps.txt") -> None:
        """Initialize FrameTimeCounter"""
        # Stores the frametime of every data cycle
        self.datapoints = collections.deque(maxlen= None if save_to_file else 3600)
        self.previous_timestamp = time.time()

        self.save_to_file = save_to_file
        self.path_to_file = path_to_file
        self.save_count = 0 # the number of times a self.add_one_datapoint has been called

    def _save_to_disk(self):
        if self.save_count % 1000 != 0:
            return

        # update every 1000 updates
        with open(self.path_to_file, "w") as f:
            f.write("last: {} last 3600: {} all: {}".format(self.get_last_frametime(),
                                                          self.get_average_last_3600(),
                                                          self.get_average_frametime()))

    def add_one_datapoint(self) -> None:
        """Save the time difference between each consecutive function call."""
        self.save_count += 1
        self._save_to_disk()

        current_time = time.time()
        time_difference = current_time - self.previous_timestamp
        self.datapoints.append(time_difference)
        self.previous_timestamp = current_time

    def get_last_frametime(self) -> float:
        """Return the latest frametime from the list

        :return: the latest frametime, and -1 if the list is empty
        """
        if not self.datapoints:
            return -1

        return self.datapoints[-1]

    def get_average_frametime(self) -> float:
        """Average the entire list

        :return: the average of the entire list, and -1 if the list is empty
        """
        if not self.datapoints:
            return -1

        return statistics.mean(self.datapoints)

    def get_average_last_3600(self) -> float:
        """Average the last 3600 frametime

        :return: the average of the last 3600 frametime
        """
        if not self.datapoints:
            return -1

        return statistics.mean(list(self.datapoints)[-3600:])
