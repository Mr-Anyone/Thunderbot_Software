#include "software/ai/navigator/path_planner/trajectory_path_with_cost.h"

TrajectoryPathWithCost::TrajectoryPathWithCost(const TrajectoryPath &traj_path,
                                               double cost)
    : traj_path(traj_path), cost(cost)
{
}

bool TrajectoryPathWithCost::collides() const
{
    return colliding_obstacle != nullptr ||
           first_collision_time < traj_path.getTotalTime();
}