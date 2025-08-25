#include "software/ai/hl/stp/tactic/primitive.h"


void UniqueObstacleList::clear(){
    obstacles_.clear();
    obstacle_list_.Clear();
}

bool UniqueObstacleList::contains(ObstaclePtr obstacle){
    for(ObstaclePtr in_obstacle: obstacles_){
        if(in_obstacle->isSame(obstacle))
            return true;
    }

    return false;
}

void UniqueObstacleList::addObstacle(ObstaclePtr obstacle){
    if(contains(obstacle))
        return; 

    obstacles_.push_back(obstacle);
    obstacle_list_.add_obstacles()->CopyFrom(obstacle->createObstacleProto());
}

TbotsProto::ObstacleList UniqueObstacleList::getObstacles(){
    return obstacle_list_;
}
