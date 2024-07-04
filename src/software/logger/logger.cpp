#include "logger.h"

#include "base64.h"

static const std::string TYPE_DELIMITER = "!!!";

std::ostream& operator<<(std::ostream& os, const google::protobuf::Message& message)
{
    // We have to base64 encode the serialized protobuf before sending it to
    // g3log since g3log treats \n characters as a new log msg which breaks the serialized
    // protobuf
    os << TYPE_DELIMITER << message.GetTypeName() << TYPE_DELIMITER
       << base64_encode(message.SerializeAsString());
    return os;
}
