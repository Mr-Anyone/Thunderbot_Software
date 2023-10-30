#include "software/ai/navigator/path_planner/trajectory_planner.h"
#include <gtest/gtest.h>
#include <math.h>
#include <random>

#include "software/test_util/test_util.h"

class BangBangTrajectoryPlannerTest : public testing::Test {
public:       
    TrajectoryPlanner planner;
protected:
    static constexpr int num_points = 10000;
    static constexpr double max_x_velocity = 1; 
    static constexpr double max_y_velocity = 1; 
    static constexpr double max_x_position = 1;
    static constexpr double maximum_acceleration = 1;
    static constexpr double max_y_position = 1;

    Vector getRandomVector()
    {
        double x_vel = vel_uniform_dist(rng) * max_x_velocity;
        double y_vel = vel_uniform_dist(rng) * max_y_velocity;

        return Vector(x_vel, y_vel);
    }

    Point getRandomPoint()
    {
        double x_pos = vel_uniform_dist(rng) * max_x_position;
        double y_pos = vel_uniform_dist(rng) * max_y_position;

        return Point(x_pos, y_pos);
    }

    std::mt19937 rng;
    std::uniform_real_distribution<> pos_uniform_dist;
    std::uniform_real_distribution<> vel_uniform_dist;

};

void generateColumnName(){
    LOG(CSV, "path_summary.csv") << "sub_dest_x,sub_dest_y,connection_time,duration,start_x,start_y,end_x,end_y,initial_vel(x),initial_vel(y),"; 
    for(int i = 1;i<=sample_counts; ++i){
        if(i == sample_counts){
            LOG(CSV, "path_summary.csv") << "x" << std::to_string(i) << "," <<  "y" << std::to_string(i);
            break;
        }
        LOG(CSV, "path_summary.csv") << "x" << std::to_string(i) << "," <<  "y" << std::to_string(i)<< ",";
    }
    LOG(CSV, "path_summary.csv") << "\n";
}

TEST_F(BangBangTrajectoryPlannerTest, generate_path){
    double maximum_velocity = sqrt(max_x_position * max_x_position + max_y_velocity * max_y_velocity);
    KinematicConstraints constraints = {maximum_velocity, BangBangTrajectoryPlannerTest::maximum_acceleration, BangBangTrajectoryPlannerTest::maximum_acceleration};

    // generate the column names 
    generateColumnName();
    for(int i = 0; i<BangBangTrajectoryPlannerTest::num_points; ++i){
        Point start_pos = getRandomPoint();
        Point destination = getRandomPoint();
        Vector velocity = getRandomVector();

        TrajectoryPath path = planner.findTrajectory(start_pos, destination, velocity, constraints, {}, Field::createSSLDivisionBField().fieldBoundary());
    }
}
