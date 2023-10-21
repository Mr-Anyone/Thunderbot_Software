#include "software/ai/navigator/path_planner/trajectory_planner.h"
#include <gtest/gtest.h>

#include <random>

#include "software/test_util/test_util.h"

class BangBangTrajectoryPlannerTest : public testing::Test
{
public:       
    TrajectoryPlanner planner;
};

TEST_F(BangBangTrajectoryPlannerTest, generate_path){
    KinematicConstraints constraints = {1, 1, 1};
    TrajectoryPath path = planner.findTrajectory({0, 0}, {1, 0}, {1, 1}, constraints, {}, Field::createSSLDivisionBField().fieldBoundary());

    LOG(DEBUG) << "I've ran";
}
