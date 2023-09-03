#pragma once

#include <optional>

#include "extlibs/AABB/AABB.h"
#include "software/ai/navigator/obstacle/obstacle.hpp"
#include "software/ai/navigator/path_planner/trajectory_path.h"

class TrajectoryPlanner
{
   public:
    TrajectoryPlanner();

    TrajectoryPath findTrajectory(const Point &start, const Point &destination,
                                  const Vector &initial_velocity,
                                  const KinematicConstraints &constraints,
                                  const std::vector<ObstaclePtr> &obstacles,
                                  const Rectangle &navigable_area);

   private:
    double calculateCost(const TrajectoryPath &trajectory_path, aabb::Tree &obstacle_tree,
                         const std::vector<ObstaclePtr> &obstacles);

    std::vector<Vector> relative_sub_destinations;

    const Duration SUB_DESTINATION_STEP_INTERVAL = Duration::fromSeconds(0.2);
    const Duration COLLISION_CHECK_STEP_INTERVAL = Duration::fromSeconds(0.1);
    const Duration MAX_FUTURE_COLLISION_CHECK = Duration::fromSeconds(3.0);

    static constexpr std::array<double, 4> SUB_DESTINATION_DISTANCES_METERS = {
        0.1, 1, 2, 3};
    static constexpr unsigned int NUM_SUB_DESTINATION_ANGLES = 15;
    static constexpr double PATH_WITH_COLLISION_COST         = 5.0;
};
