#include "software/ai/navigator/path_planner/bang_bang_trajectory_1d.h"

#include <gtest/gtest.h>

#include "software/test_util/test_util.h"

class BangBangTrajectory1DTest : public testing::Test
{
   protected:
    void verifyVelocityAndAccelerationLimits(const BangBangTrajectory1D& traj,
                                             double max_vel, double max_accel,
                                             double max_decel)
    {
        for (unsigned int i = 0; i < traj.getTrajectoryParts().size(); i++)
        {
            const auto& part = traj.getTrajectoryParts()[i];
            EXPECT_LE(std::abs(part.velocity), max_vel)
                << "Trajectory part " << i << " has a velocity of " << part.velocity
                << " which has a greater magnitude than the limit of " << max_vel;

            double accel_limit;
            // if velocity and acceleration have opposite signs, then the velocity is
            // going towards 0, so use max_decel.
            if (std::signbit(part.velocity * part.acceleration))
            {
                // Velocity is going towards 0, so use max_decel
                accel_limit = max_decel;
            }
            else
            {
                accel_limit = max_accel;
            }
            EXPECT_LE(std::abs(part.acceleration), std::abs(accel_limit))
                << "Trajectory part " << i << " has an acceleration of "
                << part.acceleration
                << " which has a greater magnitude than the limit of " << accel_limit;
        }
    }

    void verifyChronologicalTime(const BangBangTrajectory1D& traj)
    {
        Duration prev_time = Duration::fromSeconds(0);
        for (unsigned int i = 0; i < traj.getTrajectoryParts().size(); i++)
        {
            const auto& part = traj.getTrajectoryParts()[i];
            EXPECT_GE(part.end_time, prev_time)
                << "Trajectory part " << i << " ends at " << part.end_time
                << " which is greater than the end time of previous part: " << prev_time;
            prev_time = part.end_time;
        }
    }

    void verifyFinalState(const BangBangTrajectory1D& traj, double final_pos,
                          double final_accel)
    {
        EXPECT_TRUE(TestUtil::equalWithinTolerance(
            final_pos, traj.getPosition(traj.getTotalTime()), 0.001));
        // The final velocity should always be 0
        EXPECT_TRUE(TestUtil::equalWithinTolerance(
            0, traj.getVelocity(traj.getTotalTime()), 0.001));
        EXPECT_TRUE(TestUtil::equalWithinTolerance(
            final_accel, traj.getAcceleration(traj.getTotalTime()), 0.001));
    }

    void verifyPartState(const BangBangTrajectory1D& traj, size_t part_index,
                         double end_time, double position, double velocity,
                         double acceleration)
    {
        const auto& part = traj.getTrajectoryParts()[part_index];
        EXPECT_TRUE(
            TestUtil::equalWithinTolerance(end_time, part.end_time.toSeconds(), 0.001))
            << "Trajectory part " << part_index << " ends at " << part.end_time
            << " instead of the expected end time of " << end_time;
        EXPECT_TRUE(TestUtil::equalWithinTolerance(position, part.position, 0.001))
            << "Trajectory part " << part_index << " has a position of " << part.position
            << " instead of the expected position of " << position;
        EXPECT_TRUE(TestUtil::equalWithinTolerance(velocity, part.velocity, 0.001))
            << "Trajectory part " << part_index << " has a velocity of " << part.velocity
            << " instead of the expected velocity of " << velocity;
        EXPECT_TRUE(
            TestUtil::equalWithinTolerance(acceleration, part.acceleration, 0.001))
            << "Trajectory part " << part_index << " has an acceleration of "
            << part.acceleration << " instead of the expected acceleration of "
            << acceleration;
    }
};

TEST_F(BangBangTrajectory1DTest, positive_symmetrical_trapezoidal_profile)
{
    double initial_pos = 0;
    double destination = 3;
    double initial_vel = 0;
    double max_vel     = 1;
    double max_accel   = 1;
    double max_decel   = -1;

    BangBangTrajectory1D traj(initial_pos, destination, initial_vel, max_vel, max_accel,
                              max_decel);
    const auto& parts = traj.getTrajectoryParts();
    EXPECT_EQ(parts.size(), 3);
    verifyVelocityAndAccelerationLimits(traj, max_vel, max_accel, max_decel);
    verifyChronologicalTime(traj);

    // 1.0 sec to accelerate from 0 to 1 m/s (travels 0.5m)
    // 1.0 sec to decelerate from 1 to 0 m/s (travels 0.5m)
    // Remaining 2m travelled at 1 m/s takes 2 sec
    // Total time = 4 sec
    EXPECT_TRUE(
        TestUtil::equalWithinTolerance(4.0, traj.getTotalTime().toSeconds(), 0.001));

    verifyPartState(traj, 0, 1.0, initial_pos, initial_vel, max_accel);
    verifyPartState(traj, 1, 3.0, 0.5, max_vel, 0.0);
    verifyPartState(traj, 2, 4.0, 2.5, max_vel, max_decel);
    verifyFinalState(traj, destination, max_decel);
}

TEST_F(BangBangTrajectory1DTest, positive_non_symmetrical_trapezoidal_profile)
{
    double initial_pos = 2;
    double destination = 8.5;
    double initial_vel = 1;
    double max_vel     = 2;
    double max_accel   = 1;
    double max_decel   = -2;

    BangBangTrajectory1D traj(initial_pos, destination, initial_vel, max_vel, max_accel,
                              max_decel);
    const auto& parts = traj.getTrajectoryParts();
    EXPECT_EQ(parts.size(), 3);
    verifyVelocityAndAccelerationLimits(traj, max_vel, max_accel, max_decel);
    verifyChronologicalTime(traj);

    // 1.0 sec to accelerate from 1 to 2 m/s (travels 1.5m)
    // 1.0 sec to decelerate from 2 to 0 m/s (travels 1m)
    // Remaining 4m travelled at 2 m/s takes 2 sec
    // Total time = 4 sec
    EXPECT_TRUE(
        TestUtil::equalWithinTolerance(4.0, traj.getTotalTime().toSeconds(), 0.001));

    verifyPartState(traj, 0, 1.0, initial_pos, initial_vel, max_accel);
    verifyPartState(traj, 1, 3.0, 3.5, max_vel, 0.0);
    verifyPartState(traj, 2, 4.0, 7.5, max_vel, max_decel);
    verifyFinalState(traj, destination, max_decel);
}

//TEST_F(BangBangTrajectory1DTest, positive_non_symmetrical_trapezoidal_profile_with_negative_initial_velocity)
//{
//    double initial_pos = 2;
//    double destination = 8.5;
//    double initial_vel = 1;
//    double max_vel     = 2;
//    double max_accel   = 1;
//    double max_decel   = -2;
//
//    BangBangTrajectory1D traj(initial_pos, destination, initial_vel, max_vel, max_accel,
//                              max_decel);
//    const auto& parts = traj.getTrajectoryParts();
//    EXPECT_EQ(parts.size(), 3);
//    verifyVelocityAndAccelerationLimits(traj, max_vel, max_accel, max_decel);
//    verifyChronologicalTime(traj);
//
//    // 1.0 sec to accelerate from 1 to 2 m/s (travels 1.5m)
//    // 1.0 sec to decelerate from 2 to 0 m/s (travels 1m)
//    // Remaining 4m travelled at 2 m/s takes 2 sec
//    // Total time = 4 sec
//    EXPECT_TRUE(
//            TestUtil::equalWithinTolerance(4.0, traj.getTotalTime().toSeconds(), 0.001));
//
//    verifyPartState(traj, 0, 1.0, initial_pos, initial_vel, max_accel);
//    verifyPartState(traj, 1, 3.0, 3.5, max_vel, 0.0);
//    verifyPartState(traj, 2, 4.0, 7.5, max_vel, max_decel);
//    verifyFinalState(traj, destination, max_decel);
//}

TEST_F(BangBangTrajectory1DTest, negative_non_symmetrical_trapezoidal_profile)
{
    double initial_pos = -2;
    double destination = -8.5;
    double initial_vel = -1;
    double max_vel     = 2;
    double max_accel   = 1;
    double max_decel   = -2;

    BangBangTrajectory1D traj(initial_pos, destination, initial_vel, max_vel, max_accel,
                              max_decel);
    const auto& parts = traj.getTrajectoryParts();
    EXPECT_EQ(parts.size(), 3);
    verifyVelocityAndAccelerationLimits(traj, max_vel, max_accel, max_decel);
    verifyChronologicalTime(traj);

    // 1.0 sec to accelerate from 1 to 2 m/s (travels 1.5m)
    // 1.0 sec to decelerate from 2 to 0 m/s (travels 1m)
    // Remaining 4m travelled at 2 m/s takes 2 sec
    // Total time = 4 sec
    EXPECT_TRUE(
        TestUtil::equalWithinTolerance(4.0, traj.getTotalTime().toSeconds(), 0.001));

    verifyPartState(traj, 0, 1.0, initial_pos, initial_vel, -max_accel);
    verifyPartState(traj, 1, 3.0, -3.5, -max_vel, 0.0);
    verifyPartState(traj, 2, 4.0, -7.5, -max_vel, -max_decel);
    verifyFinalState(traj, destination, -max_decel);
}

TEST_F(BangBangTrajectory1DTest, positive_non_symmetrical_triangular_profile)
{
    double initial_pos = 2;
    double destination = 10.5;
    double initial_vel = 1;
    // Pick a high max velocity to ensure that the profile is triangular
    double max_vel =
        10;
    double max_accel = 1;
    double max_decel = -2;

    BangBangTrajectory1D traj(initial_pos, destination, initial_vel, max_vel, max_accel,
                              max_decel);
    const auto& parts = traj.getTrajectoryParts();
    EXPECT_EQ(parts.size(), 2);
    verifyVelocityAndAccelerationLimits(traj, max_vel, max_accel, max_decel);
    verifyChronologicalTime(traj);

    // Expected values are determined through Desmos
    // https://www.desmos.com/calculator/lgpc5g8ewr
    EXPECT_TRUE(
        TestUtil::equalWithinTolerance(4.19615, traj.getTotalTime().toSeconds(), 0.001));

    verifyPartState(traj, 0, 2.46410, initial_pos, initial_vel, max_accel);
    verifyPartState(traj, 1, 4.19615, 7.5, 3.46410, max_decel);
    verifyFinalState(traj, destination, max_decel);
}

TEST_F(BangBangTrajectory1DTest, negative_non_symmetrical_triangular_profile)
{
    double initial_pos = -2;
    double destination = -10.5;
    double initial_vel = -1;
    // Pick a high max velocity to ensure that the profile is triangular
    double max_vel = 10;
    double max_accel = 1;
    double max_decel = -2;

    BangBangTrajectory1D traj(initial_pos, destination, initial_vel, max_vel, max_accel,
                              max_decel);
    const auto& parts = traj.getTrajectoryParts();
    EXPECT_EQ(parts.size(), 2);
    verifyVelocityAndAccelerationLimits(traj, max_vel, max_accel, max_decel);
    verifyChronologicalTime(traj);

    // Expected values are determined through Desmos
    // https://www.desmos.com/calculator/lgpc5g8ewr
    EXPECT_TRUE(
        TestUtil::equalWithinTolerance(4.19615, traj.getTotalTime().toSeconds(), 0.001));

    verifyPartState(traj, 0, 2.46410, initial_pos, initial_vel, -max_accel);
    verifyPartState(traj, 1, 4.19615, -7.5, -3.46410, -max_decel);
    verifyFinalState(traj, destination, -max_decel);
}