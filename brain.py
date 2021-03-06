__author__ = 'jae'

import transitions
import time

class DroneBrain(object):
    """
    Provides state machine logic for the drone.
    """
    states = ["rest", "search", "follow"]

    def __init__(self):
        """
        Initializes the drone.
        :return:
        """
        self.machine = transitions.Machine(model=self,
                                           states=DroneBrain.states,
                                           initial="rest")
        self.machine.add_transition(trigger="target_decided", source="search", dest="follow")
        self.last_target_detected_time = 0
        self.target = None

    def evaluate_targets(self, targets):
        """
        Return the target to follow.
        :param targets:
        :return:
        """
        self.last_target_detected_time = time.time()
        rect = max(targets, key=lambda rect: rect[3]*rect[4])
        return rect

    def choose_target(self, rect):
        """
        Choose a target to follow
        :param rect:
        :return:
        """
