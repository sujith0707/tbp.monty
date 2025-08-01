# Copyright 2025 Thousand Brains Project
# Copyright 2024 Numenta Inc.
#
# Copyright may exist in Contributors' modifications
# and/or contributions to the work.
#
# Use of this source code is governed by the MIT
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

import json
import unittest
from typing import cast
from unittest.mock import Mock

from tbp.monty.frameworks.actions.actions import (
    ActionJSONDecoder,
    ActionJSONEncoder,
    LookDown,
    LookUp,
    MoveForward,
    MoveTangentially,
    OrientHorizontal,
    OrientVertical,
    SetAgentPitch,
    SetAgentPose,
    SetSensorPitch,
    SetSensorPose,
    SetSensorRotation,
    SetYaw,
    TurnLeft,
    TurnRight,
)
from tests.unit.frameworks.actions.fakes.action import FakeAction


class ActionTest(unittest.TestCase):
    def test_action_name_is_class_name_in_snake_case(self) -> None:
        self.assertEqual("fake_action", FakeAction.action_name())

    def test_name_is_class_name_in_snake_case(self) -> None:
        fake_action = FakeAction(agent_id="test")
        self.assertEqual("fake_action", fake_action.name)

    def test_agent_id_returns_configured_agent_id(self) -> None:
        fake_action = FakeAction(agent_id="test")
        self.assertEqual("test", fake_action.agent_id)


class LookDownTest(unittest.TestCase):
    def setUp(self) -> None:
        self.action = LookDown(agent_id="test", rotation_degrees=47)

    def test_delegates_to_sample_look_down(self) -> None:
        sampler = Mock()
        sampler.sample_look_down = Mock()
        LookDown.sample(agent_id="test", sampler=sampler)
        sampler.sample_look_down.assert_called_once_with("test")

    def test_delegates_to_actuate_look_down(self) -> None:
        actuator = Mock()
        actuator.actuate_look_down = Mock()
        self.action.act(actuator)
        actuator.actuate_look_down.assert_called_once_with(self.action)

    def test_rotation_degrees_returns_configured_rotation_degrees(self) -> None:
        self.assertEqual(47, self.action.rotation_degrees)

    def test_constraint_degrees_returns_90_degrees_by_default(self) -> None:
        self.assertEqual(90, self.action.constraint_degrees)

    def test_constraint_degrees_returns_configured_constraint_degrees(self) -> None:
        action = LookDown(agent_id="test", rotation_degrees=47, constraint_degrees=45)
        self.assertEqual(45, action.constraint_degrees)

    def test_json_serialization(self) -> None:
        s = json.dumps(self.action, cls=ActionJSONEncoder)
        action = cast(LookUp, json.loads(s, cls=ActionJSONDecoder))
        self.assertEqual(self.action.agent_id, action.agent_id)
        self.assertEqual(self.action.rotation_degrees, action.rotation_degrees)
        self.assertEqual(self.action.constraint_degrees, action.constraint_degrees)

    def test_dict(self) -> None:
        d = dict(self.action)
        self.assertDictEqual(
            d,
            {
                "action": self.action.name,
                "agent_id": "test",
                "rotation_degrees": 47,
                "constraint_degrees": 90,
            },
        )


class LookUpTest(unittest.TestCase):
    def setUp(self) -> None:
        self.action = LookUp(agent_id="test", rotation_degrees=77)

    def test_delegates_to_sample_look_up(self) -> None:
        sampler = Mock()
        sampler.sample_look_up = Mock()
        LookUp.sample(agent_id="test", sampler=sampler)
        sampler.sample_look_up.assert_called_once_with("test")

    def test_delegates_to_actuate_look_up(self) -> None:
        actuator = Mock()
        actuator.actuate_look_up = Mock()
        self.action.act(actuator)
        actuator.actuate_look_up.assert_called_once_with(self.action)

    def test_rotation_degrees_returns_configured_rotation_degrees(self) -> None:
        self.assertEqual(77, self.action.rotation_degrees)

    def test_constraint_degrees_returns_90_degrees_by_default(self) -> None:
        self.assertEqual(90, self.action.constraint_degrees)

    def test_constraint_degrees_returns_configured_constraint_degrees(self) -> None:
        action = LookUp(agent_id="test", rotation_degrees=77, constraint_degrees=45)
        self.assertEqual(45, action.constraint_degrees)

    def test_json_serialization(self) -> None:
        s = json.dumps(self.action, cls=ActionJSONEncoder)
        action = cast(LookUp, json.loads(s, cls=ActionJSONDecoder))
        self.assertEqual(self.action.agent_id, action.agent_id)
        self.assertEqual(self.action.rotation_degrees, action.rotation_degrees)
        self.assertEqual(self.action.constraint_degrees, action.constraint_degrees)

    def test_dict(self) -> None:
        d = dict(self.action)
        self.assertDictEqual(
            d,
            {
                "action": self.action.name,
                "agent_id": "test",
                "rotation_degrees": 77,
                "constraint_degrees": 90,
            },
        )


class MoveForwardTest(unittest.TestCase):
    def setUp(self) -> None:
        self.action = MoveForward(agent_id="test", distance=1)

    def test_delegates_to_sample_move_forward(self) -> None:
        sampler = Mock()
        sampler.sample_move_forward = Mock()
        MoveForward.sample(agent_id="test", sampler=sampler)
        sampler.sample_move_forward.assert_called_once_with("test")

    def test_delegates_to_actuate_move_forward(self) -> None:
        actuator = Mock()
        actuator.actuate_move_forward = Mock()
        self.action.act(actuator)
        actuator.actuate_move_forward.assert_called_once_with(self.action)

    def test_distance_returns_configured_distance(self) -> None:
        self.assertEqual(1, self.action.distance)

    def test_json_serialization(self) -> None:
        s = json.dumps(self.action, cls=ActionJSONEncoder)
        action = cast(MoveForward, json.loads(s, cls=ActionJSONDecoder))
        self.assertEqual(self.action.agent_id, action.agent_id)
        self.assertEqual(self.action.distance, action.distance)

    def test_dict(self) -> None:
        d = dict(self.action)
        self.assertDictEqual(
            d,
            {
                "action": self.action.name,
                "agent_id": "test",
                "distance": 1,
            },
        )


class MoveTangentiallyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.action = MoveTangentially(agent_id="test", distance=1, direction=(1, 2, 3))

    def test_delegates_to_sample_move_tangentially(self) -> None:
        sampler = Mock()
        sampler.sample_move_tangentially = Mock()
        MoveTangentially.sample(agent_id="test", sampler=sampler)
        sampler.sample_move_tangentially.assert_called_once_with("test")

    def test_delegates_to_actuate_move_tangentially(self) -> None:
        actuator = Mock()
        actuator.actuate_move_tangentially = Mock()
        self.action.act(actuator)
        actuator.actuate_move_tangentially.assert_called_once_with(self.action)

    def test_distance_returns_configured_distance(self) -> None:
        self.assertEqual(1, self.action.distance)

    def test_direction_returns_configured_direction(self) -> None:
        self.assertEqual((1, 2, 3), self.action.direction)

    def test_json_serialization(self) -> None:
        s = json.dumps(self.action, cls=ActionJSONEncoder)
        action = cast(MoveTangentially, json.loads(s, cls=ActionJSONDecoder))
        self.assertEqual(self.action.agent_id, action.agent_id)
        self.assertEqual(self.action.distance, action.distance)
        self.assertEqual(self.action.direction, action.direction)

    def test_dict(self) -> None:
        d = dict(self.action)
        self.assertDictEqual(
            d,
            {
                "action": self.action.name,
                "agent_id": "test",
                "distance": 1,
                "direction": (1, 2, 3),
            },
        )
        action = MoveTangentially(agent_id="test", distance=1, direction=(1, 2, 3))
        d = dict(action)
        self.assertEqual(d["action"], action.name)
        self.assertEqual(d["agent_id"], "test")
        self.assertEqual(d["distance"], 1)
        self.assertEqual(d["direction"], (1, 2, 3))


class OrientHorizontalTest(unittest.TestCase):
    def setUp(self) -> None:
        self.action = OrientHorizontal(
            agent_id="test", rotation_degrees=90, left_distance=1, forward_distance=1
        )

    def test_delegates_to_sample_orient_horizontal(self) -> None:
        sampler = Mock()
        sampler.sample_orient_horizontal = Mock()
        OrientHorizontal.sample(agent_id="test", sampler=sampler)
        sampler.sample_orient_horizontal.assert_called_once_with("test")

    def test_delegates_to_actuate_orient_horizontal(self) -> None:
        actuator = Mock()
        actuator.actuate_orient_horizontal = Mock()
        self.action.act(actuator)
        actuator.actuate_orient_horizontal.assert_called_once_with(self.action)

    def test_rotation_degrees_returns_configured_rotation_degrees(self) -> None:
        self.assertEqual(90, self.action.rotation_degrees)

    def test_left_distance_returns_configured_left_distance(self) -> None:
        self.assertEqual(1, self.action.left_distance)

    def test_forward_distance_returns_configured_forward_distance(self) -> None:
        self.assertEqual(1, self.action.forward_distance)

    def test_json_serialization(self) -> None:
        s = json.dumps(self.action, cls=ActionJSONEncoder)
        action = cast(OrientHorizontal, json.loads(s, cls=ActionJSONDecoder))
        self.assertEqual(self.action.agent_id, action.agent_id)
        self.assertEqual(self.action.rotation_degrees, action.rotation_degrees)
        self.assertEqual(self.action.left_distance, action.left_distance)
        self.assertEqual(self.action.forward_distance, action.forward_distance)

    def test_dict(self) -> None:
        d = dict(self.action)
        self.assertDictEqual(
            d,
            {
                "action": self.action.name,
                "agent_id": "test",
                "rotation_degrees": 90,
                "left_distance": 1,
                "forward_distance": 1,
            },
        )


class OrientVerticalTest(unittest.TestCase):
    def setUp(self) -> None:
        self.action = OrientVertical(
            agent_id="test", rotation_degrees=90, down_distance=1, forward_distance=1
        )

    def test_delegates_to_sample_orient_vertical(self) -> None:
        sampler = Mock()
        sampler.sample_orient_vertical = Mock()
        OrientVertical.sample(agent_id="test", sampler=sampler)
        sampler.sample_orient_vertical.assert_called_once_with("test")

    def test_delegates_to_actuate_orient_vertical(self) -> None:
        actuator = Mock()
        actuator.actuate_orient_vertical = Mock()
        self.action.act(actuator)
        actuator.actuate_orient_vertical.assert_called_once_with(self.action)

    def test_rotation_degrees_returns_configured_rotation_degrees(self) -> None:
        self.assertEqual(90, self.action.rotation_degrees)

    def test_down_distance_returns_configured_down_distance(self) -> None:
        self.assertEqual(1, self.action.down_distance)

    def test_forward_distance_returns_configured_forward_distance(self) -> None:
        self.assertEqual(1, self.action.forward_distance)

    def test_json_serialization(self) -> None:
        s = json.dumps(self.action, cls=ActionJSONEncoder)
        action = cast(OrientVertical, json.loads(s, cls=ActionJSONDecoder))
        self.assertEqual(self.action.agent_id, action.agent_id)
        self.assertEqual(self.action.rotation_degrees, action.rotation_degrees)
        self.assertEqual(self.action.down_distance, action.down_distance)
        self.assertEqual(self.action.forward_distance, action.forward_distance)

    def test_dict(self) -> None:
        d = dict(self.action)
        self.assertDictEqual(
            d,
            {
                "action": self.action.name,
                "agent_id": "test",
                "rotation_degrees": 90,
                "down_distance": 1,
                "forward_distance": 1,
            },
        )


class SetAgentPitchTest(unittest.TestCase):
    def setUp(self) -> None:
        self.action = SetAgentPitch(agent_id="test", pitch_degrees=90)

    def test_delegates_to_sample_set_agent_pitch(self) -> None:
        sampler = Mock()
        sampler.sample_set_agent_pitch = Mock()
        SetAgentPitch.sample(agent_id="test", sampler=sampler)
        sampler.sample_set_agent_pitch.assert_called_once_with("test")

    def test_delegates_to_actuate_set_agent_pitch(self) -> None:
        actuator = Mock()
        actuator.actuate_set_agent_pitch = Mock()
        self.action.act(actuator)
        actuator.actuate_set_agent_pitch.assert_called_once_with(self.action)

    def test_pitch_degrees_returns_configured_pitch_degrees(self) -> None:
        self.assertEqual(90, self.action.pitch_degrees)

    def test_json_serialization(self) -> None:
        s = json.dumps(self.action, cls=ActionJSONEncoder)
        action = cast(SetAgentPitch, json.loads(s, cls=ActionJSONDecoder))
        self.assertEqual(self.action.agent_id, action.agent_id)
        self.assertEqual(self.action.pitch_degrees, action.pitch_degrees)

    def test_dict(self) -> None:
        d = dict(self.action)
        self.assertDictEqual(
            d,
            {
                "action": self.action.name,
                "agent_id": "test",
                "pitch_degrees": 90,
            },
        )


class SetAgentPoseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.action = SetAgentPose(
            agent_id="test", location=(1, 2, 3), rotation_quat=(1, 2, 3, 4)
        )

    def test_delegates_to_sample_set_agent_pose(self) -> None:
        sampler = Mock()
        sampler.sample_set_agent_pose = Mock()
        SetAgentPose.sample(agent_id="test", sampler=sampler)
        sampler.sample_set_agent_pose.assert_called_once_with("test")

    def test_delegates_to_actuate_set_agent_pose(self) -> None:
        actuator = Mock()
        actuator.actuate_set_agent_pose = Mock()
        self.action.act(actuator)
        actuator.actuate_set_agent_pose.assert_called_once_with(self.action)

    def test_location_returns_configured_location(self) -> None:
        self.assertEqual((1, 2, 3), self.action.location)

    def test_rotation_returns_configured_rotation(self) -> None:
        self.assertEqual((1, 2, 3, 4), self.action.rotation_quat)

    def test_json_serialization(self) -> None:
        s = json.dumps(self.action, cls=ActionJSONEncoder)
        action = cast(SetAgentPose, json.loads(s, cls=ActionJSONDecoder))
        self.assertEqual(self.action.agent_id, action.agent_id)
        self.assertEqual(self.action.location, action.location)
        self.assertEqual(self.action.rotation_quat, action.rotation_quat)

    def test_dict(self) -> None:
        d = dict(self.action)
        self.assertDictEqual(
            d,
            {
                "action": self.action.name,
                "agent_id": "test",
                "location": (1, 2, 3),
                "rotation_quat": (1, 2, 3, 4),
            },
        )
        action = SetAgentPose(
            agent_id="test",
            location=(1, 2, 3),
            rotation_quat=(1, 2, 3, 4),
        )
        d = dict(action)
        self.assertEqual(d["action"], action.name)
        self.assertEqual(d["agent_id"], "test")
        self.assertEqual(d["location"], (1, 2, 3))
        self.assertEqual(d["rotation_quat"], (1, 2, 3, 4))


class SetSensorPitchTest(unittest.TestCase):
    def setUp(self) -> None:
        self.action = SetSensorPitch(agent_id="test", pitch_degrees=90)

    def test_delegates_to_sample_set_sensor_pitch(self) -> None:
        sampler = Mock()
        sampler.sample_set_sensor_pitch = Mock()
        SetSensorPitch.sample(agent_id="test", sampler=sampler)
        sampler.sample_set_sensor_pitch.assert_called_once_with("test")

    def test_delegates_to_actuate_set_sensor_pitch(self) -> None:
        actuator = Mock()
        actuator.actuate_set_sensor_pitch = Mock()
        self.action.act(actuator)
        actuator.actuate_set_sensor_pitch.assert_called_once_with(self.action)

    def test_pitch_degrees_returns_configured_pitch_degrees(self) -> None:
        self.assertEqual(90, self.action.pitch_degrees)

    def test_json_serialization(self) -> None:
        s = json.dumps(self.action, cls=ActionJSONEncoder)
        action = cast(SetSensorPitch, json.loads(s, cls=ActionJSONDecoder))
        self.assertEqual(self.action.agent_id, action.agent_id)
        self.assertEqual(self.action.pitch_degrees, action.pitch_degrees)

    def test_dict(self) -> None:
        d = dict(self.action)
        self.assertDictEqual(
            d,
            {
                "action": self.action.name,
                "agent_id": "test",
                "pitch_degrees": 90,
            },
        )


class SetSensorPoseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.action = SetSensorPose(
            agent_id="test", location=(1, 2, 3), rotation_quat=(1, 2, 3, 4)
        )

    def test_delegates_to_sample_set_sensor_pose(self) -> None:
        sampler = Mock()
        sampler.sample_set_sensor_pose = Mock()
        SetSensorPose.sample(agent_id="test", sampler=sampler)
        sampler.sample_set_sensor_pose.assert_called_once_with("test")

    def test_delegates_to_actuate_set_sensor_pose(self) -> None:
        actuator = Mock()
        actuator.actuate_set_sensor_pose = Mock()
        self.action.act(actuator)
        actuator.actuate_set_sensor_pose.assert_called_once_with(self.action)

    def test_location_returns_configured_location(self) -> None:
        self.assertEqual((1, 2, 3), self.action.location)

    def test_rotation_returns_configured_rotation(self) -> None:
        self.assertEqual((1, 2, 3, 4), self.action.rotation_quat)

    def test_json_serialization(self) -> None:
        s = json.dumps(self.action, cls=ActionJSONEncoder)
        action = cast(SetSensorPose, json.loads(s, cls=ActionJSONDecoder))
        self.assertEqual(self.action.agent_id, action.agent_id)
        self.assertEqual(self.action.location, action.location)
        self.assertEqual(self.action.rotation_quat, action.rotation_quat)

    def test_dict(self) -> None:
        d = dict(self.action)
        self.assertDictEqual(
            d,
            {
                "action": self.action.name,
                "agent_id": "test",
                "location": (1, 2, 3),
                "rotation_quat": (1, 2, 3, 4),
            },
        )
        action = SetSensorPose(
            agent_id="test",
            location=(1, 2, 3),
            rotation_quat=(1, 2, 3, 4),
        )
        d = dict(action)
        self.assertEqual(d["action"], action.name)
        self.assertEqual(d["agent_id"], "test")
        self.assertEqual(d["location"], (1, 2, 3))
        self.assertEqual(d["rotation_quat"], (1, 2, 3, 4))


class SetSensorRotationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.action = SetSensorRotation(agent_id="test", rotation_quat=(1, 2, 3, 4))

    def test_delegates_to_sample_set_sensor_rotation(self) -> None:
        sampler = Mock()
        sampler.sample_set_sensor_rotation = Mock()
        SetSensorRotation.sample(agent_id="test", sampler=sampler)
        sampler.sample_set_sensor_rotation.assert_called_once_with("test")

    def test_delegates_to_actuate_set_sensor_rotation(self) -> None:
        actuator = Mock()
        actuator.actuate_set_sensor_rotation = Mock()
        self.action.act(actuator)
        actuator.actuate_set_sensor_rotation.assert_called_once_with(self.action)

    def test_rotation_returns_configured_rotation(self) -> None:
        self.assertEqual((1, 2, 3, 4), self.action.rotation_quat)

    def test_json_serialization(self) -> None:
        s = json.dumps(self.action, cls=ActionJSONEncoder)
        action = cast(SetSensorRotation, json.loads(s, cls=ActionJSONDecoder))
        self.assertEqual(self.action.agent_id, action.agent_id)
        self.assertEqual(self.action.rotation_quat, action.rotation_quat)

    def test_dict(self) -> None:
        d = dict(self.action)
        self.assertDictEqual(
            d,
            {
                "action": self.action.name,
                "agent_id": "test",
                "rotation_quat": (1, 2, 3, 4),
            },
        )
        action = SetSensorRotation(agent_id="test", rotation_quat=(1, 2, 3, 4))
        d = dict(action)
        self.assertEqual(d["action"], action.name)
        self.assertEqual(d["agent_id"], "test")
        self.assertEqual(d["rotation_quat"], (1, 2, 3, 4))


class SetYawTest(unittest.TestCase):
    def setUp(self) -> None:
        self.action = SetYaw(agent_id="test", rotation_degrees=90)

    def test_delegates_to_sample_set_yaw(self) -> None:
        sampler = Mock()
        sampler.sample_set_yaw = Mock()
        SetYaw.sample(agent_id="test", sampler=sampler)
        sampler.sample_set_yaw.assert_called_once_with("test")

    def test_delegates_to_actuate_set_yaw(self) -> None:
        actuator = Mock()
        actuator.actuate_set_yaw = Mock()
        self.action.act(actuator)
        actuator.actuate_set_yaw.assert_called_once_with(self.action)

    def test_rotation_degrees_returns_configured_rotation_degrees(self) -> None:
        self.assertEqual(90, self.action.rotation_degrees)

    def test_json_serialization(self) -> None:
        s = json.dumps(self.action, cls=ActionJSONEncoder)
        action = cast(SetYaw, json.loads(s, cls=ActionJSONDecoder))
        self.assertEqual(self.action.agent_id, action.agent_id)
        self.assertEqual(self.action.rotation_degrees, action.rotation_degrees)

    def test_dict(self) -> None:
        d = dict(self.action)
        self.assertDictEqual(
            d,
            {
                "action": self.action.name,
                "agent_id": "test",
                "rotation_degrees": 90,
            },
        )


class TurnLeftTest(unittest.TestCase):
    def setUp(self) -> None:
        self.action = TurnLeft(agent_id="test", rotation_degrees=90)

    def test_delegates_to_sample_turn_left(self) -> None:
        sampler = Mock()
        sampler.sample_turn_left = Mock()
        TurnLeft.sample(agent_id="test", sampler=sampler)
        sampler.sample_turn_left.assert_called_once_with("test")

    def test_delegates_to_actuate_turn_left(self) -> None:
        actuator = Mock()
        actuator.actuate_turn_left = Mock()
        self.action.act(actuator)
        actuator.actuate_turn_left.assert_called_once_with(self.action)

    def test_rotation_degrees_returns_configured_rotation_degrees(self) -> None:
        self.assertEqual(90, self.action.rotation_degrees)

    def test_json_serialization(self) -> None:
        s = json.dumps(self.action, cls=ActionJSONEncoder)
        action = cast(TurnLeft, json.loads(s, cls=ActionJSONDecoder))
        self.assertEqual(self.action.agent_id, action.agent_id)
        self.assertEqual(self.action.rotation_degrees, action.rotation_degrees)

    def test_dict(self) -> None:
        d = dict(self.action)
        self.assertDictEqual(
            d,
            {
                "action": self.action.name,
                "agent_id": "test",
                "rotation_degrees": 90,
            },
        )


class TurnRightTest(unittest.TestCase):
    def setUp(self) -> None:
        self.action = TurnRight(agent_id="test", rotation_degrees=90)

    def test_delegates_to_sample_turn_right(self) -> None:
        sampler = Mock()
        sampler.sample_turn_right = Mock()
        TurnRight.sample(agent_id="test", sampler=sampler)
        sampler.sample_turn_right.assert_called_once_with("test")

    def test_delegates_to_actuate_turn_right(self) -> None:
        actuator = Mock()
        actuator.actuate_turn_right = Mock()
        self.action.act(actuator)
        actuator.actuate_turn_right.assert_called_once_with(self.action)

    def test_rotation_degrees_returns_configured_rotation_degrees(self) -> None:
        self.assertEqual(90, self.action.rotation_degrees)

    def test_json_serialization(self) -> None:
        s = json.dumps(self.action, cls=ActionJSONEncoder)
        action = cast(TurnRight, json.loads(s, cls=ActionJSONDecoder))
        self.assertEqual(self.action.agent_id, action.agent_id)
        self.assertEqual(self.action.rotation_degrees, action.rotation_degrees)

    def test_dict(self) -> None:
        d = dict(self.action)
        self.assertDictEqual(
            d,
            {
                "action": self.action.name,
                "agent_id": "test",
                "rotation_degrees": 90,
            },
        )


if __name__ == "__main__":
    unittest.main()
