#pragma once

#include "software/geom/circle.h"
#include "software/geom/polygon.h"
#include "software/geom/rectangle.h"
#include "software/geom/stadium.h"


/**
 * Returns the axis-aligned bounding box of the given circle, inflated by the given
 *
 * @param shape The shape which the AABB of should be generated
 * @param inflation_radius Extran distance to add to the AABB in both dimensions
 * @return A rectangle which represents the AABB of the shape
 */
Tbots::Rectangle axisAlignedBoundingBox(const Circle& circle, const double inflation_radius = 0);
Tbots::Rectangle axisAlignedBoundingBox(const Tbots::Rectangle& rectangle,
                                 const double inflation_radius = 0);
Tbots::Rectangle axisAlignedBoundingBox(const Tbots::Polygon& polygon,
                                 const double inflation_radius = 0);
Tbots::Rectangle axisAlignedBoundingBox(const Stadium& stadium,
                                 const double inflation_radius = 0);
